from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from instruction import instruction_text_1, instruction_text_2

def display_value_error():
    value_error_message = '''Podano nieprawidlowe wartosci w polu/polach.
    Sprawdz w instrukcji w lewym dolnym rogu co poszlo nie tak.'''
    popup_content = BoxLayout(orientation='vertical', padding=10)
    popup_content.add_widget(Label(text=value_error_message))
    popup = Popup(title="Podano nieprawidlowe wartosci", content=popup_content, size_hint=(None, None), size=(600, 300))
    popup.open()

