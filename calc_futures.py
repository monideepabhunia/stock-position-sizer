def FuturesBrokerageCalc(price, sl, quantity=50):
    buy = price
    sell = price
    turnover = (buy+sell)*quantity
    brokerage = 40
    stt = round(((sell*quantity)*(0.01))/100, 2)
    exchange_txn_charge = round((turnover*0.002)/100, 2)
    gst = round((brokerage+exchange_txn_charge)*0.18, 2)
    sebi = round((10/10000000)*turnover, 2)
    stamp = round((0.002*(buy*quantity)/100), 2) if (buy *
                                                     quantity) < 10000000 else 200

    total_brokerages = round(brokerage +
                             stt+exchange_txn_charge+gst+sebi+stamp, 2)

    breakeven = round((abs(total_brokerages))/quantity, 2)
    risk = round(total_brokerages + (sl * quantity), 2)

    arr = [total_brokerages, breakeven, risk]
    return arr


# arr = FuturesBrokerageCalc(17000, 10)
# print("Risk : {}".format(str(arr[2])))
# print("breakeven : {}".format(str(arr[1])))
# print("Brokerage is : {}".format(str(arr[0])))
