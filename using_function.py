import pandas as pd
URL ='https://data.seattle.gov/api/views/2khk-5ukd/rows.csv?accessType=DOWNLOAD'
df = pd.read_csv(URL)

#Read dataframe columns
df_col = sorted(df.columns)

#Read dataframe columns data type
df_col_type = list(df[df_col].dtypes)

def test_create_dataframe(df):
    df_col_test = sorted(df.columns)
    df_col_type_test = list(df[df_col_test].dtypes)
    
    #count row
    row = df.shape[0]
    
    #check if match the requirements
    if (df_col_test == df_col and df_col_type_test == df_col_type and row >= 10):
        return True
    else:
        return False


#Should return True
test_create_dataframe(df)

#Test add new column into dataframe to see if match the requirements
address = None  
df['Address'] = address

#Should return False
test_create_dataframe(df)
