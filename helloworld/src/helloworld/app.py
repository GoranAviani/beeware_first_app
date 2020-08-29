"""
My first application
"""
import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW



class HelloWorld(toga.App):

    def startup(self):
        """
        Construct and show the Toga application.

        Usually, you would add your application to a main content box.
        We then create a main window (with a name matching the app), and
        show the main window.
        """
        main_box = toga.Box(style=Pack(direction=COLUMN))
        self.hello_label = toga.Label(
            'hi! ',
            style=Pack(padding=(0, 5))
        )

        name_label = toga.Label(
            'Your text: ',
            style=Pack(padding=(0, 5))
        )
        self.name_input = toga.TextInput(style=Pack(flex=1))

        self.hello_box = toga.Box()
        self.hello_box.add(self.hello_label)

        name_box = toga.Box(style=Pack(direction=ROW, padding=5))
        name_box.add(name_label)
        name_box.add(self.name_input)

        button = toga.Button(
            'Say Hello!',
            on_press=self.say_hello,
            style=Pack(padding=5)
        )

        main_box.add(self.hello_box)
        main_box.add(name_box)
        main_box.add(button)

        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = main_box
        self.main_window.show()

    def say_hello(self, widget):
        print("Hello", self.name_input.value)
        self.hello_label.text = "Hello {}!".format(self.name_input.value)

def main():
    return HelloWorld()
