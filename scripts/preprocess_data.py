import pandas as pd
from df_transform import rename_columns, encode_answers

def preprocess_survey_data(filepath: str):

    df = pd.read_csv(filepath)

    #Drop the index column and timestamp from the Google Form 
    df.drop(df.columns[:2], axis=1, inplace=True)
    
    #Rename columns to "Question 1"...
    renamed_df, column_map = rename_columns(df)

    #Remove the first row 
    renamed_df = renamed_df.drop(0).reset_index(drop=True)

    renamed_df["Question 1"] = renamed_df["Question 1"].astype(int)

    encoding_map = encode_answers(renamed_df)

    return renamed_df, column_map, encoding_map
