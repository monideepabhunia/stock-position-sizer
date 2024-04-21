def brokerageCalc(buy, sell, quantity):
    try:
        buy = int(buy)
        sell = int(sell)
    except:
        if(buy != '' and sell == ''):
            try:
                buy = int(buy)
                sell = buy
            except:
                buy = 0
                sell = 0

        elif(buy == '' and sell != ''):
            try:
                sell = int(sell)
                buy = sell
            except:
                sell = 0
                buy = 0

        else:
            buy = 0
            sell = 0
            # quantity = 0

    try:
        quantity = int(quantity)
    except:
        quantity = 0

    turnover = (buy+sell)*quantity
    brokerage = 40
    stt = round(((sell*quantity)*(0.025))/100, 2)
    exchange_txn_charge = round((turnover*0.00345)/100, 2)
    gst = round((brokerage+exchange_txn_charge)*0.18, 2)
    sebi = round((10/10000000)*turnover, 2)
    stamp = round((0.003*(buy*quantity)/100), 2) if (buy *
                                                     quantity) < 10000000 else 300

    total_brokerages = round(brokerage +
                             stt+exchange_txn_charge+gst+sebi+stamp, 2)

    total_pnl = ((sell - buy)*quantity) - total_brokerages
    if(quantity == 0):
        total_pnl = 0
        total_brokerages = 0
    elif(total_brokerages > 0):
        breakeven = round((abs(total_brokerages))/quantity, 2)
    else:
        breakeven = "Calc Err"

    # print(f"Turnover is {turnover} \nBrokerage is {brokerage} \nstt is {stt} \nexchange txn is {exchange_txn_charge} \ngst is {gst} \nsebi is {sebi} \nstamp is {stamp} \nTotal charges is {total_brokerages} \nFinal pnl is {total_pnl} \nBreakeven is {breakeven}")
    arr = [total_brokerages, total_pnl, breakeven]

    return arr


price = 45000
trigger = 45020
sl = abs(price-trigger)
lot = 50


arr = brokerageCalc(price,price,lot)
print("SL is : ",sl)
print("Brokerage is : ",arr[0])
print("Risk is : ", lot*sl)
total_cap = arr[0] + (lot * sl)
print("Max loss : ",total_cap)
print("breakeven : ", arr[2])
