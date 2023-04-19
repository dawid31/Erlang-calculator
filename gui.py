#Tu znajduje się logika odpowiedzialna za interfejs graficzny aplikacji

import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.spinner import Spinner
from erlang import calculate_erlang_a, calculate_erlang_b, calculate_erlang_n

class MyGridLayout(GridLayout):
    def __init__(self, **kwargs):
        super(MyGridLayout, self).__init__(**kwargs)
        self.cols = 2

        # Create the input fields and labels
        self.mode_label = Label(text="Tryb:")
        self.add_widget(self.mode_label)

        self.mode_spinner = Spinner(
            text="Wybierz co chcesz policzyć?",
            values=["Natężenie ruchu work in progress :)", "Współczynnik blokady", "Ilość linii/kanałów"],
            size_hint=(None, None),
            size=(250, 44)
        )
        self.mode_spinner.bind(text=self.update_input_labels)
        self.add_widget(self.mode_spinner)

        self.intensity_label = Label(text="Intensywność zgłoszeń (w erlangach):")
        self.add_widget(self.intensity_label)

        self.intensity = TextInput(multiline=False)
        self.add_widget(self.intensity)

        self.channels_label = Label(text="Liczba kanałów:")
        self.add_widget(self.channels_label)

        self.channels = TextInput(multiline=False)
        self.add_widget(self.channels)

        self.submit = Button(text="Oblicz", font_size=40)
        self.submit.bind(on_press=self.calculate)
        self.add_widget(self.submit)

        self.result_label = Label(text="Tu pojawi się wynik")
        self.add_widget(self.result_label)


    def update_input_labels(self, instance, value):
        # Update the labels of the input fields depending on the selected mode
        if value == "Natężenie ruchu work in progress :)":
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
        if mode == 'Natężenie ruchu work in progress :)':
            #field1 = int(self.intensity.text)
            #field2 = float(self.channels.text)
            #result = calculate_erlang_a(field1, field2) doesnt do anything yet
            self.result_label.text = "W trakcie implementacji"

        elif mode == 'Współczynnik blokady':
            field1 = float(self.intensity.text)
            field2 = int(self.channels.text)
            result = calculate_erlang_b(field1, field2) 
            self.result_label.text = str(round(float(result), 5))


        elif mode == 'Ilość linii/kanałów':
            field1 = float(self.intensity.text)
            field2 = float(self.channels.text)
            result = calculate_erlang_n(field1, field2)
            self.result_label.text = str(round(float(result), 5))

class ErlangCalculator(App):
    def build(self):
        return MyGridLayout()