# Java Date Example with BeeWare

This project demonstrates how to call a Java method from a BeeWare application using Chaquopy. It provides a simple example of getting the current date and time from Java's java.util.Date class and displaying it in a BeeWare UI.

## How it Works

### Java Code

The `date.py` file contains a Python function `call_java_method()` that uses `jclass` from the `java` module (provided by Chaquopy) to:

1. Import the `java.util.Date` class.
2. Create an instance of `Date`.
3. Call the `toString()` method to get the current date and time as a string.
4. Return the result.

### BeeWare UI

The `app.py` file defines a simple BeeWare application with a button. When pressed, the button:

1. Calls the `call_java_method()` function from `date.py`.
2. Updates a label in the UI with the returned date and time string.

### Configuration

The `pyproject.toml` file includes the necessary configurations for BeeWare, such as:

- Project metadata (name, version, etc.).
- Dependencies (including BeeWare components).
- Platform-specific settings.

## Running the Example

1. Make sure you have BeeWare installed (`pip install briefcase`).
2. Navigate to the project directory.
3. Run `briefcase dev` to start the development server.
4. You should see a window with a button. Clicking the button will fetch and display the current date and time from Java.

## Key Points

- **Chaquopy**: This project relies on Chaquopy to embed a Python interpreter and enable Java/Python interoperability within the BeeWare Android app.
- **JNI**: While not explicitly used in this example, more complex Java interactions might require using the Java Native Interface (JNI) for bridging.
- **AAR Compatibility**: The current setup is primarily designed for JAR files. Integrating AAR libraries might require additional steps or adjustments.

This example serves as a starting point for incorporating Java functionality into your BeeWare applications. You can expand upon it to call other Java methods, work with different libraries, and build more sophisticated integrations.
