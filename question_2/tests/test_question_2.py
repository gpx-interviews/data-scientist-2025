import os
import sys
import pytest
import pandas as pd
import numpy as np


sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from answer_q2 import produce_csv

'''
helpers
'''
@pytest.fixture(scope="session", autouse=True)
def make_student_answer():
    file = os.path.join(os.path.dirname(__file__), '..', 'hourly_carbon_intensity_july_2025.csv')
    # make the file only once per pytest run
    produce_csv(output_filepath=file)

    
def get_correct_answer():
    ans_file = os.path.join(os.path.dirname(__file__), 'data', 'hourly_carbon_intensity_july_2025.parquet')
    ans_df = pd.read_parquet(ans_file)
    return ans_df


def get_student_answer():
    file = os.path.join(os.path.dirname(__file__), '..', 'hourly_carbon_intensity_july_2025.csv')

    if not os.path.exists(file):
        return None
    
    # Get actual columns
    with open(file) as f:
        header = f.readline().strip().split(",")

    # Filter only present columns for dtype
    desired_dtypes = {"year": str, "month": str, "day": str, "hour": str, "tonnes_co2e_per_kwh": float}
    safe_dtypes = {k: v for k, v in desired_dtypes.items() if k in header}

    ans_df = pd.read_csv(file, dtype=safe_dtypes)
    return ans_df


'''
tests
'''
def test_csv_written():
    ans = get_student_answer()
    assert ans is not None


def are_columns_correct(ans_df, correct_df):
    if ans_df is None:
        return False
    return ans_df.columns.tolist() == correct_df.columns.tolist()

def test_columns_correct():
    ans = get_student_answer()
    correct_df = get_correct_answer()
    assert are_columns_correct(ans, correct_df)


def columns_exact(ans_df, correct_df, column):
    if ans_df is None:
        return False
    if column not in ans_df.columns:
        return False
    ans_col = ans_df[column].to_list()
    correct_col = correct_df[column].to_list()
    if len(ans_col) != len(correct_col):
        return False
    return ans_col == correct_col


def test_hours_correct():
    ans = get_student_answer()
    correct_df = get_correct_answer()
    assert columns_exact(ans, correct_df, "hour")

def test_month_correct():
    ans = get_student_answer()
    correct_df = get_correct_answer()
    assert columns_exact(ans, correct_df, "hour")

def test_year_correct():
    ans = get_student_answer()
    correct_df = get_correct_answer()
    assert columns_exact(ans, correct_df, "year")


def float_columns_close(ans_df, correct_df, column, rtol=1e-05):
    if ans_df is None:
        return False
    if column not in ans_df.columns:
        return False
    ans_col = ans_df[column].to_list()
    correct_col = correct_df[column].to_list()
    if len(ans_col) != len(correct_col):
        return False
    
    ans_array = np.array(ans_col, dtype=np.float64)
    correct_array = np.array(correct_col, dtype=np.float64)

    return np.allclose(ans_array, correct_array, rtol=rtol)

def test_tonnes_co2e_per_kwh_correct():
    ans = get_student_answer()
    correct_df = get_correct_answer()
    assert float_columns_close(ans, correct_df, "tonnes_co2e_per_kwh", rtol=1e-05)

