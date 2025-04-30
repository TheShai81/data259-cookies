'''Contains methods to take in the very wordy Google Forms results and turn
column names into question numbers, ordinally encodes some fields, and creates
a mapping of question numbers to each column name/answer choices for ease of use.
'''

import pandas as pd

# questions who are going to be ordinally encoded for easier analysis
long_cols = ["Question 4", "Question 5", "Question 6", "Question 7", "Question 8",
             "Question 9", "Question 10", "Question 11", "Question 19", "Question 20",
             "Question 21", "Question 22"]

def rename_columns(df: pd.DataFrame) -> tuple:
    '''
    Renames the columns of a dataframe and returns a new dataframe with these
    column names. Also returns the mapping of new column names to old ones.

    Args:
        df (pd.DataFrame): the dataframe whose columns are to be renamed

    Returns:
        tuple: a new dataframe with the new column names and a dictionary mapping
        of new to old column names
    '''

    # drop timestamp column if it's in there
    if "Timestamp" in df.columns:
        df = df.drop("Timestamp", axis=1)
    
    new_df: pd.DataFrame = df.rename(["Question " + str(i+1) for i in range(len(df.columns))], axis=1)
    column_map = {new: old for new, old in zip(new_df.columns, df.columns)}

    return new_df, column_map


def encode_answers(df: pd.DataFrame, columns: list = long_cols) -> dict[str: dict]:
    '''
    Ordinally encodes the columns provided in the provided list. Replaces original columns in the df.
    
    Args:
        df (pd.DataFrame): The dataframe containing survey responses.
        columns (list): A list of column names (e.g., "Question 1", "Question 2") to encode.
        Defaults to long_cols (internally compiled list).

    Returns:
        dict: A mapping from each question name to a dictionary of ordinal encoding
              {ordinal_value: original_answer}
    '''
    encoding_map = {}

    for col in columns:
        unique_answers = df[col].dropna().unique()
        unique_answers_sorted = sorted(unique_answers)  # sort for consistent encoding
        answer_to_int = {ans: i for i, ans in enumerate(unique_answers_sorted)}
        int_to_answer = {i: ans for ans, i in answer_to_int.items()}

        df[col] = df[col].map(answer_to_int)
        encoding_map[col] = int_to_answer

    return encoding_map