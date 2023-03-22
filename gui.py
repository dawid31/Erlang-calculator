#Tu znajduje się logika odpowiedzialna za interfejs graficzny aplikacji

import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from erlang import erlang_b

class MyGridLayout(GridLayout):
    def __init__(self, **kwargs):
        super(MyGridLayout, self).__init__(**kwargs)

        self.cols = 2

        self.add_widget(Label(text="Intensywność zgłoszeń (w erlangach):"))
        self.intensity = TextInput(multiline=False)
        self.add_widget(self.intensity)

        self.add_widget(Label(text="Liczba kanałów:"))
        self.channels = TextInput(multiline=False)
        self.add_widget(self.channels)

        self.submit = Button(text="Oblicz", font_size=40)
        self.submit.bind(on_press=self.calculate)
        self.add_widget(self.submit)

        self.result_label = Label(text="Tu pojawi się wynik")
        self.add_widget(self.result_label)

    def calculate(self, instance):
        # Define the function that will be called when the Run button is pressed
        intensity = int(self.intensity.text)
        channels = int(self.channels.text)
        result = erlang_b(intensity, channels)
        self.result_label.text = str(round(result, 5))

class ErlangCalculator(App):
    def build(self):
        return MyGridLayout()