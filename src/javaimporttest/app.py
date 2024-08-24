"""
Java Import Test Application
"""

import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW

class javaImportTest(toga.App):
    def startup(self):
        """Construct and show the Toga application."""
        main_box = toga.Box(style=Pack(direction=COLUMN))

        # Create a button to trigger the Java method call
        button = toga.Button(
            'Get Current Date/Time',
            on_press=self.call_java_method,
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

    def call_java_method(self, widget):
        """Call a Java method and display the result."""
        try:
            # Import the Java class using Chaquopy
            from java import jclass
            
            # Use java.util.Date class
            Date = jclass('java.util.Date')
            
            # Create an instance of Date
            date_instance = Date()
            
            # Call the toString method to get the current date and time
            result = date_instance.toString()
            
            # Update the UI with the result
            self.result_label.text = f"Current date and time: {result}"
        except Exception as e:
            self.result_label.text = f"Error: {str(e)}"

def main():
    return javaImportTest()
