# Pairs Trading Algorithm

This repository contains the **Pairs Trading Algorithm** implemented in Python. The algorithm utilizes statistical arbitrage strategies to trade two correlated stocks by capitalizing on their relative price movements. It enters long and short positions when the price spread between two assets deviates from historical norms.

![Pairs Trading Algorithm](https://i.imgur.com/IhOBiOT.jpeg)

## Features
- **Pairs Selection**: Identifies pairs of stocks with high correlation.
- **Trading Strategy**: Opens long and short positions based on price spread.
- **Data Visualization**: Graphical representation of the stock price spread.
- **Market Neutral**: Minimizes exposure to broad market movements.
  
## Requirements

Ensure you have the following Python packages installed:

- `matplotlib` - For plotting and visualizing data.
- `yfinance` - For downloading stock data from Yahoo Finance.
- `numpy` - For numerical operations and calculations.
  
You can install these dependencies by running the following:

```bash
pip install -r requirements.txt
```

Alternatively, you can manually install them using:

```bash
pip install matplotlib yfinance numpy
```

## Setup and Usage

1. **Clone the repository**:

```bash
git clone https://github.com/carrolldominic/carroll-quant.git
```

2. **Navigate to the project directory**:

```bash
cd carroll-quant
```

3. **Run the algorithm**:

Execute the Python script that implements the pairs trading strategy:

```bash
python pairs_trading_algorithm.py
```

### How It Works

1. **Selecting Stock Pairs**: The algorithm selects two stocks with high historical correlation (e.g., Coca-Cola and PepsiCo). The correlation is calculated based on historical stock price data.

2. **Spread Calculation**: The spread between the two stocks is computed, representing the difference in their prices. The spread is then monitored over time.

3. **Trading Signals**:
   - The algorithm enters a **long position** (buy) when the spread is unusually low.
   - It enters a **short position** (sell) when the spread is unusually high.
   - The strategy assumes that the spread will revert to its mean, allowing profits from fluctuations in the spread.

4. **Data Visualization**: The algorithm generates plots for the stock prices, spread, and performance. This allows you to visually track how the strategy performs over time.

## File Structure

```
carroll-quant/
│
├── main.py.py   # Main script implementing the pairs trading strategy
├── README.md                   # Project documentation (this file)
```

## Example Output

The algorithm generates visualizations including:
- **Stock Price Plot**: Shows the historical price movements of the two stocks.
- **Performance Over Time**: Displays the performance of the alg over time.

## Disclaimer

**This algorithm is highly experimental and should not be used for actual financial trading.** It is not intended as financial advice or a production-ready trading strategy. The algorithm is for educational and experimental purposes only, and there are significant risks involved in applying such strategies in real-world financial markets. Please use it with caution, and do not trade real capital based on the results without thorough evaluation and professional consultation.

## Contributing

If you'd like to contribute to this project, feel free to fork the repository, create a new branch, and submit a pull request. All contributions are welcome!

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
