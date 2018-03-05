# Bitcoin Turtle Trading Strategy Exploration

This project is an exploration of a very simplified version of the famous [Turtle](http://www.turtletrader.com/)
trading strategy done on the Bitcoin price data.  The strategy consists of looking
at the past 4 weeks of price data and calculating the total range.  If price exceeds
the high of the range at any point on a given day a hypothetical long trade is
entered from a price level just above the range high.  We then calculate the difference
in this entry price and the closing price of Bitcoin 4 weeks later.  The analysis
is then done on these differences to determine if breaking out above a 4 week high
price leads to higher prices 4 weeks later.

## Data

The dataset is cryptocurrency daily price data from [Coinmarketcap.com](https://coinmarketcap.com/), aggregated at [Kaggle.com](https://www.kaggle.com/)

https://www.kaggle.com/philmohun/cryptocurrency-financial-data

## Contents

The repository consists of the csv data file, a Python file, and a Jupyter notebook.  

The Python file is the code portions of the analysis abstracted into functions, and
can be run separately from the command line to get information on any cryptocurrency
in the dataset, for any range period, for either/both trade directions. Simply run the
file and follow the prompts.  You can look in the csv file itself for the names of
the 200 cryptocurrencies available.

The notebook encompasses the entire project from initial question to topics to explore further,
focusing only on Bitcoin price data.  This is the most interesting part as it includes
some background, all the visualizations, and trading analysis.

##

## Improvements and Topics for Further Exploration

#### Trading

From a real trading perspective this analysis is not very relevant for a number of
reasons.  First of all, looking at where price is a month after a trade doesn't give
the full story.  Even if price is higher, it may have gone lower first and forced
you out of the position.  This analysis also doesn't take into account the short
side of the market, break-outs below the low range may be relevant as well.  

A better approach in the future would be to establish some trading rules such as risk
amount, profit targets, number of positions on a once, etc.  With a more realistic
approach you could then get a better idea if the strategy is worth actually trading.

After improving the analysis of Bitcoin the next step would then be to apply it to
other cryptocurrencies, stocks, commodities, etc.  A robust trading strategy would
show positive expectancy with many different underlying products.

#### Analysis

One main part of this analysis that could be improved immediately is better plotting
for this type of data.  Seeing an OHLC type chart for price action is much better
than a simple line chart.

Also, in the statistical analysis at the end there needs to be more random samples of
the hypothetical data taken.  Only one sample gives you a picture, but taking a
larger number of samples and showing that you can reject the null hypothesis with
all of them would be much more convincing.

## References

  * https://stats.stackexchange.com/questions/169383/method-for-a-hypothesis-testing-non-normal-distribution-number-of-retweets
  * https://stats.stackexchange.com/questions/235243/when-should-i-use-scipy-stats-wilcoxon-instead-of-scipy-stats-ranksums
  * https://pandas.pydata.org/pandas-docs/stable/
  * https://docs.scipy.org/doc/
