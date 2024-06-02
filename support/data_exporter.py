"""
Used to write data to xlsx-files.
"""

import pandas as pd
import os

BASE_DIR = "./_results"


def write_scalabrino(data, time_stamp: str = "no-time-stamp") -> None:
    _create_directory_if_not_exists(BASE_DIR)

    file_name = f'{BASE_DIR}/{time_stamp}_scalabrino_results.xlsx'

    try:
        existing_data = pd.read_excel(file_name)
    except FileNotFoundError:
        existing_data = pd.DataFrame()

    new_data = pd.DataFrame(data)
    combined_data = pd.concat([existing_data, new_data], ignore_index=True)

    combined_data.to_excel(file_name, index=False)
    print('Scalabrino results has been successfully written to the Excel file.')


def write_complexity(data, class_name: str, time_stamp: str = "no-time-stamp") -> None:
    _create_directory_if_not_exists(BASE_DIR)

    file_name = f'{BASE_DIR}/{time_stamp}_complexity_results.xlsx'

    try:
        existing_data = pd.read_excel(file_name)
    except FileNotFoundError:
        existing_data = pd.DataFrame()

    class_name_df = pd.DataFrame({'Class_name': [class_name]})
    new_data = pd.DataFrame(data)
    new_data_with_class_name = pd.concat([class_name_df, new_data], axis=1)  # Concatenate classname with new data

    combined_data = pd.concat([existing_data, new_data_with_class_name], ignore_index=True)
    combined_data.to_excel(file_name, index=False)
    print('Complexity results has been successfully written to the Excel file.')


def _create_directory_if_not_exists(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)