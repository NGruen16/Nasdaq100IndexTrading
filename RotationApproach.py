import sys
import pandas as pd
import numpy as np
from statistics import mean


def iso1_short(x,y,z,portfoliobalance):
    # Inputs
    portfoliovalue = portfoliobalance
    stocksholding = 1

    # Constants
    portfoliobackteststart = 100000
    holdinggreen = 0
    holdingred = 0
    df = pd.read_csv("PTON2.csv")
    currentclose = x
    futureclose = y
    pastclose = currentclose - 1
    portfolioovertime = []

    while futureclose != z:
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
        averagefinalchangedranked = mean(finalchange)
        finalchange = [x / averagefinalchangedranked for x in finalchange]

        # Get New and Old Lists and Find % Change For Holding Day
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
            # finalchangeholdingranked = list(finalchangeholdingranked)
            # finalchangeholdingranked.reverse()
            # print(finalchangeholdingranked)
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

        # End of Iteration
        print("END OF TRADE")
        portfolioovertime.append(portfoliovalue)

        # Changes for Next Iteration
        pastclose = pastclose + 1
        currentclose = currentclose + 1
        futureclose = futureclose + 1

    print("THE FINAL BALANCE IS " + str(summedportfolio))
    print(summedportfolio)
    stdev = np.std(portfolioovertime)
    print(stdev)
    pchange = (summedportfolio - portfoliobackteststart) / portfoliobackteststart * 100000
    print(pchange)
    #ranking = pchange / stdev
    #print(ranking)


    return (summedportfolio, portfolioovertime)
def iso1_long(x,y,z,portfoliobalance):
    # Inputs
    portfoliovalue = portfoliobalance
    stocksholding = 1

    # Constants
    holdinggreen = 0
    portfoliobackteststart = 100000
    holdingred = 0
    df = pd.read_csv("PTON2.csv")
    currentclose = x
    futureclose = y
    pastclose = currentclose - 1
    portfolioovertime = []

    while futureclose != z:
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
            # finalchangeholdingranked = list(finalchangeholdingranked)
            # finalchangeholdingranked.reverse()
            # print(finalchangeholdingranked)
            if averagefinalchangedranked > 0:
                investmentchange = finalchangeholdingranked[holdingiterator] * investments + investments
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

        # End of Iteration
        print("END OF TRADE")
        portfolioovertime.append(portfoliovalue)

        # Changes for Next Iteration
        pastclose = pastclose + 1
        currentclose = currentclose + 1
        futureclose = futureclose + 1

    print("THE FINAL BALANCE IS " + str(summedportfolio))
    print(portfolioovertime)
    stdev = np.std(portfolioovertime)
    print(stdev)
    pchange = (summedportfolio - portfoliobackteststart) / portfoliobackteststart * 100000
    print(pchange)
    #ranking = pchange / stdev

    return (summedportfolio, portfolioovertime)
def iso3_short(x,y,z,portfoliobalance):
    # Inputs
    portfoliovalue = portfoliobalance
    stocksholding = 1

    # Constants
    holdinggreen = 0
    portfoliobackteststart = 100000
    holdingred = 0
    df = pd.read_csv("PTON2.csv")
    currentclose = x
    futureclose = y
    pastclose = currentclose - 1
    portfolioovertime = []

    while futureclose != z:
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
            finalchangeholdingranked = list(finalchangeholdingranked)
            finalchangeholdingranked.reverse()
            print(finalchangeholdingranked)
            if averagefinalchangedranked < 0:
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

        # End of Iteration
        print("END OF TRADE")
        portfolioovertime.append(portfoliovalue)

        # Changes for Next Iteration
        pastclose = pastclose + 1
        currentclose = currentclose + 1
        futureclose = futureclose + 1

    print("THE FINAL BALANCE IS " + str(summedportfolio))
    print(portfolioovertime)
    stdev = np.std(portfolioovertime)
    print(stdev)
    pchange = (summedportfolio - portfoliobackteststart) / portfoliobackteststart * 100000
    print(pchange)
    #ranking = pchange / stdev

    return (summedportfolio, portfolioovertime)
def iso3_long(x,y,z,portfoliobalance):
    # Inputs
    portfoliovalue = portfoliobalance
    stocksholding = 1

    # Constants
    holdinggreen = 0
    portfoliobackteststart = 100000
    holdingred = 0
    df = pd.read_csv("PTON2.csv")
    currentclose = x
    futureclose = y
    pastclose = currentclose - 1
    portfolioovertime = []

    while futureclose != z:
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
            finalchangeholdingranked = list(finalchangeholdingranked)
            finalchangeholdingranked.reverse()
            print(finalchangeholdingranked)
            if averagefinalchangedranked < 0:
                investmentchange = finalchangeholdingranked[holdingiterator] * investments + investments
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

        # End of Iteration
        print("END OF TRADE")
        portfolioovertime.append(portfoliovalue)

        # Changes for Next Iteration
        pastclose = pastclose + 1
        currentclose = currentclose + 1
        futureclose = futureclose + 1

    print("THE FINAL BALANCE IS " + str(summedportfolio))
    print(portfolioovertime)
    print(summedportfolio)
    stdev = np.std(portfolioovertime)
    print(stdev)
    pchange = (summedportfolio - portfoliobackteststart) / portfoliobackteststart * 100000
    print(pchange)
    #ranking = pchange / stdev

    return (summedportfolio, portfolioovertime)
