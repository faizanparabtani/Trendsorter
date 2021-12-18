from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.graphics import Rectangle, Color

# MD
from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.datatables import MDDataTable
from kivy.metrics import dp
from kivymd.uix.label import MDLabel

# from scraper import searchtrends


class TrendSort(MDApp):
    def build(self):
        screen = Screen()
        self.window = GridLayout()
        self.window.cols = 3
        self.window.rows = 3
        self.window.size_hint = (0.6, 0.7)
        self.window.pos_hint = {"center_x": 0.5, "center_y":0.5}

        """
        Datatable
        """
        table = MDDataTable(
            pos_hint = {'center_x':0.5, 'center_y':0.5},
            size_hint = (0.9, 0.6),
            column_data=[
            ("Results", dp(30)),
            ("Popularity", dp(30)),
            ("Tag", dp(40)),
            ("Link", dp(30)),
            ]

        )

        screen.add_widget(table)

        """
        Text Labels
        """
        # App name
        self.appname = MDLabel(
                        text = "Redbubble Trend Scraper",
                        font_size = 18,
                        color = '#00FFCE'
                        )
        screen.add_widget(self.appname)

        # Current Search Criteria
        self.current_criteria = Label(
                        text = "Current Criteria",
                        font_size = 18,
                        color = '#00FFCE'
                        )
        self.window.add_widget(self.current_criteria)

        # New Search Criteria
        self.new_criteria = Label(
                        text = "New Criteria(Optional)",
                        font_size = 18,
                        color = '#00FFCE'
                        )
        self.window.add_widget(self.new_criteria)

        # Dev
        self.faizan = Label(
                        text = "Made by Faizan Parabtani",
                        font_size = 18,
                        color = '#00FFCE'
                        )
        self.window.add_widget(self.faizan)

        """
        Text Inputs

        """
        # Results Lower Bound
        self.results_lower = TextInput(
                    multiline= False,
                    padding_y= (20,20),
                    size_hint= (1, 0.5)
                    )
        self.window.add_widget(self.results_lower)
        # Results Higher Bound
        self.results_higher = TextInput(
                    multiline= False,
                    padding_y= (20,20),
                    size_hint= (1, 0.5)
                    )
        self.window.add_widget(self.results_higher)

        # Popularity Lower Bound
        self.popularity_lower = TextInput(
                    multiline= False,
                    padding_y= (20,20),
                    size_hint= (1, 0.5)
                    )
        self.window.add_widget(self.popularity_lower)
        # Popularity Higher Bound
        self.popularity_higher = TextInput(
                    multiline= False,
                    padding_y= (20,20),
                    size_hint= (1, 0.5)
                    )
        self.window.add_widget(self.popularity_higher)

        # button widget
        self.button = Button(
                      text= "Go!",
                      size_hint= (1,0.5),
                      bold= True,
                      background_color ='#00FFCE',
                      #remove darker overlay of background colour
                      # background_normal = ""
                      )
        # self.button.bind(on_press=searchtrends)
        self.window.add_widget(self.button)


        return screen

        # def callback(self, instance):
        #     # change label text to "Hello + user name!"
        #     self.greeting.text = "Hello " + self.user.text + "!"


if __name__ == '__main__':
    TrendSort().run()
