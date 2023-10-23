ERRORS AND EXCEPTIONS IN PYTHON:
1. WHAT'S THE DIFFERENCE BETWEEN ERRORS AND EXCEPTIONS
In Python, both errors and exceptions represent different types of problems that can occur during program execution. Here's a summary of their differences:

- **Errors**: Errors in Python are problems in a program due to which the program will stop the execution¹. They represent conditions such as compilation error, syntax error, error in the logical part of the code, library incompatibility, infinite recursion, etc⁴. Errors are usually beyond the control of the programmer and we should not try to handle errors⁴. For example, when the proper syntax of the language is not followed then a syntax error is thrown¹.

- **Exceptions**: Exceptions in Python are raised when some internal events occur which changes the normal flow of the program¹. They occur at runtime, when the code is executed³. Exceptions are errors that are discovered during the execution of a program¹. Exceptions occur when the code tries to perform an invalid operation, such as dividing by zero or accessing an invalid variable³. Exceptions can be caught and handled by the program⁴.

Here's an example of how to handle exceptions with `try/except/finally` in Python:

```python
try:
    print("code start")
    print(1 / 0)
except:
    print("an error occurs")
finally:
    print("GeeksForGeeks")
```

In this example, a `ZeroDivisionError` exception is raised when we try to divide a number by 0. The `try` block contains code that might throw an exception. If that exception occurs, the code in the `try` block stops being executed, and the code in the `except` block is run. The `finally` block contains code that is always executed, whether an exception has occurred or not¹.

2.WHAT ARE EXCEPTIONS AND HOW TO USE THEM;
Exceptions are events that occur during the execution of programs that disrupt the normal flow of instructions¹. They are used to handle errors that can be recovered from within the program¹. Here are some basic guidelines and best practices for using exceptions:

a. **Use asserts to check for errors** that should never occur¹.
b. **Use exceptions when the code** that handles the error is separated from the code that detects the error by one or more intervening function calls¹.
c. For every function that might throw or propagate an exception, provide one of the three exception guarantees: the strong guarantee, the basic guarantee, or the nothrow (noexcept) guarantee¹.
d. **Use try/catch/finally blocks** to recover from errors or release resources¹.
e. Handle common conditions without throwing exceptions¹.
f. Design classes so that exceptions can be avoided¹.
g. Throw exceptions instead of returning an error code¹.
h. Use the predefined .NET exception types¹.
i. End exception class names with the word Exception¹.
j. Include three constructors in custom exception classes¹.

Here's an example of how to handle exceptions in Python:

```python
try:
    # Code start
    print(1 / 0)
except:
    # An error occurs
    print("An error occurred")
finally:
    # Always executed
    print("End of code")
```

In this example, a `ZeroDivisionError` exception is raised when we try to divide a number by 0. The `try` block contains code that might throw an exception. If that exception occurs, the code in the `try` block stops being executed, and the code in the `except` block is run. The `finally` block contains code that is always executed, whether an exception has occurred or not¹.

3. WHEN DO WE NEED TO USE EXCEPTIONS?
In Python, exceptions are used to handle unexpected events that occur during the execution of a program¹. Here are some scenarios when we need to use exceptions:

a. **Unpredictable Errors**: Exceptions are used when an error occurs that the program cannot predict or prevent¹. For example, if a file that the program needs to read does not exist, an exception is thrown¹.

b. **Error Propagation**: If an error occurs in a method, it might not be appropriate or possible for the method to handle the error itself. Instead, the method can throw an exception to indicate that an error has occurred. The method's caller can then catch the exception and handle it appropriately¹.

c. **Grouping and Differentiating Error Types**: Exceptions allow you to differentiate between different types of errors. You can create different classes of exceptions for different error conditions¹.

d. **Cleaner Code**: Using exceptions can make your code cleaner and easier to understand. Without exceptions, you would need to use error codes and checks that could clutter up your code¹.

e. **Resource Cleanup**: When an exception is thrown, it often means that some resource has not been properly cleaned up (like a file being left open). The `finally` block in a `try-catch-finally` statement allows you to ensure resources are cleaned up¹.

