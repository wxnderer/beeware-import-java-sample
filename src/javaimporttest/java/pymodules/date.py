def call_java_method():
    """Call a Java method and display the result."""

    # Import the Java class using Chaquopy
    from java import jclass
    
    # Use java.util.Date class
    Date = jclass('java.util.Date')
    
    date_instance = Date()
    
    # Call the toString method to get the current date and time
    result = date_instance.toString()
    return result


