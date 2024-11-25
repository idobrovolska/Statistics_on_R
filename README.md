Here you can find projects aimed on statistical data analysis, such as
__correlation analysis, hypothesis testing, construction of confidence intervals etc__

1. __Cor_analysis__ is a correation analysis project. The purpose of the work is to investigate the relationships between stock prices of various companies on the New York Stock Exchange based on data from 2002-2013.

We have a raw directory 'daily' from 'daily_sp500' which is being filtered twice (second is on your own, just to choose only 10 complanies). First-time filtering is performed in a file __cs.py__, where we are choosing only those companies which have its table symbols started with letters I and T (description of each company's data, including symbols, is available in file "List_of_S&P_500_companies") and a result is stored in 'new' directory. All the main actions will be further performed with __'working_dir'__ (where we have moved 10 random chosen companies from 'new'). 