Remember, exceptions should not be used for normal flow control in your program, but only for actual error conditions¹. Also, creating and throwing exceptions has a high computational cost, so they should be used sparingly¹.

4.HOW TO CORRECTLY HANDLE AN EXCEPTION;
In Python, exceptions are handled using `try`, `except`, and `finally` statements¹². Here's how you can correctly handle an exception:

```python
try:
    # Code that may cause an exception
    print(1 / 0)
except Exception as e:
    # Code to run when an exception occurs
    print(f"An exception occurred: {e}")
finally:
    # Code that is always executed, whether an exception occurred or not
    print("End of code")
```

In this example, a `ZeroDivisionError` exception is raised when we try to divide a number by 0¹. The `try` block contains code that might throw an exception. If that exception occurs, the code in the `try` block stops being executed, and the code in the `except` block is run. The `finally` block contains code that is always executed, whether an exception has occurred or not¹.

It's important to handle exceptions properly in your code using try-except blocks or other error-handling techniques, in order to gracefully handle errors and prevent the program from crashing².

5. WHAT IS THE PURPOSE OF CATCHING EXCEPTIONS?
Catching exceptions in Python serves several important purposes:

a. **Error Handling**: Catching exceptions allows a program to handle error conditions and prevent the program from crashing. It enables the program to take appropriate action or provide a useful message when an error occurs¹.

b. **Flow Control**: Exceptions alter the flow of control in a program. When an exception is thrown, the normal flow of the program is interrupted, and control is transferred to an exception handler². This allows the program to continue executing even after an error has occurred¹.

c. **Resource Cleanup**: The `finally` block in a `try/except/finally` statement allows you to ensure resources are cleaned up, regardless of whether an exception was thrown¹. This is useful for releasing resources like file handles or network connections².

d. **Debugging and Logging**: Catching exceptions can also help with debugging, as it allows you to log errors and exception information, which can be useful for understanding and fixing problems¹.

Here's an example of how to catch exceptions in Python:

```python
try:
    # Code that may raise an exception
    x = 1 / 0
except ZeroDivisionError as e:
    # Handle the exception
    print(f"Caught an exception: {e}")
```

In this code, if the operation in the `try` block raises a `ZeroDivisionError`, the `except` block will catch it and print a message¹.

6. HOW TO RAISE A BUILTIN EXCEPTION;
In Python, you can raise a built-in exception using the `raise` keyword¹⁷. The `raise` keyword is followed by the name of the exception you want to raise¹⁷. Here's an example:

```python
try:
    # Code that may cause an exception
    raise ValueError("A value error has occurred")
except ValueError as e:
    # Handle the exception
    print(f"Caught an exception: {e}")
```

In this code, a `ValueError` exception is manually raised inside the `try` block. The `except` block catches the `ValueError` exception and prints a message¹⁷.

Remember, user code can raise built-in exceptions⁴. This can be used to test an exception handler or to report an error condition⁴. However, be aware that there is nothing to prevent user code from raising an inappropriate error⁴.

7.WHEN DO WE NEED TO IMPLEMENT A CLEAN-UP ACTION AFTER EXCEPTION?
In Python, clean-up actions are implemented after an exception to ensure that certain necessary tasks are always performed before the program continues execution or terminates, regardless of whether an error occurred². Here are some scenarios when you might need to implement a clean-up action:

1. **Resource Management**: If your program has opened a file, established a network connection, or acquired some other resource, you should ensure these resources are properly released even if an error occurs³. This is typically done in a `finally` block².

2. **State Reset**: If an exception occurs during the execution of a block of code, the program's state may need to be reset (variables might need to be reinitialized, data structures might need to be cleared, etc.)¹.

3. **Error Logging**: If your program logs errors or other information, you might want to ensure that all logging is properly flushed and all log files are closed¹.

Here's an example of how to implement a clean-up action in Python:

```python
try:
    # Code that may raise an exception
    file = open("file.txt", "r")
except IOError as e:
    # Handle the exception
    print(f"Caught an exception: {e}")
finally:
    # Clean-up action
    file.close()
```

In this code, the `finally` block ensures that the file is closed whether an exception occurred or not².

