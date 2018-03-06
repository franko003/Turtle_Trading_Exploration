#!/usr/bin/env python
# # -*- coding: utf-8 -*-

""" This module is meant to be used to explore a simplified version of the
    famous Turtle trading strategy.  Using cryptocurrency financial data from a csv
    file aggregated at Kaggle.com and given the name of a coin, time period of interest,
    and direction of strategy, these functions will create a relevant dataframe and
    price range, then find valid entry points, and finally return a list of price
    changes on all valid entry points selected.  This list can then be used for analysis
    to determine if the strategy shows promise to create positive expectancy.
"""

from util import *
import pandas as pd

def main():
    # Read in all data from the Coinmarketcap file
    df = pd.read_csv('consolidated_coin_data.csv', skiprows=4, low_memory=False)

    # Get user input for coin name, create new dataframe and check
    coin_name = input('What cryptocurrency do you want data for? (lowercase)\n')

    df_coin = create_coin_df(df, coin_name)

    print('These are the first 10 rows of the new {} dataframe.'.format(coin_name))
    print(df_coin.head(10))

    # Get user input for period, create new columns and check
    period = int(input('How many days do you want to include in your break-out range?\n'))

    create_range_column(df_coin, period)

    print('Added new columns to the dataframe')
    print(df_coin.tail())

    # Get user input for direction of trades, generate tradelist, print trades and ave
    direction = input('What trade direction do you want to include?\nLong/Short/Both\n')

    price_diff_list = generate_tradelist(df_coin, period, direction)
    trade_count = len(price_diff_list)
    ave_price_diff = price_diff_list.mean()

    print('Total number of trades: {}'.format(trade_count))
    print('Average price change per trade: {}'.format(ave_price_diff))


if __name__ == '__main__':
    main()
