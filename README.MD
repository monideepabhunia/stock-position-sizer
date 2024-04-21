# POSITION SIZE CALCULATOR

(only Indian markets Equity supported currently)


![ss2](https://user-images.githubusercontent.com/37045880/203510840-a0f33f59-83c8-4428-8d56-03e673b0227e.png)

### This app aims to provide the best "position size" for a trade with a predefined "stop loss"

### Suppose in a trade, an investor/trader can take loss upto Rs.1500.

### so,

### For a given Risk Amount(1500) and the desired "Buy Price" of the stock and the "SL difference" between the desired buy price and desired SL price, it calculates the optimal position size, breakeven point and required margin for that specific trade

### including

### the brokerage charges and all hidden charges

## Installation :

1. Pre-requisites : [python](https://www.python.org/downloads/) must be installed
2. In a folder clone this repository and install the required files - `pip install -r requirements.txt`
3. run the `main.py` file by running `python main.py` in terminal or in case of any virtual environment run `source {virtualenv_name}/bin/activate && python main.py`


![ss1](https://user-images.githubusercontent.com/37045880/203510385-396ad955-1240-4659-9aeb-ccf4030191ac.png)

## Usage :

1. Enter desired maximum risk amount per trade in the "Risk Amount" tab
2. Select Buy/Sell which trade type it is
3. Enter the desired Buy/Sell "Entry price"
4. Enter the absolute difference in Rs. between the desired StopLoss price and Entry price
5. Click Calculate
6. It will show you the probable Trigger Price which you had in your mind, and it is for CROSS VERIFICATION
7. The best position size will be shown followed by the "Breakeven" and "Margin" amount required for that trade

![ss2](https://user-images.githubusercontent.com/37045880/203510695-b1ef9e67-e0d6-4ad8-8ea6-630acdfcc56b.png)

