import get_Data as getdat
import pandas as pd
from datetime import date, timedelta
import get_and_set_env

language = get_and_set_env.returnLanguageKey()

# Function to create a DataFrame
def createDataFrame(dataframe):
    df = pd.DataFrame(dataframe)
    return df

# Function to split on multiple patterns (ellipsis '...', Unicode '…', or other patterns like '\r\n')
def custom_split(text):
    return text.replace('\r\n', ' ').replace('…', '...').split('...')[0]

def cleanData():
    # Call the API to get the data
    df = getdat.call_Api()
    # Create a DataFrame from the 'articles' key in the data
    df = createDataFrame(df['articles'])

    if df is None or df.empty:
        return None
    # data = getdat.mergeData()

    print(df.info())

    # Print the count of missing values in each column
    print(df.isna().sum())

    # Drop rows with any missing values
    df = df.dropna()

    # Print the count of missing values in each column
    print(df.isna().sum())

    # Change data type to object to date
    df['publishedAt'] = pd.to_datetime(df['publishedAt'])

    df['description'] = df['description'].str.lower()
    # print(df['description'])

    #
    df['content'] = df['content'].apply(custom_split)

    print(df.info())

    return df

def changeDate(df, date_columns):
    for column in date_columns:
        df[column] = pd.to_datetime(df[column], errors='coerce')
        print(df[column])
    return df

def test(df, listVariables, name):
    columns = df.columns.tolist()
    # print('columns', columns)
    test2 = [col in listVariables for col in columns]
    # print('test2')
    print(test2)
    if not any(test2) and name not in columns:
        # print('entre aqui')
        df[name] = 'unknown'
        return df
    if all(not val for val in test2):
        return df
    else:
        item = [i for i, x in enumerate(test2) if x][0]
        # print(item)
        try:
            df = df.rename(columns={f'{columns[item]}': f'{name}'})
        except Exception:
            print(df)
        return df

def findDates(df):
    date_columns = []
    for column in df.columns:
        if df[column].dtype == 'object':  # Ensure the column is of object type before attempting to convert
            try:
                df[column] = pd.to_datetime(df[column])
                date_columns.append(column)
            except (ValueError, TypeError):
                continue
    # print(date_columns)
    if not date_columns:
        # print('entre aqui')
        df['publishedAt'] = date.today()
        df['publishedAt'] = pd.to_datetime(df['publishedAt'])
    else:
        print('date_columns:', date_columns)
    df = changeDate(df, date_columns)

    return date_columns, df

def findText(df):
    columns = df.columns.tolist()
    # print(columns)
    listVariables = ['text_pt', 'text', 'news']
    test2 = [col in listVariables for col in columns]
    # print('test2', test2)
    item = [i for i, x in enumerate(test2) if x][0]
    # print('item', item)
    try:
        # df = df.rename(columns={f'{listVariables[item]}': 'description'})
        df = df.rename(columns={f'{columns[item]}': 'description'})
    except Exception:
        print(df.columns)
    # print(df.info())
    return df


def  cleanDataCSV():
    # Call the CSV to get the data
    df = getdat.get_DataCSV()

    if df is None or df.empty:
        return None

    # lower case column names
    df.columns = df.columns.str.lower()

    print(df.info())

    list_dates_columns, df = findDates(df)
    print('list_dates_columns: ', list_dates_columns)

    listVariables = ['date', 'published at']
    name = 'publishedAt'
    df = test(df, listVariables, name)
    # print('df.columns')
    # print(df.columns)
    # print()

    listVariables = ['text_pt', 'text', 'news']
    name = 'description'
    df = test(df, listVariables, name)

    listVariables = ['writer']
    name = 'author'
    df = test(df, listVariables, name)

    # df = findText(df)
    df['description'] = df['description'].str.lower()
    # print(df.columns)

    # Drop rows with any missing values if there are any missing values
    if df.isna().sum().sum() > 0:
        df = df.dropna()
        # Print the count of missing values in each column
        print(df.isna().sum())

        # Change data type to object to date
        # df = df.rename(columns={'published at': 'publishedAt'})


            # df = df.rename(columns={f'{test2[item]}': 'description'})
        # df = df.rename(columns={'y': 'sentiment'})
        # print(test2, item)

    # df = df.drop(columns=['type'])

    # print(df.info())
    # #
    # print(df['description'].iloc[2])
    # # df['content'] = df['content'].apply(custom_split)


    # print(df.columns)
    # print(df.info())
    return df