def iso2_long(x,y,z,portfoliobalance):
    # Inputs
    portfoliovalue = portfoliobalance
    stocksholding = 1

    # Constants
    holdinggreen = 0
    portfoliobackteststart = 100000
    holdingred = 0
    df = pd.read_csv("PTON2.csv")
    currentclose = x
    futureclose = y
    pastclose = currentclose - 1
    portfolioovertime = []

    while futureclose != z:
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
            if averagefinalchangedranked < 0:
                investmentchange = finalchangeholdingranked[holdingiterator] * investments + investments
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

        # End of Iteration
        print("END OF TRADE")
        portfolioovertime.append(portfoliovalue)

        # Changes for Next Iteration
        pastclose = pastclose + 1
        currentclose = currentclose + 1
        futureclose = futureclose + 1

    print("THE FINAL BALANCE IS " + str(summedportfolio))
    print(portfolioovertime)
    print(summedportfolio)
    stdev = np.std(portfolioovertime)
    print(stdev)
    pchange = (summedportfolio - portfoliobackteststart) / portfoliobackteststart * 100000
    print(pchange)
    #ranking = pchange / stdev

    return (summedportfolio, portfolioovertime)
def iso2_short(x,y,z,portfoliobalance):
    # Inputs
    portfoliovalue = portfoliobalance
    stocksholding = 1

    # Constants
    holdinggreen = 0
    portfoliobackteststart = 100000
    holdingred = 0
    df = pd.read_csv("PTON2.csv")
    currentclose = x
    futureclose = y
    pastclose = currentclose - 1
    portfolioovertime = []

    while futureclose != z:
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
            if averagefinalchangedranked < 0:
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

        # End of Iteration
        print("END OF TRADE")
        portfolioovertime.append(portfoliovalue)

        # Changes for Next Iteration
        pastclose = pastclose + 1
        currentclose = currentclose + 1
        futureclose = futureclose + 1

    print("THE FINAL BALANCE IS " + str(summedportfolio))
    print(portfolioovertime)
    print(summedportfolio)
    stdev = np.std(portfolioovertime)
    print(stdev)
    pchange = (summedportfolio - portfoliobackteststart) / portfoliobackteststart * 100000
    print(pchange)
    #ranking = pchange / stdev

    return (summedportfolio, portfolioovertime)
def iso4_short(x,y,z,portfoliobalance):
    # Inputs
    portfoliovalue = portfoliobalance
    stocksholding = 1

    # Constants
    holdinggreen = 0
    portfoliobackteststart = 100000
    holdingred = 0
    df = pd.read_csv("PTON2.csv")
    currentclose = x
    futureclose = y
    pastclose = currentclose - 1
    portfolioovertime = []

    while futureclose != z:
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
            finalchangeholdingranked = list(finalchangeholdingranked)
            finalchangeholdingranked.reverse()
            print(finalchangeholdingranked)
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

        # End of Iteration
        print("END OF TRADE")
        portfolioovertime.append(portfoliovalue)

        # Changes for Next Iteration
        pastclose = pastclose + 1
        currentclose = currentclose + 1
        futureclose = futureclose + 1

    print("THE FINAL BALANCE IS " + str(summedportfolio))
    print(portfolioovertime)
    print(summedportfolio)
    stdev = np.std(portfolioovertime)
    print(stdev)
    pchange = (summedportfolio - portfoliobackteststart) / portfoliobackteststart * 100000
    print(pchange)
    #ranking = pchange / stdev



    return (summedportfolio, portfolioovertime)
def iso4_long(x,y,z,portfoliobalance):
    # Inputs
    portfoliovalue = portfoliobalance
    stocksholding = 1

    # Constants
    holdinggreen = 0
    portfoliobackteststart = 100000
    holdingred = 0
    df = pd.read_csv("PTON2.csv")
    currentclose = x
    futureclose = y
    pastclose = currentclose - 1
    portfolioovertime = []

    while futureclose != z:
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
            finalchangeholdingranked = list(finalchangeholdingranked)
            finalchangeholdingranked.reverse()
            print(finalchangeholdingranked)
            if averagefinalchangedranked > 0:
                investmentchange = finalchangeholdingranked[holdingiterator] * investments + investments
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

        # End of Iteration
        print("END OF TRADE")
        portfolioovertime.append(portfoliovalue)

        # Changes for Next Iteration
        pastclose = pastclose + 1
        currentclose = currentclose + 1
        futureclose = futureclose + 1

    print("THE FINAL BALANCE IS " + str(summedportfolio))
    print(portfolioovertime)
    print(summedportfolio)
    stdev = np.std(portfolioovertime)
    print(stdev)
    pchange = (summedportfolio - portfoliobackteststart) / portfoliobackteststart * 100000
    print(pchange)
    #ranking = pchange / stdev

    return (summedportfolio, portfolioovertime)

