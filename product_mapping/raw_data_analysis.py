# TODO: https://developers.google.com/machine-learning/guides/text-classification/step-2-5
import pdb
import csv
import json

import heuristic

SIGNALS = ['GM_ADVERTISER_NAME', 'GM_SECTOR_NAME', 'GM_SUBSECTOR_NAME',
           'GM_CATEGORY_NAME', 'GM_BRAND_NAME', 'GM_PRODUCT_NAME']
TARGET_CATEGORY = 'CP_SUBCATEGORY_NAME'
EXCLUDED_WORDS = {'N/A'}

query_name = 'mapped_items'
print('Loading data from remote database using query:', heuristic.QUERIES[query_name])
mapping_data = json.loads(heuristic.get_data_from_query(query_name))

word_lens = set()
uniq_chars = set()
input_output = {}

num_of_sample = 0
num_of_words = 0
for row in mapping_data:
    num_of_sample += 1
    cur_word = []
    for sig in SIGNALS:
        if row[sig] not in EXCLUDED_WORDS:
            cur_word.append(row[sig])
    cur_word_str = ' '.join(cur_word)
    tokenized_word = ' '.join(heuristic.tokenize(cur_word_str))
    num_of_words += len(tokenized_word)
    word_lens.add(len(tokenized_word))
    input_output[tokenized_word] = row[TARGET_CATEGORY]

    for chr in tokenized_word:
        uniq_chars.add(chr)

print(num_of_sample) # S = 150057
print(num_of_words) # W = 15991476
print('Finished')

