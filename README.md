# Bitcoin Turtle Trading Strategy Exploration

This project is an exploration of a very simplified version of the famous [Turtle](http://www.turtletrader.com/)
trading strategy done on the Bitcoin price data.  The strategy consists of looking
at the past 4 weeks of price data and calculating the total range.  If price exceeds
the high of the range at any point on a given day a hypothetical long trade is
entered from a price level just above the range high.  We then calculate the difference
in this entry price and the closing price of Bitcoin 4 weeks later.  The analysis
is then done on these differences to determine if breaking out above a 4 week high
price leads to higher prices 4 weeks later.

## The Data

The dataset is cryptocurrency daily price data from [Coinmarketcap.com](https://coinmarketcap.com/), aggregated at [Kaggle.com](https://www.kaggle.com/)

https://www.kaggle.com/philmohun/cryptocurrency-financial-data

## Shortcomings and Topics for Further Exploration

1. Does not take into account stops
2. Look at short trades as well
3. Better plotting of price information (OHLC bar or candlestick charts)
4. Different time frames to determine success or failure (not just 28 days)
5. Need to apply trading rules so that you don't take too many trades in a row
6. Trade sizing to calculate real pnl, wouldn't be just the price change
7. In testing could have done a large number of random samples and saw how none of
them could accept the null hypothesis

## References

  * https://stats.stackexchange.com/questions/169383/method-for-a-hypothesis-testing-non-normal-distribution-number-of-retweets
  * https://stats.stackexchange.com/questions/235243/when-should-i-use-scipy-stats-wilcoxon-instead-of-scipy-stats-ranksums
  * https://pandas.pydata.org/pandas-docs/stable/
  * https://docs.scipy.org/doc/
