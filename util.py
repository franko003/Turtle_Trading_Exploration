#!/usr/bin/env python
# # -*- coding: utf-8 -*-

""" This module is a group of functions that assist in doing break out trading strategy
    testing for different cryptocurrencies, over specific ranges and trade directions.
"""

import pandas as pd
import numpy as np
from pandas.tseries.offsets import *

def create_coin_df(df, coin_name):
    ''' This function takes in a dataframe (pandas DataFrame) and a coin_name (string)
        and returns a new dataframe (pandas DataFrame) with Date as index,
        the column for name of coin, and the following price data columns, Open, High, Low,
        Close.
    '''
    # Print message if coin does not exist in csv file
    if ~df.Currency.str.contains(coin_name).any():
        print('Coin does not exist in database.  Will return empty dataframe.')

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

def create_range_column(df, period):
    ''' This function takes in a dataframe of price data and a integer for the length
        of the period desired for the range.  It then creates two new columns, one
        for the High desired period and one for the Low.  No return, changes input df.
    '''
    # Create new columns
    try:
        df['Range_High'] = df['High'].rolling(window=period).max().shift(1)
        df['Range_Low'] = df['Low'].rolling(window=period).min().shift(1)

    except ValueError:
        print('Period must be an integer value')

def generate_tradelist(df, period, direction='Both'):
    ''' Inputs are dataframe, period and flag for Long/Short/Both directions, function
        returns a list of price changes for all valid trades in the df given the parameters.
    '''
    # Create new df of potential trades, allowing for period number of days forward data
    df_trades = df[:-(period)]

    # Get a series of entry prices
    entry_prices_long = df_trades[df_trades.High > df_trades.Range_High].High + 1
    entry_prices_short = df_trades[df_trades.Low < df_trades.Range_Low].Low - 1

    # Create a series of exit prices based off closing price period days later
    exit_dates_long = entry_prices_long.index + DateOffset(days=period)
    exit_dates_short = entry_prices_short.index + DateOffset(days=period)

    exit_prices_long = []
    exit_prices_short = []

    for i in range(len(exit_dates_long)):
        exit_prices_long.append(df.loc[exit_dates_long[i]].Close)
    for j in range(len(exit_dates_short)):
        exit_prices_short.append(df.loc[exit_dates_short[j]].Close)

    # Generate the final list of price differences
    exit_prices_long_arr = np.array(exit_prices_long)
    exit_prices_short_arr = np.array(exit_prices_short)

    price_diffs_long = exit_prices_long_arr - entry_prices_long
    price_diffs_short = entry_prices_short - exit_prices_short_arr

    # Create list dependant on direction param
    if direction == 'Long':
        price_diffs_final = price_diffs_long
    elif direction == 'Short':
        price_diffs_final = price_diffs_short
    else:
        price_diffs_final = price_diffs_long.append(price_diffs_short)

    return price_diffs_final
