#Tu znajduje się logika odpowiedzialna za interfejs graficzny aplikacji

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.spinner import Spinner
from erlang import calculate_erlang_a, calculate_erlang_b, calculate_erlang_n
from functools import partial
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivy.uix.image import Image
from instruction import instruction_text
from kivy.uix.slider import Slider
from plot import plot_graph
from utilities import display_value_error


class MainScreen(Screen):
    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)
        self.layout = GridLayout(cols=1, orientation='tb-lr')

        self.mode_spinner = Spinner(
            text="Wybierz co chcesz policzyć?",
            values=["Natężenie ruchu", "Współczynnik blokady", "Ilość linii/kanałów"],
            size_hint=(None, None),
            size=(250, 44)
        )
        self.mode_spinner.bind(text=self.update_input_labels)
        self.layout.add_widget(self.mode_spinner)

        self.intensity_label = Label(text="Intensywność zgłoszeń (w erlangach):", font_size=40)
        self.layout.add_widget(self.intensity_label)

        self.intensity = TextInput(multiline=False, size_hint=(0.3, None), height=40)
        self.layout.add_widget(self.intensity)

        self.channels_label = Label(text="Liczba kanałów:", font_size=40)
        self.layout.add_widget(self.channels_label)

        self.channels = TextInput(multiline=False, size_hint=(0.3, None), height=40)
        self.layout.add_widget(self.channels)

        self.submit = Button(text="Oblicz", font_size=40)
        self.submit.bind(on_press=self.calculate)
        self.layout.add_widget(self.submit)

        self.result_label = Label(text="Tu pojawi się wynik", font_size=40)
        self.layout.add_widget(self.result_label)

        box_layout = BoxLayout(orientation='horizontal', size_hint=(1, None), height=50)
        self.layout.add_widget(box_layout)

        button = Button(text="Go to Second Screen", size_hint=(None, None), size=(200, 50))
        button.bind(on_press=self.goto_second_screen)

        box_layout.add_widget(button)
        self.add_widget(self.layout)


    def goto_second_screen(self, instance):
        self.manager.current = 'second'

    def update_input_labels(self, instance, value):
        if value == "Natężenie ruchu":
            self.intensity_label.text = "Ilość linii:"
            self.channels_label.text = "Współczynnik blokady:"
        elif value == "Współczynnik blokady":
            self.intensity_label.text = "Intensywność zgłoszeń (w erlangach):"
            self.channels_label.text = "Liczba kanałów/linii:"
        elif value == "Ilość linii/kanałów":
            self.intensity_label.text = "Intensywność zgłoszeń (w erlangach)"
            self.channels_label.text = "Współczynnik blokady:"


    def calculate(self, instance):
        # Define the function that will be called when the Run button is pressed
        mode = self.mode_spinner.text
        if mode == 'Natężenie ruchu':
            try:
                field1 = int(self.intensity.text)
                field2 = float(self.channels.text)
                result = calculate_erlang_a(field1, field2) 
                self.result_label.text = f"{mode}: {str(round(float(result), 5))}"
            except ValueError:
                display_value_error()

        elif mode == 'Współczynnik blokady':
            try:
                field1 = float(self.intensity.text)
                field2 = int(self.channels.text)
                result = calculate_erlang_b(field1, field2) 
                self.result_label.text = f"{mode}: {str(round(float(result), 5))}"
            except ValueError:
                display_value_error()

        elif mode == 'Ilość linii/kanałów':
            try:
                field1 = float(self.intensity.text)
                field2 = float(self.channels.text)
                result = calculate_erlang_n(field1, field2)
                self.result_label.text = f"{mode}: {str(round(float(result), 5))}"
            except ValueError:
                display_value_error()


class SecondScreen(Screen):
    def __init__(self, **kwargs):

        super(SecondScreen, self).__init__(**kwargs)
        self.layout = GridLayout(cols=1, orientation='tb-lr')

        # Mode label
        self.mode_label = Label(
            text="Szkicowanie wykresu wsp. blokady \n dla wybranego przedziału:",
            font_size=40)
        self.layout.add_widget(self.mode_label)
        self.add_widget(self.layout)

        self.start_value_label = Label(text="Wartość początkowa")
        self.layout.add_widget(self.start_value_label)
        self.start_value = TextInput(multiline=False, size_hint=(0.3, None), height=40)
        self.layout.add_widget(self.start_value)

        self.end_value_label = Label(text="Wartość końcowa")
        self.layout.add_widget(self.end_value_label)
        self.end_value = TextInput(multiline=False, size_hint=(0.3, None), height=40)
        self.layout.add_widget(self.end_value)

        self.plot = Button(text="Pokaz wykres", font_size=40,)
        self.plot.bind(on_press=self.plot_graph_callback)
        self.layout.add_widget(self.plot)

        # Going back to the main screen part of GUI
        button = Button(text="Go to Main Screen", size_hint=(None, None), size=(200, 50))
        button.bind(on_press=self.goto_main_screen)
        self.layout.add_widget(button)

    
    def plot_graph_callback(self, instance):
        try:
            start = float(self.start_value.text)
            end = float(self.end_value.text)
            plot_graph(start, end)  
        except ValueError:
            display_value_error()
    

    def goto_main_screen(self, instance):
        self.manager.current = 'main'
        

class ErlangCalculatorApp(App):
    def build(self):
        screen_manager = ScreenManager()
        screen_manager.add_widget(MainScreen(name='main'))
        screen_manager.add_widget(SecondScreen(name='second'))
        return screen_manager

