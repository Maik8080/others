"""This is the subclass of Transform function for South Africa (AED division).

We will define transform functions specific to South Africa here.

Author: Phyo Thiha
Last Modified: November 30, 2020
"""

import logging

from constants import comp_harm_constants
from transform_functions.common_comp_harm_transform_functions import CommonCompHarmTransformFunctions


class AedSouthAfricaTransformFunctions(CommonCompHarmTransformFunctions):
    """
    All custom (uncommon) transform functions **SPECIFIC to
    individual processing task** must be defined as part
    of this class.
    """

    SOUTH_AFRICA_SPECIFIC_CATEGORY_MAPPINGS = {
        # TODO: Merge the list below with comp_harm_constants.ENGLISH_CATEGORY_MAPPINGS
        # Excel formula to create these mappings is: =",'(?i)^"&A2&"$': '"&B2&"'"
        '(?i)^FOUNDATION$': 'Other'
        , '(?i)^CORPORATE ADVERTISING$': 'Other'
        , '(?i)^INSECTICIDES REPELLENTS & PEST$': 'Other'
        , '(?i)^FOOD SPONSORSHIP$': 'Other'
        , '(?i)^BABY EQUIPMENT & PRODUCTS$': 'Other'
        , '(?i)^ENERGY DRINKS$': 'Other'
        , '(?i)^BABY FOOD BOTTLED/BOXED/CEREAL$': 'Other'
        , '(?i)^COMPANIES CORPORATE$': 'Other'
        , '(?i)^ADHESIVES SEALANTS$': 'Other'
        , '(?i)^BABY GROOMING$': 'Personal Care'
        , '(?i)^FACE CARE PRODUCT RANGE$': 'Personal Care'
        , '(?i)^HAND & BODY$': 'Personal Care'
        , '(?i)^SANPRO RANGE$': 'Personal Care'
        , '(?i)^SANPRO PADS$': 'Personal Care'
        , '(?i)^TOOTHPASTE$': 'Oral Care'
        , '(?i)^CONCERT & THEATRE SHOWS$': 'Other'
        , '(?i)^DETERGENT HEAVY DUTY$': 'Home Care'
        , '(?i)^DETERGENT LIGHT DUTY$': 'Home Care'
        , '(?i)^COMPLEX AND FACE MOISTURISING$': 'Personal Care'
        , '(?i)^DEODORANTS$': 'Personal Care'
        , '(?i)^COLD AND FLU REMEDIES$': 'Other'
        , '(?i)^APPLIANCES KITCHEN$': 'Home Care'
        , '(?i)^PERFUME/COLOGNE RANGE$': 'Personal Care'
        , '(?i)^BABY CARE$': 'Personal Care'
        , '(?i)^HOUSEHOLD CLEANERS$': 'Home Care'
        , '(?i)^FLOORPOLISH TILE CLEANER$': 'Home Care'
        , '(?i)^MEDICINES$': 'Other'
        , '(?i)^TOOTHBRUSHES$': 'Oral Care'
        , '(?i)^DENTAL CARE$': 'Oral Care'
        , '(?i)^DETERGENT FABRIC SOFTNER$': 'Home Care'
        , '(?i)^HAIR RELAXERS$': 'Personal Care'
        , '(?i)^ETHNIC HAIR CONDITIONERS$': 'Personal Care'
        , '(?i)^ETHNIC HAIR STYLING$': 'Personal Care'
        , '(?i)^SOAP LIQUID/BAR$': 'Personal Care'
        , '(?i)^BATH AND SHOWER$': 'Personal Care'
        , '(?i)^ANTISEPTIC$': 'Other'
        , '(?i)^PAIN TREATMENT OR ANALGESICS$': 'Other'
        , '(?i)^FRAGRANCE FEMALE$': 'Personal Care'
        , '(?i)^FRAGRANCE MALE$': 'Personal Care'
        , '(?i)^CHARITY/ FUND RAISING/ WELFARE$': 'Other'
        , '(?i)^TOILET CLEANSER$': 'Home Care'
        , '(?i)^CAUCASIAN HAIR TREATMENTS$': 'Personal Care'
        , '(?i)^HEALTH & BEAUTY SPONSORSHIP$': 'Personal Care'
        , '(?i)^CONDOMS$': 'Other'
        , '(?i)^MEDICAL EQUIPMENT$': 'Other'
        , '(?i)^ACNE PREPS$': 'Personal Care'
        , '(?i)^ETHNIC SKINCARE$': 'Personal Care'
        , '(?i)^ANTI AGEING$': 'Personal Care'
        , '(?i)^SUN CARE$': 'Personal Care'
        , '(?i)^DISHWASHING LIQUID / AUTO$': 'Home Care'
        , '(?i)^DISHWASHING TABLETS$': 'Home Care'
        , '(?i)^VITAMINS AND BODY BUILD PRODUCTS$': 'Other'
        , '(?i)^FACE CARE & CLEANSING$': 'Personal Care'
        , '(?i)^ETHNIC HAIR COLOUR$': 'Personal Care'
        , '(?i)^CAUCASIAN HAIR COLOUR$': 'Personal Care'
        , '(?i)^CAUCASIAN HAIR RANGE$': 'Personal Care'
        , '(?i)^CAUCASIAN HAIR STYLING$': 'Personal Care'
        , '(?i)^ANTACIDS$': 'Other'
        , '(?i).*LAUNDRY.*': 'Home Care'
        , '(?i)^SHAVING PREPARATIONS FEMALE$': 'Personal Care'
        , '(?i)^HAIR REMOVAL SYSTEM$': 'Personal Care'
        , '(?i)^RAZORS / BLADES$': 'Personal Care'
        , '(?i)^SHAVING PREPARATIONS MALE$': 'Personal Care'
        , '(?i)^AIRFRESHENER & ODOUR REMOVERS$': 'Home Care'
        , '(?i)^CAUCASIAN HAIR SHAMPOO$': 'Personal Care'
        , '(?i)^MAYONNAISE SALAD CREAM/SALAD DRESSING$': 'Other'
        , '(?i)^ICE CREAM & FROZEN CONFECTION$': 'Other'
        , '(?i)^SHOE POLISH$': 'Home Care'
        , '(?i)^HERBS /SPICES & SALT/VEG DRIED$': 'Other'
        , '(?i)^PACKET SOUP/CANNED SOUP$': 'Other'
        , '(?i)^FOOD RANGE$': 'Other'
        , '(?i)^SAUCES BROWN BRAAI/SWEET /COOKING/PASTA$': 'Other'
        , '(?i)^SOUP STOCK CUBES TABLETS POWDER$': 'Other'
        , '(?i)^LIP BALM$': 'Personal Care'
        , '(?i)^ICED TEA AND ICED COFFEE$': 'Other'
        , '(?i)^CORPORATE$': 'Other'
        , '(?i)^BREATH FRESHENERS$': 'Oral Care'
        , '(?i)^COSMETIC.*?RANGE$': 'Personal Care'
        , '(?i)^LIP COLOUR$': 'Personal Care'
        , '(?i)^MASCARA$': 'Personal Care'
        , '(?i)^SOCIAL UPLIFTMENT BUSINESS INITIATIVES$': 'Other'
        , '(?i)^BUSINESS AWARDS$': 'Other'
        , '(?i)^ETHNIC HAIR RANGE$': 'Personal Care'
        , '(?i)^MEN TOILETRIES$': 'Personal Care'
        , '(?i)^ETHNIC HAIR SHAMPOO$': 'Personal Care'
        , '(?i)^NAPPIES DISPOSABLE AND TOWEL$': 'Personal Care'
        , '(?i)^CAUCASIAN HAIR CONDITIONERS$': 'Personal Care'
        , '(?i)^DETERGENT PREWASH$': 'Home Care'
        , '(?i)^CLINIC HOSPITAL HOME NURSING$': 'Other'
        , '(?i)^NASAL SPRAYS AND DROPS$': 'Other'
        , '(?i)^AWARENESS CAMPAIGNS$': 'Other'
        , '(?i)^BLEACH$': 'Home Care'
        , '(?i)^BODY RUBS / PAIN RELIEF$': 'Other'
        , '(?i)^FINANCIAL STATEMENTS$': 'Other'
        , '(?i)^ETHNIC HAIR TREATMENTS$': 'Personal Care'
        , '(?i)^FIRST AID DRESSINGS$': 'Other'
        , '(?i)^ROOIBOS TEA$': 'Other'
        , '(?i)^TEA$': 'Other'
        , '(?i)^FEMININE HEALTH PREPARATIONS$': 'Personal Care'
        , '(?i)^ASTHMA CARE$': 'Other'
        , '(?i)^SMOKING CURES$': 'Other'
        , '(?i)^DISINFECTANTS DRAIN$': 'Home Care'
        , '(?i)^NATURAL & ALTERNATIVE MEDICATION$': 'Other'
        , '(?i)^COSMETICS AUTO$': 'Personal Care'
        , '(?i)^FOOD CORPORATE$': 'Other'
        , '(?i)^HOUSEHOLD SPONSORSHIP$': 'Home Care'
        , '(?i)^DIETS & SLIMMING AIDS$': 'Other'
    }

    def __init__(self, config):
        self.config = config
        self.logger = logging.getLogger(__name__)
        # Define self.category_mappings below if we want to use
        # specific category mapping for this country
        self.category_mappings = dict(
            comp_harm_constants.ENGLISH_CATEGORY_MAPPINGS,
            **AedSouthAfricaTransformFunctions.SOUTH_AFRICA_SPECIFIC_CATEGORY_MAPPINGS)

    def drop_data_with_non_standard_categories_from_HARMONIZED_CATEGORY_column(
            self,
            df):
        """
        We will drop the rows that have unexpected (non standard) category names
        in HARMONIZED_CATEGORY column.
        """
        NON_STANDARD_HARMONIZED_CATEGORY = [
            "EYEWEAR SPECTACLES CONTACT LENS",
            "CONFERENCES & CONFERENCE CENTRES",
            "EYE CARE",
            "BABY CARE SPONSORSHIP"
        ]

        self.logger.warning(
            f"These categories {NON_STANDARD_HARMONIZED_CATEGORY} "
            f"were deleted from the raw data because they do NOT "
            f"belong to standard categories in comp harm project."
        )

        df = df[~df[comp_harm_constants.CATEGORY_COLUMN].apply(
            lambda x: True
            if x in NON_STANDARD_HARMONIZED_CATEGORY
            else False)]

        return df
