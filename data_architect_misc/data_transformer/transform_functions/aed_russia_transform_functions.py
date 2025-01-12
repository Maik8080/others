"""This is the subclass of Transform function for Russia (AED division).

We will define transform functions specific to Russia here.

Author: Phyo Thiha
Last Modified: April 7, 2020
"""

import pandas as pd

from constants import comp_harm_constants
from transform_functions.common_comp_harm_transform_functions import CommonCompHarmTransformFunctions


class AedRussiaTransformFunctions(CommonCompHarmTransformFunctions):
    """
    All custom (uncommon) transform functions **SPECIFIC to
    individual processing task** must be defined as part
    of this class.
    """

    def __init__(self, config):
        self.config = config

    def rename_HARMONIZED_CATEGORY_data_using_dictionary_values(
            self,
            df
    ):
        # As of July 8, 2020, Phyo and Maicol decided that
        # we will map multi-category advertisements for Russia into OC for now
        temporary_harmonized_category_mappings_for_russia = {
            "OC/PC": "Oral Care",
            "OC/HC/PC": "Oral Care",
            "HC/PC": "Oral Care"
        }
        df[comp_harm_constants.CATEGORY_COLUMN] = df[comp_harm_constants.CATEGORY_COLUMN]\
            .replace(temporary_harmonized_category_mappings_for_russia)

        return df
