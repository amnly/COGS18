def mean2020(input):
    """
    returns the mean of the stock's 2020 volume, opening, high, low, closing, and adjacent closing price.
    """ 
    import pandas as pd
    inputstock = input.upper() # set name as caps
    stockinp = pd.read_csv(inputstock+".csv") # read in data
    stockinp['Date'] = pd.to_datetime(stockinp['Date'], errors='coerce') # convert column to date time
    stockinp['Year'] = stockinp['Date'].dt.year # create column based on year in date
    print("Mean of 2020 for " +inputstock+ "'s prices and volumes:")

    year = stockinp.groupby(['Year']).mean() # group by year, find mean of year
    latest = year.iloc[[-1]] # latest year of the stock data
    return latest
def March2020Increase(input):
    """
    return the days in March 2020 where the input stock's opening prices increased from the previous day
    """ 
    import numpy as np
    import pandas as pd
    inputstock = input.upper() # cap name
    stockinp = pd.read_csv(inputstock+".csv") # read in datafile
    stockinp['Date'] = pd.to_datetime(stockinp['Date'], errors='coerce') # convert column to date time
    stockinp['Year'] = stockinp['Date'].dt.year # create column based on year in date
    stockinp['Month'] = stockinp['Date'].dt.month 
    stockinp['Day'] = stockinp['Date'].dt.day
    stockinp['Date'] = stockinp['Date'].dt.date # this will remove the timestamp from the date when printing later on
    
    is_2020 = stockinp['Year']==2020 # filter for year
    stock2020 = stockinp[is_2020] # places into dataframe
    march_2020 = stock2020['Month']==3 # filter for 3rd month, march
    stockMarch2020 = stock2020[march_2020] # append column
    stockMarch2020 = stockMarch2020.sort_values('Date', ascending = True)
    
    print("Days in March 2020 where " +inputstock+"'s opening prices increased from the previous day:")
    
    y=np.arange(len(stockMarch2020['Date'])-1) # gives the count of the number of days
    
    result=[0] # list to append to
    for i in y:
        stockdiff = stockMarch2020['Open'].iloc[i+1] - stockMarch2020['Open'].iloc[i] # find differences in opening prices
        result.append(stockdiff)
    
    stockMarch2020['result']=result # append column for easier filtering
    list1 = []
    z=np.arange(len(stockMarch2020['Date'])) # gives count of rows
    for x in z:
        if stockMarch2020['result'].iloc[x]>0: # filter for positive differences
            print(stockMarch2020['Date'].iloc[x]) 
            list1 = np.append(list1, stockMarch2020['Date'].iloc[x])
    return list1
def March2020Closing(input):
    """
    return a chart of the input stock's closing prices in March 2020
    """ 
    import numpy as np
    import matplotlib.pyplot as plt
    import pandas as pd
    inputstock = input.upper() # cap name
    stockinp = pd.read_csv(inputstock+".csv") # read in datafile
    stockinp['Date'] = pd.to_datetime(stockinp['Date'], errors='coerce') # convert column to date time
    stockinp['Year'] = stockinp['Date'].dt.year # create column based on year in date
    stockinp['Month'] = stockinp['Date'].dt.month # column based on month
    
    is_2020 = stockinp['Year']==2020 # filter for year
    stock2020 = stockinp[is_2020] # places into dataframe
    march_2020 = stock2020['Month']==3 # filter for 3rd month, march
    stockMarch2020 = stock2020[march_2020] # append
    stockMarch2020 = stockMarch2020.sort_values('Date', ascending = True) # sort ascending of column
    
    stockMarch2020['Day'] = stockMarch2020['Date'].dt.day # create column basted on day
    # define variable
    day = stockMarch2020.Day
    close = stockMarch2020.Close
    # plotting numbers of days against closing prices
    plt.figure(figsize=(10,5))
    plt.plot(day,close)
    plt.xticks(np.arange(min(day), max(day), 1.0)) # set xaxis ticks using the first and last days
    plt.xlabel('Day')
    plt.ylabel('Closing Price')
    return plt.title(inputstock+' Closing Prices March 2020')
    plt.show()
