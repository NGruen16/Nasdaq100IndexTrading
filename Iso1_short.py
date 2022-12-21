import pandas as pd
import numpy as np
from statistics import mean

#Inputs
portfoliovalue = 100000
stocksholding = 1

#Constants
holdinggreen = 0
holdingred = 0
df = pd.read_csv("PTON2.csv")
pastclose = 0
currentclose = 1
futureclose = 2
portfolioovertime = []

while futureclose != 250:
    # Get New and Old Lists and Find % Change For Lookback Day
    pastclose1 = pastclose + 1
    currentclose1 = currentclose + 1
    futureclose1 = futureclose + 1

    old1 = df.iloc[pastclose:pastclose1]
    new1 = df.iloc[currentclose:currentclose1]
    dflistold = old1.values.tolist()
    dflistnew = new1.values.tolist()
    dflistold = dflistold.pop(0)
    dflistnew = dflistnew.pop(0)
    dflistold.pop(0)
    dflistnew.pop(0)

    arrayold = np.array(dflistold)
    arraynew = np.array(dflistnew)

    subtractedarray = np.subtract(arraynew, arrayold)
    finalchange = np.divide(subtractedarray, arrayold)
    finalchange = list(finalchange)
    print(finalchange)
    averagefinalchangedranked = mean(finalchange)
    print(averagefinalchangedranked)
    finalchange = [x / averagefinalchangedranked for x in finalchange]


    # Get New and Old Lists and Find % Change For Holding Day
    print("")
    oldholding = df.iloc[currentclose:currentclose1]
    newholding = df.iloc[futureclose:futureclose1]
    dflistoldholding = oldholding.values.tolist()
    dflistnewholding = newholding.values.tolist()
    dflistoldholding = dflistoldholding.pop(0)
    dflistnewholding = dflistnewholding.pop(0)
    dflistoldholding.pop(0)
    dflistnewholding.pop(0)

    arrayoldholding = np.array(dflistoldholding)
    arraynewholding = np.array(dflistnewholding)

    subtractedarrayholding = np.subtract(arraynewholding, arrayoldholding)
    finalchangeholding = np.divide(subtractedarrayholding, arrayoldholding)
    finalchangeholding = list(finalchangeholding)
    print(finalchangeholding)
    print('')

    # Get ticker list
    tickers = df.columns
    tickers = tickers.values.tolist()
    tickers.pop(0)

    # Zip and Rank Both Lists
    print('')
    zippedlist = list(zip(finalchange, tickers, finalchangeholding))
    zippedlist.sort(reverse=True)
    print("the ranked zipped list is " + str(zippedlist))
    res = list(zip(*zippedlist))
    finalchangeranked = res[0]
    tickersranked = res[1]
    finalchangeholdingranked = res[2]

    # Get Data for the % Change of Next Day
    investments = portfoliovalue / stocksholding
    holdingiterator = 0
    portfoliolist = []
    print("Investment is " + str(investments))

    while holdingiterator != stocksholding:
        print(averagefinalchangedranked)
        fcr = finalchangeranked[holdingiterator]
        print("FCR IS: " + str(fcr))
        #finalchangeholdingranked = list(finalchangeholdingranked)
        #finalchangeholdingranked.reverse()
        #print(finalchangeholdingranked)
        if averagefinalchangedranked > 0:
            investmentchange = finalchangeholdingranked[holdingiterator] * investments - investments
            print(finalchangeholdingranked[holdingiterator])
            print(investmentchange)
            investmentchange = abs(investmentchange)
            portfoliolist.append(investmentchange)
            holdingiterator = holdingiterator + 1
            print(portfoliolist)
            if investmentchange > investments:
                holdinggreen = holdinggreen + 1
            else:
                holdingred = holdingred + 1
        else:
            portfoliolist.append(investments)
            holdingiterator = holdingiterator + 1
            print(portfoliolist)

    print(portfoliolist)

    print("# of Investments that were Green is " + str(holdinggreen))
    print("# of Investments that were Red is " + str(holdingred))

    # Sum Portfolios
    summedportfolio = sum(portfoliolist)
    print(summedportfolio)
    portfoliovalue = summedportfolio

    #End of Iteration
    print("END OF TRADE")
    portfolioovertime.append(portfoliovalue)


    # Changes for Next Iteration
    pastclose = pastclose + 1
    currentclose = currentclose + 1
    futureclose = futureclose + 1



print("THE FINAL BALANCE IS " + str(summedportfolio))
print(portfolioovertime)

iso1_short = summedportfolio

