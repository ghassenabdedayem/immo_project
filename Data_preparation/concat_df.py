import pandas as pd
from Data_processing import data_process as dp

def concatenate (df_list_path):
    df = pd.DataFrame()
    for df_element_path in df_list_path:
        unit_df = dp.read_clean_process(df_element_path)
        # print(df_element_path[-10:] ,' : ', len(unit_df)) # Print control
        df = pd.concat([df, unit_df], ignore_index=True)
        # print('cumulé ', df_element_path[-8:] ,' : ', len(df))
    return df