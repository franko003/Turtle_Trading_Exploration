import pandas as pd

def create_range_column(df, period):
    '''
        This function takes in a dataframe of price data and a integer for the length
        of the period desired for the range.  It then creates two new columns, one
        for the High desired period and one for the Low.  It returns the new dataframe.
    '''

    # Create variables for new column names
    column_name_High = 'High_{}_day'.format(period)
    column_name_Low = 'Low_{}_day'.format(period)

    # Create new columns
    df[column_name_High] = df['High'].rolling(window=period).max().shift(1)
    df[column_name_Low] = df['Low'].rolling(window=period).min().shift(1)

    return df