def beststratabove(iso1_short, iso1_long, iso4_short, iso4_long):
    stratlist = [iso1_short, iso1_long, iso4_short, iso4_long]
    stratlist.sort(reverse=True)
    beststrat = stratlist[0]
    return beststrat
def beststratbelow(iso3_short, iso3_long, iso2_short, iso2_long):
    stratlist = [iso3_short, iso3_long, iso2_short, iso2_long]
    stratlist.sort(reverse=True)
    beststrat = stratlist[0]
    return beststrat
def truncate(num, n):
    integer = int(num * (10**n))/(10**n)
    return float(integer)

runninglength = 2

currentclose = 1
futureclose = 2
enddate = currentclose + runninglength

cclose = enddate - 1
fclose = cclose + 1
endclose = fclose + 1

portfoliorunning = 100000
portfoliobalancebackteststart = 100000
portfoliorunninglist = []
it = 0

while endclose != 250:
    iso1_shortnum = iso1_short(currentclose, futureclose, enddate, portfoliobalancebackteststart)
    iso1_longnum = iso1_long(currentclose, futureclose, enddate, portfoliobalancebackteststart)
    iso3_longnum = iso3_long(currentclose, futureclose, enddate, portfoliobalancebackteststart)
    iso3_shortnum = iso3_short(currentclose, futureclose, enddate, portfoliobalancebackteststart)
    iso2_shortnum = iso2_short(currentclose, futureclose, enddate, portfoliobalancebackteststart)
    iso2_longnum = iso2_long(currentclose, futureclose, enddate, portfoliobalancebackteststart)
    iso4_shortnum = iso4_short(currentclose, futureclose, enddate, portfoliobalancebackteststart)
    iso4_longnum = iso4_long(currentclose, futureclose, enddate, portfoliobalancebackteststart)

    beststratabovenum = beststratabove(iso1_shortnum[0], iso1_longnum[0], iso4_shortnum[0], iso4_longnum[0])
    beststratbelownum = beststratbelow(iso3_shortnum[0], iso3_longnum[0], iso2_shortnum[0], iso2_longnum[0])
    print('')
    print(iso3_longnum[0])
    print(iso3_shortnum[0])
    print(iso1_longnum[0])
    print(iso1_shortnum[0])
    print(iso2_shortnum[0])
    print(iso2_longnum[0])
    print(iso4_shortnum[0])
    print(iso4_longnum[0])
    print('')
    print(beststratabovenum)
    print(beststratbelownum)

    cclose = enddate - 1
    fclose = cclose + 1
    endclose = fclose + 1
    print(portfoliorunning)
    it = it + 1

    portfoliorunningoriginal = portfoliorunning
    print(portfoliorunningoriginal)

    if  beststratabovenum == iso1_longnum[0]:
        portfoliorunningfortest = iso1_long(cclose, fclose, endclose, portfoliorunning)
        print("iso1_longnum")
    elif beststratabovenum == iso1_shortnum[0]:
        portfoliorunningfortest = iso1_short(cclose, fclose, endclose, portfoliorunning)
        print("iso1_shortnum")
    elif beststratabovenum == iso4_longnum[0]:
        portfoliorunningfortest = iso4_long(cclose, fclose, endclose, portfoliorunning)
        print("iso4_longnum")
    elif beststratabovenum == iso4_shortnum[0]:
        portfoliorunningfortest = iso4_short(cclose, fclose, endclose, portfoliorunning)
        print("iso4_shortnum")

    portfoliorunningfortest1 = portfoliorunningfortest[0]
    print(portfoliorunningfortest1)

    if portfoliorunningfortest1 == portfoliorunningoriginal:
        if beststratbelownum == iso3_longnum[0]:
            portfoliorunning = iso3_long(cclose, fclose, endclose, portfoliorunning)
            print("iso3_longnum")
        elif beststratbelownum == iso3_shortnum[0]:
            portfoliorunning = iso3_short(cclose, fclose, endclose, portfoliorunning)
            print("iso3_shortnum")
        elif beststratbelownum == iso2_shortnum[0]:
            portfoliorunning = iso2_short(cclose, fclose, endclose, portfoliorunning)
            print("iso2_shortnum")
        elif beststratbelownum == iso2_longnum[0]:
            portfoliorunning = iso2_long(cclose, fclose, endclose, portfoliorunning)
            print("iso2_longnum")
    else:
        portfoliorunning = portfoliorunningfortest

    print(portfoliorunning)
    portfoliorunningchanges = portfoliorunning[1]
    portfoliorunning = portfoliorunning[0]
    print(portfoliorunning)
    print(portfoliorunningchanges)
    portfoliorunninglist.append(portfoliorunning)
    print(portfoliorunninglist)

    currentclose = currentclose + 1
    futureclose = futureclose + 1
    enddate = currentclose + runninglength

print("FINISHED")
print(portfoliorunning)
print(portfoliorunninglist)

