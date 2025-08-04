import os
import sys
import pandas as pd

sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from answer_q1 import normalise_dict_scores_01


def is_q1_correct():
    """Test if the answer DataFrame is correct."""
    # get the input as dict
    input_file = os.path.join(os.path.dirname(__file__), 'data', 'input_df.parquet')
    input_df = pd.read_parquet(input_file)
    input_dict = input_df['score'].to_dict()

    # get the outpput answer
    output_dict = normalise_dict_scores_01(input_dict)

    # get the output 
    output_file = os.path.join(os.path.dirname(__file__), 'data', 'output_df.parquet')
    output_df = pd.read_parquet(output_file)
    output_correct = output_df['normalised_score'].to_dict()

    correct = output_dict == output_correct
    return correct


def test_answer_q1():
    assert is_q1_correct()