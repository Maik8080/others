DATABASE = "[DM_1219_ColgateGlobal].[dbo]"

all_mappings_q = """
SELECT  GM_COUNTRY_NAME
       ,GM_ADVERTISER_NAME
       ,GM_SECTOR_NAME
       ,GM_SUBSECTOR_NAME
       ,GM_CATEGORY_NAME
       ,GM_BRAND_NAME
       ,GM_PRODUCT_NAME
       ,CP_SUBCATEGORY_ID
       ,CP_SUBCATEGORY_NAME
       ,CP_VARIANT_ID_1PH
       ,CP_VARIANT_NAME
FROM {}.GM_CP_MASTER_PRODUCT_MAPPING
""".format(DATABASE)

mapped_subcategories_q = """
SELECT
GM_GLOBAL_PRODUCT_ID
,GM_COUNTRY_ID
,GM_COUNTRY_NAME
,GM_ADVERTISER_NAME
,GM_SECTOR_NAME
,GM_SUBSECTOR_NAME
,GM_CATEGORY_NAME
,GM_BRAND_NAME
,GM_PRODUCT_NAME
,SOS_PRODUCT
,CP_SUBCATEGORY_ID
,CP_SUBCATEGORY_NAME
,CP_VARIANT_ID_1PH
,CP_BRAND_ID
,CP_BRAND_NAME
,LAST_MAPPED_BY
FROM {}.GM_CP_MASTER_PRODUCT_MAPPING
WHERE CP_SUBCATEGORY_NAME IS NOT NULL
""".format(DATABASE)

unmapped_subcategories_q = """
SELECT
GM_GLOBAL_PRODUCT_ID
,GM_COUNTRY_ID
,GM_COUNTRY_NAME
,GM_ADVERTISER_NAME
,GM_SECTOR_NAME
,GM_SUBSECTOR_NAME
,GM_CATEGORY_NAME
,GM_BRAND_NAME
,GM_PRODUCT_NAME
,SOS_PRODUCT
,CP_SUBCATEGORY_ID
,CP_SUBCATEGORY_NAME
,CP_VARIANT_ID_1PH
,CP_BRAND_ID
,CP_BRAND_NAME
,LAST_MAPPED_BY
FROM {}.GM_CP_MASTER_PRODUCT_MAPPING
WHERE CP_SUBCATEGORY_NAME IS NULL
""".format(DATABASE)
# SELECT  A.GM_COUNTRY_NAME
#        ,A.GM_ADVERTISER_NAME
#        ,A.GM_SECTOR_NAME
#        ,A.GM_SUBSECTOR_NAME
#        ,A.GM_CATEGORY_NAME
#        ,A.GM_BRAND_NAME
#        ,A.GM_PRODUCT_NAME
#        ,A.CP_SUBCATEGORY_ID
#        ,A.CP_SUBCATEGORY_NAME
#        ,A.CP_VARIANT_ID_1PH
#        ,A.CP_VARIANT_NAME
# FROM {}.GM_CP_MASTER_PRODUCT_MAPPING AS A
# WHERE A.CP_SUBCATEGORY_NAME IS NULL

distinct_subcat_name_and_id_q = """
SELECT DISTINCT CP_SUBCATEGORY_ID, CP_SUBCATEGORY_NAME
FROM {}.GM_CP_MASTER_PRODUCT_MAPPING
WHERE CP_SUBCATEGORY_ID IS NOT NULL
""".format(DATABASE)