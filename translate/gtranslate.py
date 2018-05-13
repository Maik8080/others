import requests
import io
import json
import re
import pandas as pd
import pdb


# REF: https://stackoverflow.com/q/37667671
# REF: https://web.archive.org/web/20180513001508/https://ctrlq.org/code/19909-google-translate-api
# REF: https://web.archive.org/web/20180513001611/https://ctrlq.org/code/19899-google-translate-languages

def translate(text, source_language, target_language):
    error_msg = 'Translation error'
    base_url= 'https://translate.googleapis.com/translate_a/single?client=gtx&dt=t'
    source_lang= '&sl=' + source_language
    target_lang= '&tl=' + target_language
    text= '&q=' + text
    url = base_url + source_lang + target_lang + text
    rq = requests.get(url)
    if rq.status_code == 200:
        translated_text = json.load(io.StringIO(rq.text))
        return translated_text[0][0][0]
    return error_msg


def clean_text(text):
    str_before_comma=text.split(',')[0]
    regex = re.compile('[^a-zA-Z]') # remove non-alphabetical stuff
    str_with_only_alphabets = regex.sub(' ', str_before_comma)
    str_with_just_one_space_allowed = ' '.join(str_with_only_alphabets.split())
    str_lowered = str_with_just_one_space_allowed.lower() # this has positive effect on translation accuracy
    return str_lowered


if __name__ == "__main__":
    source_lang = 'de'
    target_lang = 'en'
    df = pd.read_excel(open('to_translate.xlsx', 'rb'), sheetname='Products_Mapping')
    cols = ['GM_COUNTRY_NAME', 'GM_ADVERTISER_NAME', 'GM_SECTOR_NAME', 'GM_CATEGORY_NAME', 'GM_BRAND_NAME',
            'GM_PRODUCT_NAME', 'SOS_PRODUCT']
    cols_to_translate = ['GM_COUNTRY_NAME', 'GM_ADVERTISER_NAME', 'GM_SECTOR_NAME', 'GM_CATEGORY_NAME', 'GM_BRAND_NAME',
                         'GM_PRODUCT_NAME']
    translated_output = []

    for i, r in df.iterrows():
        cur_row = []
        for c in cols_to_translate:
            cur_row.append(r[c])
            cleaned_txt = clean_text(r[c])
            translated_text = translate(cleaned_txt, source_lang, target_lang)
            cur_row.append(translated_text)
        cur_row.append(r['SOS_PRODUCT'])
        print(cur_row)
        translated_output.append(cur_row)

    final_cols = [j for c in cols_to_translate for j in [c, '{}_Translated'.format(c)]] + ['SOS_PRODUCT']
    df_out = pd.DataFrame(translated_output, columns=final_cols)
    df_out.to_excel('translated.xlsx', index=False)
    # writer = pd.ExcelWriter('translated.xlsx')
    # df_out.to_excel(writer, index=False)
    # writer.save()
    print('Translation finished')

