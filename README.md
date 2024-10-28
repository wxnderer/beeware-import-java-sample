# Java Date Example with BeeWare

This project demonstrates how to call a Java method from a BeeWare application using Chaquopy. It provides a simple example of getting the current date and time from Java's java.util.Date class and displaying it in a BeeWare UI.

## How it Works

### Java Native Date Integration

The `date.py` file contains a Python function `call_java_method()` that uses `jclass` from the `java` module (provided by Chaquopy) to:

1. Import the `java.util.Date` class.
2. Create an instance of `Date`.
3. Call the `toString()` method to get the current date and time as a string.
4. Return the result.

### ONNX Runtime Integration

The `onnx.py` file demonstrates how to integrate ONNX Runtime with Java using Chaquopy. Here's how it works:

1. It imports the `jclass` function from the `java` module provided by Chaquopy.
2. The `get_onnxruntime_version()` function:
   - Uses `jclass` to import the `ai.onnxruntime.OrtEnvironment` Java class.
   - Gets the ONNX Runtime environment using `OrtEnvironment.getEnvironment()`.
   - Retrieves the version of ONNX Runtime using `env.getVersion()`.
   - Returns the version string.

### Configuration in pyproject.toml

To use ONNX Runtime with Java in your BeeWare project, you need to add the following configuration to your `pyproject.toml` file:


[tool.briefcase.app.javaimporttest.android]
build_gradle_dependencies = [
    "com.microsoft.onnxruntime:onnxruntime-android:1.19.2"
]


This configuration:

- Adds the ONNX Runtime Android library as a Gradle dependency.

Make sure to replace "javaimporttest" with your actual application name in the configuration.

By adding these configurations, you enable your BeeWare application to use ONNX Runtime's Java API through Chaquopy, allowing you to leverage machine learning models in your cross-platform Python application.

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
