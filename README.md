# Bitcoin Turtle Trading Strategy Exploration

This project is an exploration of a very simplified version of the famous "Turtle"
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
