'''
This program is used for extracting user speficic cryptocurrency data from Coinmarketcap
and putting it into a useable pandas dataframe structure.
'''

import pandas as pd

def create_coin_df(df, coin_name):
    '''
        This function takes in a dataframe (pandas DataFrame) and a coin_name (string)
        and returns a new dataframe (pandas DataFrame) with all trades dates as index,
        the column for name of coin, and the following price data columns, Open, High, Low,
        Close.  It will also print out the first 10 rows of the dataframe to check
    '''
    # Create a dataframe of only specific coin and columns of interest
    df_coin = df[df.Currency == coin_name]
    df_coin = df_coin[['Currency', 'Date', 'Open','High', 'Low', 'Close']]

    # Set Date to a datetime object and use as index
    df_coin.Date = pd.to_datetime(df_coin.Date)
    df_coin = df_coin.set_index('Date')

    # Cast price data columns to floats
    df_coin.Open = df_coin.Open.apply(pd.to_numeric)
    df_coin.High = df_coin.High.apply(pd.to_numeric)
    df_coin.Low = df_coin.Low.apply(pd.to_numeric)
    df_coin.Close = df_coin.Close.apply(pd.to_numeric)

    # Sort data in ascending order
    df_coin.sort_index(axis=0, ascending=True, inplace=True)

    return df_coin

# Read in all data from the Coinmarketcap file, get name of coin from user
df = pd.read_csv('consolidated_coin_data.csv', skiprows=4, low_memory=False)
coin_name = input('What cryptocurrency do you want data for?\n')

df_coin = create_coin_df(df, coin_name)

print('These are the first 10 rows of the new {} dataframe.'.format(coin_name))
print(df_coin.head(10))
