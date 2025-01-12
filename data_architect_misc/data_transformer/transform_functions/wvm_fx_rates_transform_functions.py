"""
This class has transform functions to clean and transform
the foreign exchange rates data for
WorldView Media (WVM) dashboard.

Author: Phyo Thiha
Last Modified: June 16, 2020
"""
import datetime
import re

import pandas as pd

from constants.fx_rates_constants import *
from constants.comp_harm_constants import COUNTRIES as COMP_HARM_PROJECT_COUNTRIES

from transform_functions.common_transform_functions import CommonTransformFunctions
from qa_functions.common_comp_harm_qa_functions import CommonCompHarmQAFunctions
from qa_functions.qa_errors import \
    InsufficientNumberOfColumnsError, \
    InvalidValueFoundError, \
    NullValueFoundError, \
    UnexpectedColumnNameFoundError, \
    UnexpectedColumnValuesFoundError


def generate_one_yyyy_mm_dd_string_for_each_month_of_the_year(year):
    first_days_of_all_months = ['-'.join([str(year), str(i), '1'])
                                for i in range(1, 13)]
    return [datetime.datetime.strptime(d, '%Y-%m-%d').strftime('%Y-%m-%d') for d in first_days_of_all_months]


class WvmFxRatesTransformFunctions(CommonTransformFunctions, CommonCompHarmQAFunctions):

    # We will have to extract year value from the FX file before
    # processing the rest of the data in a different read.
    static_year_in_data_file = None

    @classmethod
    def update_year_in_data_file(cls, value):
        cls.static_year_in_data_file = value

    def __init__(self, config):
        self.config = config

    def extract_year_value_and_set_it_to_static_variable(self, df):
        """
        Note to my teammates: This is a **hack** and should not be
        relied on to pass information (esp. variables that hold a
        lot of data) between different configs in the same config
        file.
        """
        WvmFxRatesTransformFunctions.update_year_in_data_file([c for c in df.columns if type(c) == int][0])
        return df

    def select_COUNTRY_and_YEARLY_AVG_RATE_columns(
            self,
            df
    ):
        """
        We select 'COUNTRY' name column and Yearly average
        FX rate column, which usually tends to be the
        last column in the file.
        """
        # Sometimes for files like 2015 FX rates, it's better
        # to filter with startswith('AVG')
        yearly_avg_col = [col_name for col_name in df.columns
                          if str(col_name).startswith('AVG')][-1]

        # Sometimes, the average column is the last one WITHOUT 'AVG' keyword...
        # yearly_avg_col = [col_name for col_name in df.columns.tolist()][-1]
        return df[[RAW_COUNTRY_COLUMN_FX_RATES_AND_CONSTANT_DOLLAR_DATA, yearly_avg_col]]

    def select_COUNTRY_and_YEARLY_AVG_RATE_columns_with_yearly_avg_col_name_as_input(
            self,
            df,
            yearly_avg_col_name
    ):
        """
        Unfortunately, the client does NOT keep the FX rate file
        in consistent format. So we need to pick the monthly avg.
        FX rates from different columns in some months.

        This method allows us to choose the rate from a column name
        provided as an input parameter.
        """
        return df[[RAW_COUNTRY_COLUMN_FX_RATES_AND_CONSTANT_DOLLAR_DATA, yearly_avg_col_name]]

    def assert_the_first_column_is_COUNTRY_column(self,
                                                  df):
        """
        We must make sure the first column in
        the loaded dataframe is 'COUNTRY' colum.
        Otherwise, some of the ensuing the transform
        functions rely on 'COUNTRY' column being the
        first one.
        """
        if RAW_COUNTRY_COLUMN_FX_RATES_AND_CONSTANT_DOLLAR_DATA != df.columns.tolist()[0]:
            raise UnexpectedColumnNameFoundError(
                f"The first column in the dataframe is not 'COUNTRY'. "
                f"The other transform functions rely on the first column "
                f"being '{RAW_COUNTRY_COLUMN_FX_RATES_AND_CONSTANT_DOLLAR_DATA}'. "
                f"Please fix this in the raw data file and rerun the code."
            )

        return df

    def copy_country_names_to_row_below(self,
                                        df,
                                        list_of_col_names):
        """
        We need to copy country names to the rows below
        because we need the FX rates in the second row.
        """
        return self.copy_value_from_row_above_to_empty_rows_below(df, list_of_col_names)

    def select_every_third_row(
            self,
            df
    ):
        """
        We will only extract the local currency to USD FX rate factor.
        For that, we only need to keep every third row (starting from
        the first row).
        REF: https://stackoverflow.com/a/55684977/1330974
        """
        return df.iloc[1::3].reset_index(drop=True)

    def rename_yearly_avg_rate_column(
            self,
            df
    ):
        """
        Rename the name of the original column which stores
        average FX rates of the year to the value of the year
        found in the file.
        """
        if not WvmFxRatesTransformFunctions.static_year_in_data_file:
            raise InvalidValueFoundError(
                f"Seems like extracting year information from the "
                f"first few lines of the FX rate data file did not "
                f"return anything. Please inspect the static method "
                f"that extracts year information in this transform "
                f"function file."
            )
        # ASSUMPTION: we assume that the first column is 'COUNTRY'
        old_to_new_name_dict = {
            df.columns[-1]: WvmFxRatesTransformFunctions.static_year_in_data_file
        }

        return self.rename_columns(df, old_to_new_name_dict)

    def add_HARMONIZE_COUNTRY_column_using_existing_country_column(
            self,
            df,
            existing_country_col_name=RAW_COUNTRY_COLUMN_FX_RATES_AND_CONSTANT_DOLLAR_DATA,
            harmonized_country_col_name=HARMONIZED_COUNTRY_COLUMN_FX_RATES_AND_CONSTANT_DOLLAR_DATA
    ):
        """
        Update raw country names with standard country names
        we use in our WorldView Media (WVM) dashboard project
        (as listed in constants.wvm_dashboard_constants).

        If there is no entry in the mapping dictionary,
        we will copy the original country's name.
        """
        df = self.add_new_column_with_values_based_on_another_column_values_using_exact_str_match(
            df,
            existing_country_col_name,
            harmonized_country_col_name,
            FX_COUNTRY_NAME_TO_HARMONIZED_COUNTRY_NAME_MAPPINGS,
            True
        )
        return df.reset_index(drop=True)

    def assert_HARMONIZED_COUNTRY_column_includes_all_expected_countries_in_mapping_table(
            self,
            df,
            harmonized_country_col_name=HARMONIZED_COUNTRY_COLUMN_FX_RATES_AND_CONSTANT_DOLLAR_DATA
    ):
        """
        Make sure that we know if CP changes country names in
        FX rate files by raising error when we find that
        not all HARMONIZED country names in mapping dictionary
        show up in the resulting dataframe after mapping process.
        """
        expected_harmonized_country_names = set(FX_COUNTRY_NAME_TO_HARMONIZED_COUNTRY_NAME_MAPPINGS.values())
        actual_harmonized_country_names = set(df[harmonized_country_col_name].unique())

        if bool(expected_harmonized_country_names - actual_harmonized_country_names):
            raise UnexpectedColumnValuesFoundError(
                f"We found that these expected countries are missing from "
                f"'{harmonized_country_col_name} column: '"
                f"{expected_harmonized_country_names - actual_harmonized_country_names}. "
                f"Make sure all expected countries show up in '{harmonized_country_col_name}' "
                f"column or update the country mapping in constants.wvm_dashboard_constants file."
            )

        return df

    def remove_existing_rows_for_countries_that_use_USD_and_EURO(
            self,
            df
    ):
        """
        Unfortunately, the raw data already has rows for countries
        that uses EURO and USD such as BAHRAIN, KUWAIT, OMAN, ...,
        SLOVAKIA. Therefore, we need to remove these rows before
        adding rows with constant values for USD and EURO-using
        countries.
        """
        countries_to_drop = {c.upper() for c in COUNTRIES_THAT_USE_USD}.union(
            {c.upper() for c in COUNTRIES_THAT_USE_EURO})

        return self.drop_rows_with_matching_string_values(
            df,
            [HARMONIZED_COUNTRY_COLUMN_FX_RATES_AND_CONSTANT_DOLLAR_DATA],
            [countries_to_drop])

    def add_yearly_rows_for_countries_that_use_USD(
            self,
            df
    ):
        """
        GCC, Puerto Rico, USA use USD as currency in the data we receive.
        We will populate rows for these countries with 1.0 as FX rates.
        """
        for country in COUNTRIES_THAT_USE_USD:
            df1 = pd.DataFrame(columns=df.columns)
            df1.loc[0] = [country,
                          USD_FX_Rate,
                          country]
            df = pd.concat([df, df1])

        return df.reset_index(drop=True)

    def add_yearly_rows_for_countries_that_use_EURO(
            self,
            df
    ):
        """
        Some EU countries use Euro as currency in the data we receive.
        We will populate rows for these countries by using Euro to USD FX rates.
        """

        for country in COUNTRIES_THAT_USE_EURO:
            # REF: https://stackoverflow.com/a/53954986
            df1 = df[df[HARMONIZED_COUNTRY_COLUMN_FX_RATES_AND_CONSTANT_DOLLAR_DATA] == EURO_CURRENCY_NAME].copy(deep=True)
            df1.loc[df1[HARMONIZED_COUNTRY_COLUMN_FX_RATES_AND_CONSTANT_DOLLAR_DATA] == EURO_CURRENCY_NAME, HARMONIZED_COUNTRY_COLUMN_FX_RATES_AND_CONSTANT_DOLLAR_DATA] = country
            df = pd.concat([df, df1])

        return df.reset_index(drop=True)

    def check_HARMONIZED_COUNTRY_column_against_country_names_from_comp_harm_project(
            self,
            df,
            harmonized_country_col_name=HARMONIZED_COUNTRY_COLUMN_FX_RATES_AND_CONSTANT_DOLLAR_DATA
    ):
        """
        Check harmonized country column to see if we are missing
        any country name from the list of countries we process
        for the competitive harmonization project.
        """
        actual_harmonized_country_names = set(df[harmonized_country_col_name].unique())

        if bool(COMP_HARM_PROJECT_COUNTRIES - actual_harmonized_country_names):
            self.logger.warning(
                f"We found that these countries in competitive harmonization "
                f"project are missing from '{harmonized_country_col_name} column: '"
                f"{COMP_HARM_PROJECT_COUNTRIES - actual_harmonized_country_names}. "
                f"Make sure all expected countries show up in '{harmonized_country_col_name}' "
                f"column or update the country mapping in constants.wvm_dashboard_constants file."
            )

        return df

    def rearrange_columns_for_final_output_of_yearly_avg_fx_rate_file(
            self,
            df):
        """
        Rearrange the order of columns (just for aesthetic sake)
        so that country and harmonized country columns appear
        next to each other in the final output.
        """
        return self.update_order_of_columns_in_dataframe(
            df,
            [
                RAW_COUNTRY_COLUMN_FX_RATES_AND_CONSTANT_DOLLAR_DATA,
                HARMONIZED_COUNTRY_COLUMN_FX_RATES_AND_CONSTANT_DOLLAR_DATA,
                WvmFxRatesTransformFunctions.static_year_in_data_file,
            ]
        )

    # =======================================================
    # Methods below are for combining yearly avg FX rates
    # into one file (step 2).
    # =======================================================
    def rearrange_columns_for_final_output_of_combined_yearly_avg_fx_rate_file(
            self,
            df):
        output_cols = [col for col in df.columns if col != RAW_COUNTRY_COLUMN_FX_RATES_AND_CONSTANT_DOLLAR_DATA]

        return self.update_order_of_columns_in_dataframe(
            df,
            output_cols
        )

    def convert_column_names_to_string_type(self, df):
        df.columns = df.columns.map(str)
        return df

    def assert_no_comp_harm_country_has_NaN_data_point_in_any_of_the_years(
            self,
            df
    ):
        for year_col in df.columns[~df.columns.isin([RAW_COUNTRY_COLUMN_FX_RATES_AND_CONSTANT_DOLLAR_DATA,
                                                     HARMONIZED_COUNTRY_COLUMN_FX_RATES_AND_CONSTANT_DOLLAR_DATA])]:
            cur_df = df[df[year_col].isna()]
            set_intersection = COMP_HARM_PROJECT_COUNTRIES.intersection(
                set(cur_df[HARMONIZED_COUNTRY_COLUMN_FX_RATES_AND_CONSTANT_DOLLAR_DATA].unique()))
            if bool(set_intersection):
                raise NullValueFoundError(
                    f"For year '{year_col}', the FX rate data is missing for the following "
                    f"countries: '{set_intersection}'. Missing FX data for countries in "
                    f"competitive harmonization project is NOT good."
                    f"Make sure to inspect the corresponding input file to fix this."
                )

        return df

    # =======================================================
    # Step 3: Methods below are for calculating constant dollar
    # ratios from the yearly avg. FX rates (combined) file.
    # =======================================================
    def calculate_and_add_constant_dollar_ratio_columns_using_previous_year_as_base(
            self,
            df
    ):
        """
        We will use previous year's rates as base in calculating constant dollar
        values because we generally have full year's worth of FX rates for previous
        year. The formula for constant dollar value is like this:
        constant_dollar_ratio_for_year_x = fx_rate_of_base_year/fx_rate_of_year_x
        """
        previous_year = str(datetime.datetime.now().year - 1)
        year_columns = [c for c in df.columns if c not in [RAW_COUNTRY_COLUMN_FX_RATES_AND_CONSTANT_DOLLAR_DATA, HARMONIZED_COUNTRY_COLUMN_FX_RATES_AND_CONSTANT_DOLLAR_DATA]]
        constant_dollar_ratio_df = pd.DataFrame(columns = df.columns)

        # Copy harmonized country column from FX rates dataframe to the new one
        constant_dollar_ratio_df[HARMONIZED_COUNTRY_COLUMN_FX_RATES_AND_CONSTANT_DOLLAR_DATA] = df[HARMONIZED_COUNTRY_COLUMN_FX_RATES_AND_CONSTANT_DOLLAR_DATA]

        for y in year_columns:
            constant_dollar_ratio_df[y] = df[previous_year]/df[y]

        return constant_dollar_ratio_df

    def set_constant_dollar_ratio_of_current_year_to_one(
            self,
            df
    ):
        """
        Since we don't have full year's worth of FX rate data, we will
        set the current year's constant dollar ratio to 1.
        """
        current_year = str(datetime.datetime.now().year)
        df[current_year] = 1.0

        return df

    # =======================================================
    # Methods below are for calculating constant dollar values.
    # =======================================================
    def append_data_from_files(
            self,
            df,
            list_of_file_path_and_names
    ):
        """
        Append data from the other transformed FX rate files
        into the base dataframe. We will make sure that there
        is no duplicate year in the final, combined data
        in the later step.
        """
        # Label to indicate that this column is found in
        # both dataframes. We will use that to drop one
        # of them toward the end of the process
        conflict_column_label = '_common_column'

        for f in list_of_file_path_and_names:
            cur_df = pd.read_excel(f)
            cur_df.columns = cur_df.columns.map(str)
            # We can use pandas' join method, but that requires
            # us to set 'country' as index, and the output is not
            # as close to what we expect. Pandas' merge gives
            # a closer output that we want. For more, please read
            # REF: https://stackoverflow.com/a/22676213/1330974
            df = df.merge(cur_df,
                          how='outer',
                          on=HARMONIZED_COUNTRY_COLUMN_FX_RATES_AND_CONSTANT_DOLLAR_DATA,
                          suffixes=('', conflict_column_label))
            # Drop the columns that are common between
            # the two dataframes being merged, and only
            # keep one of them.
            # REF1: https://stackoverflow.com/a/54410702/1330974
            # REF2: https://stackoverflow.com/a/54410702/1330974
            df = df.loc[:, ~df.columns.str.contains(
                f".*?{conflict_column_label}$",
                case=False,
                na=False  # Year columns returns NaN; convert them to bool array
            )]
        return df

    # =======================================================
    # Methods below are for extracting monthly FX rates.
    # We decided to use yearly average FX rates to simplify
    # the constant dollar calculation and keep the amount of
    # data manageable.
    # =======================================================
    def unpivot_fx_data(self,
                        df):
        # REF: https://stackoverflow.com/a/18259236/1330974
        # First, set the index to COUNTRY column then unstack
        df1 = df.set_index(RAW_COUNTRY_COLUMN_FX_RATES_AND_CONSTANT_DOLLAR_DATA)
        df2 = df1.unstack().reset_index(name=FX_RATES_COLUMN)

        return self.rename_columns(df2, {'level_0': YEAR_COLUMN_FX_RATES_AND_CONSTANT_DOLLAR_DATA})

    def select_COUNTRY_and_MONTHLY_RATE_columns(
            self,
            df
    ):
        """
        We only need Actual and Estimated FX rate columns
        in addition to 'COUNTRY' name column.
        """
        desired_cols = [RAW_COUNTRY_COLUMN_FX_RATES_AND_CONSTANT_DOLLAR_DATA] \
                       + [col_name for col_name in df.columns.tolist()
                          if (str(col_name).startswith('ACT')
                              or str(col_name).startswith('EST'))]
        return df[desired_cols]

    def assert_FX_columns_for_all_months_exist(self,
                                               df):
        """ Check if there are 12 columns with FX rates """
        # First, join column names with '|' in a single string.
        col_names = '|'.join(df.columns.tolist()[1:])

        # Second, find either 'ACT' or 'EST' because these
        # represents columns FX rates for each month
        result = re.findall(r'(ACT)|(EST)', col_names)
        expected_col_count = 12
        if len(result) != expected_col_count:
            raise InsufficientNumberOfColumnsError(
                f"Expected FX rate column count of: "
                f"{expected_col_count} but found: "
                f"{len(result)} in the current dataframe."
            )

        return df

    def rename_columns_with_year_and_month_name_for_each(
            self,
            df,
            year
    ):
        """
        Given a year provided as parameter to this method
        and **assuming that the existing columns are already
        in the right order (from January to December)**,
        rename the existing column names with new column
        names having YYYY-MM-DD format.
        """
        cur_year = datetime.datetime.now().year
        if cur_year != year:
            raise InvalidValueFoundError(
                f"The year provided, {year}, is not the same as "
                f"the current year. Please comment out this "
                f"line in python code if you want to proceed "
                f"with the rest of the step even when the year "
                f"that you are using is different than the current "
                f"year (e.g., you are processing data from previous "
                f"years)."
            )

        # ASSUMPTION: we assume that the first column is 'COUNTRY'
        month_cols = df.columns.tolist()[1:]
        yyyy_mm_dd = generate_one_yyyy_mm_dd_string_for_each_month_of_the_year(year)
        old_to_new_name_dict = dict(zip(month_cols, yyyy_mm_dd))

        return self.rename_columns(df, old_to_new_name_dict)

    def add_monthly_rows_for_countries_that_use_USD(
            self,
            df
    ):
        """
        GCC, Puerto Rico, USA use USD as currency in the data we receive.
        We will populate rows for these countries with 1.0 as FX rates.
        """
        cur_year = datetime.datetime.now().year
        yyyy_mm_dd = generate_one_yyyy_mm_dd_string_for_each_month_of_the_year(cur_year)

        for country in COUNTRIES_THAT_USE_USD:
            df1 = pd.DataFrame(columns=df.columns)
            for i, d in enumerate(yyyy_mm_dd):
                df1.loc[i] = [d, country, USD_FX_Rate, country]
            df = pd.concat([df, df1])

        return df.reset_index(drop=True)