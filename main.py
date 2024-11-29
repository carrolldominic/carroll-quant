import matplotlib.pyplot as plt
import yfinance as yf
import numpy as np



def pairs(tickerA, tickerB, showPlot):
    length = "5y"

    a = yf.Ticker(tickerA)
    b = yf.Ticker(tickerB)

    historical_data_1 = a.history(period=length)
    historical_data_2 = b.history(period=length)

    merged_data = historical_data_1[['Close']].join(historical_data_2[['Close']], lsuffix='_A', rsuffix='_B')

    rebase_index = 0
    a_index = 1
    b_index = 1

    a_last, b_last = None, None

    ratios = {}

    for date, row in merged_data.iterrows():
        close_price_A = row['Close_A']
        close_price_B = row['Close_B']
        # print(f"Date: {date}, AAPL Close: {close_price_COST}, MSFT Close: {close_price_BJ}")

        if a_last != None:
            a_index = a_index * (close_price_A/a_last)
            b_index = b_index * (close_price_B/b_last)
            rebase_index += 1

        
        a_last = close_price_A
        b_last = close_price_B

        ratio = a_index/b_index
        ratios[date] = ratio

        if rebase_index == 30:
            a_index = 1
            b_index = 1
            rebase_index = 0

    ratios_val = list(ratios.values())
    ratios_mean = np.mean(ratios_val)
    ratios_stdev = np.std(ratios_val)

    if showPlot:
        plt.figure(figsize=(10, 5))
        plt.plot(ratios.keys(), ratios.values(), marker='o', color='b', markersize=2)

        plt.title(f"Pairs: {tickerA} / {tickerB}", fontsize=14)
        plt.xlabel('Date', fontsize=12)
        plt.ylabel('Pairs Ratio', fontsize=12)

        plt.grid(False)
        plt.xticks(rotation=45)
        plt.tight_layout()



        print(f"Mean: {ratios_mean}  |  StDev: {ratios_stdev}")

        tail_up = ratios_mean + ratios_stdev * 2
        tail_down = ratios_mean - ratios_stdev * 2

        plt.axhline(y=tail_up, color='r', linestyle='--')
        plt.axhline(y=tail_down, color='r', linestyle='--')

        
        plt.show()

    return {"Mean": ratios_mean, "StDev": ratios_stdev}

def findBestPair(pairsToTest):
    calculatedPairs = {}

    for i, sublist in enumerate(pairsToTest):
        testPair = pairs(sublist[0], sublist[1], False)
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
    pairs(newStockA, newStockB, True)
    getInput()

testList = [
    ['AAPL', 'MSFT'],   # Technology: Apple vs. Microsoft
    ['GOOG', 'META'],   # Technology/Online: Google vs. Meta (Facebook)
    ['TSLA', 'RIVN'],   # Electric Vehicles: Tesla vs. Rivian
    ['NVDA', 'AMD'],    # Semiconductors: NVIDIA vs. AMD
    ['AMD', 'INTC'],    # Semiconductors: AMD vs. Intel
    ['V', 'MA'],        # Payments: Visa vs. Mastercard
    ['JPM', 'GS'],      # Banking/Finance: JPMorgan Chase vs. Goldman Sachs
    ['BABA', 'AMZN'],   # E-commerce: Alibaba vs. Amazon
    ['WMT', 'TGT'],     # Retail: Walmart vs. Target
    ['DIS', 'CMCSA'],   # Media/Entertainment: Disney vs. Comcast
    ['PEP', 'KO'],      # Beverages: PepsiCo vs. Coca-Cola
    ['MCD', 'YUM'],     # Restaurants: McDonald's vs. Yum! Brands
    ['PG', 'CL'],       # Consumer Goods: Procter & Gamble vs. Colgate-Palmolive
    ['XOM', 'CVX'],     # Energy: ExxonMobil vs. Chevron
    ['LMT', 'BA'],      # Aerospace/Defense: Lockheed Martin vs. Boeing
    ['MDT', 'ABT'],     # Healthcare/Medical Devices: Medtronic vs. Abbott Laboratories
    ['CAT', 'DE'],      # Heavy Machinery: Caterpillar vs. Deere & Co.
    ['UNH', 'CVS'],     # Healthcare: UnitedHealth vs. CVS Health
    ['AMT', 'CCI'],     # Telecom Infrastructure: American Tower vs. Crown Castle
    ['T', 'VZ'],        # Telecommunications: AT&T vs. Verizon
    ['WBA', 'CVS'],     # Retail/Healthcare: Walgreens Boots Alliance vs. CVS Health
    ['PFE', 'MRK'],     # Pharmaceuticals: Pfizer vs. Merck
    ['LUV', 'DAL'],     # Airlines: Southwest Airlines vs. Delta Air Lines
    ['AIG', 'TRV'],     # Insurance: AIG vs. Travelers
    ['CSCO', 'ORCL'],   # Technology/Software: Cisco vs. Oracle
    ['NKE', 'ADIDY'],   # Apparel/Footwear: Nike vs. Adidas
    ['FIS', 'FISV'],    # Payment Services: FIS vs. Fiserv
    ['SBUX', 'DNKN'],   # Coffee: Starbucks vs. Dunkin' Brands
    ['SO', 'EXC'],      # Utilities: Southern Co. vs. Exelon
    ['NFLX', 'DIS'],    # Media/Entertainment: Netflix vs. Disney
    ['SHW', 'PPG'],     # Paints/Coatings: Sherwin-Williams vs. PPG Industries
    ['RTX', 'GD'],      # Aerospace/Defense: Raytheon Technologies vs. General Dynamics
    ['ZM', 'TEAM']      # Collaboration Software: Zoom vs. Atlassian
]


# findBestPair(testList)
getInput()