import pandas as pd
URL ='https://data.seattle.gov/api/views/2khk-5ukd/rows.csv?accessType=DOWNLOAD'

#read data
def read_data(url):
    return pd.read_csv(url)

#check three requirements
def test_create_dataframe(df, colName):
    isValid = True #initialize return
    if list(df.columns) != colName: #check columns
        isValid = False
    if len(df) < 10: #check number of rows
        isValid = False
    for i in df.columns: #check value data type
        for j in range(len(df)):
            if type(df[i][j]) != type(df[i][0]):
                isValid = False;
                break
    return isValid
