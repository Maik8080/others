import pdb

import argparse
import datetime
import json
import os
import sys

import pandas as pd

import heuristic

INPUT_DIR = 'input'
OUTPUT_DIR = 'output'
INPUT_SIGNALS = ['GM_ADVERTISER_NAME', 'GM_SECTOR_NAME', 'GM_SUBSECTOR_NAME',
                 'GM_CATEGORY_NAME', 'GM_BRAND_NAME', 'GM_PRODUCT_NAME']

if __name__ == '__main__':
    desc = '''
    Guess mappings based on heuristic of previously mapped items.
    This program can take an input file (use '-i' flag) with raw (unmapped)
    data and output a file ('input_file_name-yyyyddmm.csv') which includes 
    mapped data.
    It can also pull unmapped data directly from the database (use '-d' flag).
    For more detail, please use '-h' flag.
    '''

    cur_date = datetime.datetime.now().strftime('%Y-%m-%d-%H%M%S')
    cur_dir_path = os.path.dirname(os.path.realpath(__file__))
    input_dir = os.path.join(cur_dir_path, INPUT_DIR)
    output_dir = os.path.join(cur_dir_path, OUTPUT_DIR)
    output_in_csv = False

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    parser = argparse.ArgumentParser(description=desc)
    parser.add_argument('-f',
                        help="Input file which contains unmapped data. The file must be placed in this folder: " +
                        INPUT_DIR)
    parser.add_argument('-d',
                        type=int,
                        default=1,
                        help="If set to '1', the unmapped data will be pulled directly from the database table.")
    args = parser.parse_args()

    if (args.f is None) and (args.d is None):
        print("You must provide either the input file (path+name) or \n"
              "use '-d' flag to pull input from database directly.\n"
              "For more detail, please use '-h' flag.")
        sys.exit()

    query_name = 'all_mappings'
    print('Loading data from remote database using query:', heuristic.QUERIES[query_name])
    mapping_data = json.loads(heuristic.get_data_from_query(query_name))
    word_cnt_tbl = heuristic.build_total_word_cnt_table(mapping_data, heuristic.SIGNALS)

    if args.f:
        input_file = os.path.join(input_dir, args.f)
        filename, file_extension = os.path.splitext(args.f)
        if file_extension == '.csv':
            output_file = os.path.join(output_dir, (args.f + '-' + cur_date + '.csv'))
            output_in_csv = True
            df = pd.read_csv(input_file, index_col=False)
        elif file_extension == '.xlsx':
            output_file = os.path.join(output_dir, (args.f + '-' + cur_date + '.xlsx'))
            df = pd.read_excel(input_file, index_col=False)
        else:
            print("The file format (extension) is not supported. Only CSV and XLSX as input file will work.")
            sys.exit()
        input_data = df.to_json(orient='records')
    elif args.d:
        output_file = os.path.join(output_dir, ('database_pull' + '-' + cur_date + '.xlsx'))
        query_name = 'unmapped_items'
        print('Pulling input data from remote database using query:', heuristic.QUERIES[query_name])
        input_data = heuristic.get_data_from_query(query_name)
    else:
        pass

    input_data = json.loads(input_data)
    output_data = []
    for input_row in input_data:
        print("\n------------")
        print("Current row:")
        print(input_row)
        uniq_input_words = set()
        for sig in INPUT_SIGNALS:
            if input_row[sig] is not None:
                uniq_input_words.add(input_row[sig])

        uniq_input_words = list(uniq_input_words - heuristic.EXCLUDED_WORDS)
        if len(uniq_input_words) == 0:
            input_row['CP_SUBCATEGORY_NAME'] = heuristic.NOT_ENOUGH_WORDS
        else:
            suggestions = heuristic.get_suggestions(word_cnt_tbl, ' '.join(uniq_input_words))
            if len(suggestions) > 2:
                # if a lot of suggestions were returned originally, try to filter out noisy words
                helpful_words = heuristic.get_helpful_words(suggestions)
                if len(helpful_words) > 0:
                    print("\nGot enhanced suggestions:")
                    suggestions = heuristic.get_suggestions(word_cnt_tbl, ' '.join(helpful_words))
                else:
                    suggestions = [(heuristic.AMBIGUOUS,)]

            print(suggestions)
            print("------------\n")
            input_row['CP_SUBCATEGORY_NAME'] = suggestions[0][0] if len(suggestions) > 0 else heuristic.NO_SUGGESTIONS

        output_data.append(input_row)

    cols = list(output_data[0].keys())
    df = pd.DataFrame.from_dict(output_data)
    if output_in_csv:
        df.to_csv(output_file, index=False, columns=cols)
    else:
        df.to_excel(output_file, index=False, columns=cols)
    print("Output written in:", output_file)
    print("Program successfully finished.\n")