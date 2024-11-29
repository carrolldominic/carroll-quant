# Carroll 2024
# Disclaimer: This algorithm is for educational and experimental purposes only and is not intended for real trading or financial decision-making.

import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

import yfinance as yf
import numpy as np

def pairs(tickerA, tickerB, tradingThreshold, showPlot):
    historyLength = "5y"

    a = yf.Ticker(tickerA)
    b = yf.Ticker(tickerB)

    historical_data_1 = a.history(period=historyLength)
    historical_data_2 = b.history(period=historyLength)

    merged_data = historical_data_1[['Close']].join(historical_data_2[['Close']], lsuffix='_A', rsuffix='_B')

    rebase_index = 0
    a_index = 1
    b_index = 1

    a_last, b_last = None, None

    ratios = {}
    gains = {}

    tradeEngaged = False

    longBasis = None
    shortBasis = None
    gainIndex = 1
    for date, row in merged_data.iterrows():
        close_price_A = row['Close_A']
        close_price_B = row['Close_B']

        if a_last != None:
            a_index = a_index * (close_price_A/a_last)
            b_index = b_index * (close_price_B/b_last)
            rebase_index += 1

        
        a_last = close_price_A
        b_last = close_price_B

        ratio = a_index/b_index

        if ratio>(1+tradingThreshold):
            # short A, long B
            if tradeEngaged != True:
                tradeEngaged = True

                longBasis = [close_price_B, 'Close_B']
                shortBasis = [close_price_A, 'Close_A']
        if ratio<(1-tradingThreshold):
            # short B, long A
            if tradeEngaged != True:               
                tradeEngaged = True

                longBasis = [close_price_A, 'Close_A']
                shortBasis = [close_price_B, 'Close_B']

        if (0.99) <= ratio <= (1.01):
            if tradeEngaged == True:
                tradeEngaged = False
                longGain = row[longBasis[1]]/longBasis[0]-1
                shortGain = -1*(row[shortBasis[1]]/shortBasis[0]-1)

                weight = 0.2
                newGainIndex = gainIndex * (1 + longGain * weight) * (1 + shortGain * weight)
                totalGain = newGainIndex / gainIndex - 1
                gainIndex = newGainIndex

                gains[date] = gainIndex-1

                # print('gain index update: ', gainIndex)

                print("Long gain: ", longGain, f" (Bought {longBasis[0]} and sold {row[longBasis[1]]})")
                print("Short gain: ", shortGain, f" (Short {shortBasis[0]} and covered {row[shortBasis[1]]})")


        ratios[date] = ratio

        if rebase_index == 30:
            a_index = 1
            b_index = 1
            rebase_index = 0

    ratios_val = list(ratios.values())
    ratios_mean = np.mean(ratios_val)
    ratios_stdev = np.std(ratios_val)

    tail_up = ratios_mean + ratios_stdev * 2
    tail_down = ratios_mean - ratios_stdev * 2

    print("5y CAGR: ", (gainIndex / 1) ** (1 / 5) - 1)

    if showPlot:
        plt.figure(figsize=(10, 5))
        
        ax2 = plt.gca().twinx()
        ax2.plot(gains.keys(), gains.values(), marker='s', color='g', markersize=2, label='Gains')
        ax2.yaxis.set_major_formatter(ticker.FuncFormatter(lambda x, pos: f'{x * 100:.0f}%'))

        plt.plot(ratios.keys(), ratios.values(), marker='o', color='b', markersize=2)

        plt.title(f"Pairs: {tickerA} / {tickerB}", fontsize=14)
        plt.xlabel('Date', fontsize=12)
        plt.ylabel('', fontsize=12) #pairs ratio

        plt.grid(False)
        plt.xticks(rotation=45)
        plt.tight_layout()

        print(f"Mean: {ratios_mean}  |  StDev: {ratios_stdev}")


        plt.axhline(y=tail_up, color='r', linestyle='--')
        plt.axhline(y=tail_down, color='r', linestyle='--')





        plt.show()

    return {"Mean": ratios_mean, "StDev": ratios_stdev}

def findBestPair(pairsToTest):
    calculatedPairs = {}

    for i, sublist in enumerate(pairsToTest):
        testPair = pairs(sublist[0], sublist[1], 0.05, False)
        sd = testPair["StDev"]
        pairString = f"{sublist[0]}/{sublist[1]}"
        print(f"{pairString}: {sd}")

        calculatedPairs[pairString] = sd


    min_key = min(calculatedPairs, key=calculatedPairs.get)
    min_value = calculatedPairs[min_key]

    print("Pair:", min_key)
    print("SD:", min_value)

    meanSD = np.mean(list(calculatedPairs.values()))
    print("Mean SD: ", meanSD)

def getInput():
    newStockA = input("Enter new ticker A: ")
    newStockB = input("Enter new ticker B: ")
    pairs(newStockA, newStockB, 0.074, True)
    getInput()

# findBestPair(testList)
getInput()