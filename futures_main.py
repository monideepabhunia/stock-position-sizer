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
        Window.size = (400, 151)  # TODO: decrease it to lower the height

        self.top_grid = GridLayout(
            row_force_default=True, row_default_height=ht, col_force_default=True, col_default_width=wdth)
        self.top_grid.cols = 2

        self.top_grid.add_widget(
            Label(text="Lot Size", font_size=fontSize))
        self.lotSize = TextInput(multiline=False)
        self.top_grid.add_widget(self.lotSize)
        self.lotSize.text = '50'

        self.top_grid.add_widget(
            Label(text="Price", font_size=fontSize))
        self.price = TextInput(multiline=False)
        self.top_grid.add_widget(self.price)
        # self.price.text = "700"

        self.top_grid.add_widget(
            Label(text="SL Difference", font_size=fontSize))
        self.sl = TextInput(multiline=False)
        self.top_grid.add_widget(self.sl)
        # self.sl.text = ""

        self.top_grid.add_widget(
            Label(text="Risk Amount (Rs.)", font_size=fontSize))
        self.risk = TextInput(multiline=False)
        self.top_grid.add_widget(self.risk)
        # self.risk.text = ""

        self.top_grid.add_widget(Label(text="Result", font_size=fontSize))
        self.result = TextInput(multiline=False)
        self.top_grid.add_widget(self.result)
        # self.result.text = ""
        # TODO: If sending msg in telegram not wanted by default, change below => state='down' --> state='normal'
        # sendTEleButton = ToggleButton(text="Send to Telegram", state='down')
        # sendTEleButton = ToggleButton(text="Send to Telegram", state='normal')
        # self.top_grid.add_widget(sendTEleButton)
        # sendTEleButton.bind(on_press=self.sendTelegram)

        self.add_widget(self.top_grid)

        self.Calculate = Button(
            text="Calculate", font_size=fontSize, size_hint_y=None, height=ht, size_hint_x=None, width=wdth)
        self.Calculate.bind(on_press=self.press)
        self.add_widget(self.Calculate)

    def press(self, instance):
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

        try:
            price = int(self.price.text)
            sl = int(self.sl.text)+1
            lotSize = int(self.lotSize.text)

            arr = FuturesBrokerageCalc(price, sl, lotSize)
            # arr = [total_brokerages, breakeven, risk] ### result format of above array
            self.risk.text = str(arr[2])
            self.result.text = "Breakeven : {}".format(str(arr[1]))
        except Exception as e:
            print(e)
            result = "Try again"
            self.result.text = result


class StockQuantityCalculator(App):
    def build(self):
        return MyGridLayout()


StockQuantityCalculator().run()
