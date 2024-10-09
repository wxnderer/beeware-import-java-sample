"""
Java Import Test Application
"""

import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW
from .java.pymodules.date import call_java_method

class javaImportTest(toga.App):
    def startup(self):
        """Construct and show the Toga application."""
        main_box = toga.Box(style=Pack(direction=COLUMN))

        # Create a button to trigger the Java method call
        button = toga.Button(
            'Get Current Date/Time',
            on_press=self.set_time,
            style=Pack(padding=5)
        )

        # Create a label to display the result
        self.result_label = toga.Label(
            'Date/Time will appear here',
            style=Pack(padding=5)
        )

        main_box.add(button)
        main_box.add(self.result_label)

        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = main_box
        self.main_window.show()
    def set_time(self, widget):
        result = call_java_method()        
        self.result_label.text = f"Current date and time: {result}"
    

def main():
    return javaImportTest()
