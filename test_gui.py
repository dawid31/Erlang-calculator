from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label

class MyLayout(BoxLayout):
    def __init__(self, **kwargs):
        super(MyLayout, self).__init__(**kwargs)
        
        # Set padding for the BoxLayout
        self.padding = (10, 10, 10, 10)  # (left, top, right, bottom)
        
        # Create a GridLayout inside the BoxLayout
        grid_layout = GridLayout(cols=2, spacing=10)
        grid_layout.padding = (10, 10, 10, 10)  # (left, top, right, bottom)
        
        # Add labels to the GridLayout
        for i in range(4):
            label = Label(text=f"Label {i+1}")
            grid_layout.add_widget(label)
        
        # Add the GridLayout to the BoxLayout
        self.add_widget(grid_layout)

class MyApp(App):
    def build(self):
        return MyLayout()

if __name__ == '__main__':
    MyApp().run()