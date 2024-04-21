import credentials
import requests
import pyperclip
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.core.window import Window  # needed to change window size
from kivy.uix.togglebutton import ToggleButton

global fontSize, ht, wdth
fontSize = 18
ht = 30
wdth = 200
chat_id = credentials.chat_id
apikey = credentials.api_key
# TODO: Line 72 change default telegram sending msg and also in Line 30


class MyGridLayout(GridLayout):
    def __init__(self, **kwargs):
        super(MyGridLayout, self).__init__(**kwargs)
        self.cols = 1
        # self.col_force_default = True
        # self.col_default_width = wdth
        # Changing app launch window size

        self.buysell_toggle = 0
        self.sendTele = 0
        Window.size = (400, 180)

        self.top_grid = GridLayout(
            row_force_default=True, row_default_height=ht, col_force_default=True, col_default_width=wdth)
        self.top_grid.cols = 2

        self.top_grid.add_widget(
            Label(text="Risk Amount (Rs.)", font_size=fontSize))
        self.risk = TextInput(multiline=False)
        self.top_grid.add_widget(self.risk)
        self.risk.text = "1500"

        btn1 = ToggleButton(text="Buy", group="buy_sell")
        btn2 = ToggleButton(text="Sell", group="buy_sell")
        self.top_grid.add_widget(btn1)
        self.top_grid.add_widget(btn2)
        btn1.bind(on_press=self.buytoggled)
        btn2.bind(on_press=self.selltoggled)

        self.top_grid.add_widget(
            Label(text="SL Difference", font_size=fontSize))
        self.sl = TextInput(multiline=False)
        self.top_grid.add_widget(self.sl)
        self.sl.text = "5"

        self.top_grid.add_widget(
            Label(text="Price", font_size=fontSize))
        self.price = TextInput(multiline=False)
        self.top_grid.add_widget(self.price)
        # self.price.text = "700"

        self.top_grid.add_widget(
            Label(text="Trigger Price", font_size=fontSize))
        self.triggerprice = TextInput(multiline=False)
        self.top_grid.add_widget(self.triggerprice)
        # self.triggerprice.text = "750"

        self.top_grid.add_widget(Label(text="Result", font_size=fontSize))
        self.result = TextInput(multiline=False)
        self.top_grid.add_widget(self.result)
        # TODO: If sending msg in telegram not wanted by default, change below => state='down' --> state='normal'
        # sendTEleButton = ToggleButton(text="Send to Telegram", state='down')
        sendTEleButton = ToggleButton(text="Send to Telegram", state='normal')
        self.top_grid.add_widget(sendTEleButton)
        sendTEleButton.bind(on_press=self.sendTelegram)

        self.add_widget(self.top_grid)

        self.Calculate = Button(
            text="Quantity", font_size=fontSize, size_hint_y=None, height=ht, size_hint_x=None, width=wdth)
        self.Calculate.bind(on_press=self.press)
        self.add_widget(self.Calculate)

    def sendTelegram(self, instance):
        if(self.sendTele == 1):
            self.sendTele = 0
        else:
            self.sendTele = 1

    def buytoggled(self, instance):
        self.buysell_toggle = 1

    def selltoggled(self, instance):
        self.buysell_toggle = -1

    def press(self, instance):
        buy_sell = self.buysell_toggle

        def sendcopy(w, x, y):
            url1 = "https://api.telegram.org/bot" + apikey + \
                "/sendMessage?chat_id=" + chat_id + "&text="+"-----------------"
            url2 = "https://api.telegram.org/bot" + apikey + \
                "/sendMessage?chat_id=" + chat_id + "&text=`"+w+"`&parse_mode=MARKDOWN"
            url3 = "https://api.telegram.org/bot" + apikey + \
                "/sendMessage?chat_id=" + chat_id + "&text=`"+x+"`&parse_mode=MARKDOWN"
            url4 = "https://api.telegram.org/bot" + apikey + \
                "/sendMessage?chat_id=" + chat_id + "&text=`"+y+"`&parse_mode=MARKDOWN"
            # time.sleep(5)
            r1 = requests.get(url1)
            r2 = requests.get(url2)
            r3 = requests.get(url3)
            r4 = requests.get(url4)
            print("Messages Sent")

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

        # sellPrice = self.sell.text
        # buyPrice = self.buy.text
        price = self.price.text
        risk = self.risk.text
        sl = self.sl.text
        result = self.result.text

        try:
            risk = int(risk)
            # sl = abs(int(price) - int(sl))
            sl = int(sl)
            result = int(risk//sl)
            margin = 5  # TODO: margin 5x
            # arr = brokerageCalc(buyPrice, sellPrice, result)
            arr = brokerageCalc(price, price, result)
            if(int(arr[0]) != 0):
                risk = risk - int(arr[0])
                if (int(risk//sl) > 0):
                    # result = str(int(risk//sl)) + "   BE:" + str(arr[2])
                    result = str(int(risk//sl)) + "   BE:" + \
                        str(arr[2]) + "   M:" + \
                        str(round(((risk//sl)*int(float(price)))/500000, 3)) + "L"

                    if(buy_sell == 1):
                        # buy bcz buy_sell is 1, so SL trigger is lower
                        trigger = float(price)-float(sl)
                    elif(buy_sell == -1):
                        # sell bcz buy_sell is 0, so SL trigger is higher
                        trigger = float(price) + float(sl)
                    else:
                        trigger = 0
                    print(f"\nPrice is : {price}")
                    print(f"Trigger is : {trigger}")
                    self.triggerprice.text = str(trigger)
                    if(self.sendTele == 1):
                        sendcopy(str(int(risk//sl)), str(price), str(trigger))
                    pyperclip.copy(price)
                else:
                    #     # print breakeven
                    # result = "Need More Risk.  Breakeven : " + str(arr[2])
                    result = "Need More Risk"

                self.result.text = str(result)
            else:
                result = "Try again Above"
        except Exception as e:
            print(e)
            result = "Try again"
            self.result.text = result


class StockQuantityCalculator(App):
    def build(self):
        return MyGridLayout()


StockQuantityCalculator().run()
