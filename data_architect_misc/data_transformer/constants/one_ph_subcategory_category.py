"""
To retrieve data from 1PH table for this file, use this SQL query -
SELECT DISTINCT
[SUBCATEGORY_NAME],
[CATEGORY_NAME]
FROM [dbo].[CP_DIM_PRODUCT_1PH]
WHERE [CATEGORY_NAME] IS NOT NULL
ORDER BY 1, 2

and copy/paste that into a blank Excel file. Then use this Excel
formula -
="'"&A2&"': '"&B2&"',"

in column 'C' and replace the existing variable,
'subcategory_category_relations', below.
"""
from constants.comp_harm_constants import NOT_AVAILABLE

last_updated = '2020-10-05'
subcategory_category_relations = {
    # Sometimes in countries like Guatemala, we do not receive subcategory column.
    # Then, we must assign them to 'Not Available' as subcategory and leave category as empty. 
    NOT_AVAILABLE: NOT_AVAILABLE,

    'Air Freshners': 'Home Care',
    'Bleach': 'Home Care',
    'Cleaners Glass': 'Home Care',
    'Cleaners Liquid / Gel': 'Home Care',
    'Cleaners Other': 'Home Care',
    'Cleaners Regimen': 'Home Care',
    'Cleaners Scourer': 'Home Care',
    'Cleaners Spray': 'Home Care',
    'Cleaners Toilet': 'Home Care',
    'Cleaners Wipes': 'Home Care',
    'Dish Auto': 'Home Care',
    'Dish Hand': 'Home Care',
    'Dry Clean': 'Home Care',
    'FC Liquids': 'Home Care',
    'FC Other': 'Home Care',
    'FC Regimen': 'Home Care',
    'FC Sheets': 'Home Care',
    'FD Fabric Shampoo': 'Home Care',
    'FD Laundry Bars': 'Home Care',
    'FD Other': 'Home Care',
    'HC Regimen': 'Home Care',
    'Home Care HALB SC': 'Home Care',
    'Home Care HALB SC -': 'Home Care',
    'Home Care PROM SC': 'Home Care',
    'Home Care ROH SC': 'Home Care',
    'Home Care VERP SC': 'Home Care',
    'Home Care ZPRM SC': 'Home Care',
    'Household Cleaners NC': 'Home Care',
    'Laundry Pre-wash': 'Home Care',
    'Other Home Care NC': 'Home Care',
    'Paper Products': 'Home Care',
    'Scourers': 'Home Care',
    'Toilet': 'Home Care',

    'At Home Whitening': 'Oral Care',
    'Battery TB': 'Oral Care',
    'Electric TB': 'Oral Care',
    'Hybrid TB': 'Oral Care',
    'Interdental': 'Oral Care',
    'Manual TB': 'Oral Care',
    'Mouthwash': 'Oral Care',
    'OC Regimen': 'Oral Care',
    'On The Go': 'Oral Care',
    'Oral Care HALB SC': 'Oral Care',
    'Oral Care HALB SC -': 'Oral Care',
    'Oral Care PROM SC': 'Oral Care',
    'Oral Care ROH SC': 'Oral Care',
    'Oral Care VERP SC': 'Oral Care',
    'Oral Care ZPRM SC': 'Oral Care',
    'Other Oral Care NC': 'Oral Care',
    'PP High Fluoride': 'Oral Care',
    'Replacement Head PTB': 'Oral Care',
    'Tongue Cleaner': 'Oral Care',
    'Toothpaste': 'Oral Care',
    'Toothpowder': 'Oral Care',

    'AP/Deo': 'Personal Care',
    'Baby Accessories': 'Personal Care',
    'Bar Soap': 'Personal Care',
    'Bath Foam': 'Personal Care',
    'Bath Foam - OBS': 'Personal Care',
    'Body Care Other': 'Personal Care',
    'Body Cleansing Regimen': 'Personal Care',
    'Body Lotion': 'Personal Care',
    'Body Wash': 'Personal Care',
    'Conditioner': 'Personal Care',
    'Cosmetics': 'Personal Care',
    'Diapers & Wipes': 'Personal Care',
    'Facial Care': 'Personal Care',
    'Feminine Protection': 'Personal Care',
    'Hair Care Regimen': 'Personal Care',
    'Hair Care Styling Aids': 'Personal Care',
    'Hair Care Treatment': 'Personal Care',
    'Hair Colorants': 'Personal Care',
    'Hair Removal / Shave': 'Personal Care',
    'Hand Lotion': 'Personal Care',
    'Hand Lotion - OBS': 'Personal Care',
    'Hand Sanitizer': 'Personal Care',
    'Intimate Care': 'Personal Care',
    'Liquid Hand Wash': 'Personal Care',
    'Lotion': 'Personal Care',
    'Other Personal Care NC': 'Personal Care',
    'PCP Regimen': 'Personal Care',
    'Personal Care HALB S': 'Personal Care',
    'Personal Care PROM S': 'Personal Care',
    'Personal Care ROH SC': 'Personal Care',
    'Personal Care SUC Mi': 'Personal Care',
    'Personal Care VERP S': 'Personal Care',
    'Personal Care ZPRM S': 'Personal Care',
    'Professional Skin Care': 'Personal Care',
    'Shampoo': 'Personal Care',
    'Shave Prep': 'Personal Care',
    'Shower Gel': 'Personal Care',
    'Skin Care Other': 'Personal Care',
    'Talcum Powder': 'Personal Care',

    'Cat Dry': 'Pet Nutrition',
    'Cat Treat': 'Pet Nutrition',
    'Cat Wet': 'Pet Nutrition',
    'Dog Dry': 'Pet Nutrition',
    'Dog Treat': 'Pet Nutrition',
    'Dog Wet': 'Pet Nutrition',
    'Pet Food': 'Pet Nutrition',
    'Pet Nutrition Other SC': 'Pet Nutrition',

    'Food & Beverages': 'Other',
    'Institutional': 'Other',
    'Other Sub Cat': 'Other',
    'Pharmaceuticals & Vitamins': 'Other',
}