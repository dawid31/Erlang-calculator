#Tu znajduje się logika odpowiedzialna za interfejs graficzny aplikacji

import kivy
from kivy.app import App
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


class MyGridLayout(GridLayout):
    def __init__(self, **kwargs):
        super(MyGridLayout, self).__init__(**kwargs)
        self.cols = 1
        self.orientation = 'tb-lr'


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

        self.intensity_label = Label(text="Intensywność zgłoszeń (w erlangach):", font_size=40)
        self.add_widget(self.intensity_label)

        # self.image = Image(source="arrow-down.png")
        # self.add_widget(self.image)

        self.intensity = TextInput(multiline=False, size_hint=(0.3, None), height=40)
        self.add_widget(self.intensity)

        self.channels_label = Label(text="Liczba kanałów:", font_size=40)
        self.add_widget(self.channels_label)

        self.channels = TextInput(multiline=False, size_hint=(0.3, None), height=40)
        self.add_widget(self.channels)

        self.submit = Button(text="Oblicz", font_size=40)
        self.submit.bind(on_press=self.calculate)
        self.add_widget(self.submit)

        self.result_label = Label(text="Tu pojawi się wynik")
        self.add_widget(self.result_label)


        box_layout = BoxLayout(orientation='horizontal', size_hint=(1, None), height=50)

        # Create the "?" button
        button = Button(text="?", size_hint=(None, None), size=(50, 50))
        button.bind(on_press=partial(self.show_help_popup, "xd"))
        box_layout.add_widget(button)

        # Add the box layout to the main layout
        self.add_widget(box_layout)

    def show_help_popup(self, label_text, instance):
        # Define the help messages for each label
        help_messages = {
            "Tryb:": "Wybierz co chcesz policzyć?",
            "Co powinno być w tym polu?": "Podaj intensywność zgłoszeń w erlangach.",
            "Liczba kanałów:": "Podaj liczbę kanałów."
        }

        # Retrieve the help message based on the label text
        help_message = "tutaj bedzie zawartosc insturkcji kiedys :D"

        # Create and open a popup window with the help message
        popup_content = BoxLayout(orientation='vertical', padding=10)
        popup_content.add_widget(Label(text=help_message))
        popup = Popup(title="Pomoc", content=popup_content, size_hint=(None, None), size=(400, 200))
        popup.open()

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