Getting Started With Testing in Python:
Testing Your Code
There are many ways to test your code. In this tutorial, you’ll learn the techniques from the most basic steps and work towards advanced methods.
Automated vs. Manual Testing
The good news is, you’ve probably already created a test without realizing it. Remember when you ran your application and used it for the first time? Did you check the features and experiment using them? That’s known as exploratory testing and is a form of manual testing.

Exploratory testing is a form of testing that is done without a plan. In an exploratory test, you’re just exploring the application.

To have a complete set of manual tests, all you need to do is make a list of all the features your application has, the different types of input it can accept, and the expected results. Now, every time you make a change to your code, you need to go through every single item on that list and check it.

That doesn’t sound like much fun, does it?

This is where automated testing comes in. Automated testing is the execution of your test plan (the parts of your application you want to test, the order in which you want to test them, and the expected responses) by a script instead of a human. Python already comes with a set of tools and libraries to help you create automated tests for your application. We’ll explore those tools and libraries in this tutorial.

Unit Tests vs. Integration Tests
The world of testing has no shortage of terminology, and now that you know the difference between automated and manual testing, it’s time to go a level deeper.

Think of how you might test the lights on a car. You would turn on the lights (known as the test step) and go outside the car or ask a friend to check that the lights are on (known as the test assertion). Testing multiple components is known as integration testing.

Think of all the things that need to work correctly in order for a simple task to give the right result. These components are like the parts to your application, all of those classes, functions, and modules you’ve written.

A major challenge with integration testing is when an integration test doesn’t give the right result. It’s very hard to diagnose the issue without being able to isolate which part of the system is failing. If the lights didn’t turn on, then maybe the bulbs are broken. Is the battery dead? What about the alternator? Is the car’s computer failing?

If you have a fancy modern car, it will tell you when your light bulbs have gone. It does this using a form of unit test.

A unit test is a smaller test, one that checks that a single component operates in the right way. A unit test helps you to isolate what is broken in your application and fix it faster.

You have just seen two types of tests:

An integration test checks that components in your application operate with each other.
A unit test checks a small component in your application.
You can write both integration tests and unit tests in Python. To write a unit test for the built-in function sum(), you would check the output of sum() against a known output.

For example, here’s how you check that the sum() of the numbers (1, 2, 3) equals 6:

>>> assert sum([1, 2, 3]) == 6, "Should be 6"
This will not output anything on the REPL because the values are correct.

If the result from sum() is incorrect, this will fail with an AssertionError and the message "Should be 6". Try an assertion statement again with the wrong values to see an AssertionError:

>>> assert sum([1, 1, 1]) == 6, "Should be 6"
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AssertionError: Should be 6
In the REPL, you are seeing the raised AssertionError because the result of sum() does not match 6.

Instead of testing on the REPL, you’ll want to put this into a new Python file called test_sum.py and execute it again:

def test_sum():
    assert sum([1, 2, 3]) == 6, "Should be 6"

if __name__ == "__main__":
    test_sum()
    print("Everything passed")
Now you have written a test case, an assertion, and an entry point (the command line). You can now execute this at the command line:

$ python test_sum.py
Everything passed
You can see the successful result, Everything passed.

In Python, sum() accepts any iterable as its first argument. You tested with a list. Now test with a tuple as well. Create a new file called test_sum_2.py with the following code:

def test_sum():
    assert sum([1, 2, 3]) == 6, "Should be 6"

def test_sum_tuple():
    assert sum((1, 2, 2)) == 6, "Should be 6"

if __name__ == "__main__":
    test_sum()
    test_sum_tuple()
    print("Everything passed")
When you execute test_sum_2.py, the script will give an error because the sum() of (1, 2, 2) is 5, not 6. The result of the script gives you the error message, the line of code, and the traceback:

$ python test_sum_2.py
Traceback (most recent call last):
  File "test_sum_2.py", line 9, in <module>
    test_sum_tuple()
  File "test_sum_2.py", line 5, in test_sum_tuple
    assert sum((1, 2, 2)) == 6, "Should be 6"
AssertionError: Should be 6
Here you can see how a mistake in your code gives an error on the console with some information on where the error was and what the expected result was.

Note: It’s possible to simultaneously document and test your code, while ensuring that your code and its documentation remain in sync, with doctest. Check out Python’s doctest: Document and Test Your Code at Once to learn more.

Writing tests in this way is okay for a simple check, but what if more than one fails? This is where test runners come in. The test runner is a special application designed for running tests, checking the output, and giving you tools for debugging and diagnosing tests and applications.
Choosing a Test Runner
There are many test runners available for Python. The one built into the Python standard library is called unittest. In this tutorial, you will be using unittest test cases and the unittest test runner. The principles of unittest are easily portable to other frameworks. The three most popular test runners are:

unittest
nose or nose2
pytest
Choosing the best test runner for your requirements and level of experience is important.

unittest
unittest has been built into the Python standard library since version 2.1. You’ll probably see it in commercial Python applications and open-source projects.

unittest contains both a testing framework and a test runner. unittest has some important requirements for writing and executing tests.

unittest requires that:

You put your tests into classes as methods
You use a series of special assertion methods in the unittest.TestCase class instead of the built-in assert statement
To convert the earlier example to a unittest test case, you would have to:

Import unittest from the standard library
Create a class called TestSum that inherits from the TestCase class
Convert the test functions into methods by adding self as the first argument
Change the assertions to use the self.assertEqual() method on the TestCase class
Change the command-line entry point to call unittest.main()
Follow those steps by creating a new file test_sum_unittest.py with the following code:

import unittest


class TestSum(unittest.TestCase):

    def test_sum(self):
        self.assertEqual(sum([1, 2, 3]), 6, "Should be 6")

    def test_sum_tuple(self):
        self.assertEqual(sum((1, 2, 2)), 6, "Should be 6")

if __name__ == '__main__':
    unittest.main()
If you execute this at the command line, you’ll see one success (indicated with .) and one failure (indicated with F):

$ python test_sum_unittest.py
.F
======================================================================
FAIL: test_sum_tuple (__main__.TestSum)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "test_sum_unittest.py", line 9, in test_sum_tuple
    self.assertEqual(sum((1, 2, 2)), 6, "Should be 6")
AssertionError: Should be 6

----------------------------------------------------------------------
Ran 2 tests in 0.001s

FAILED (failures=1)
You have just executed two tests using the unittest test runner.

Note: Be careful if you’re writing test cases that need to execute in both Python 2 and 3. In Python 2.7 and below, unittest is called unittest2. If you simply import from unittest, you will get different versions with different features between Python 2 and 3.

For more information on unittest, you can explore the unittest Documentation.

nose
You may find that over time, as you write hundreds or even thousands of tests for your application, it becomes increasingly hard to understand and use the output from unittest.

nose is compatible with any tests written using the unittest framework and can be used as a drop-in replacement for the unittest test runner. The development of nose as an open-source application fell behind, and a fork called nose2 was created. If you’re starting from scratch, it is recommended that you use nose2 instead of nose.

To get started with nose2, install nose2 from PyPI and execute it on the command line. nose2 will try to discover all test scripts named test*.py and test cases inheriting from unittest.TestCase in your current directory:

$ pip install nose2
$ python -m nose2
.F
======================================================================
FAIL: test_sum_tuple (__main__.TestSum)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "test_sum_unittest.py", line 9, in test_sum_tuple
    self.assertEqual(sum((1, 2, 2)), 6, "Should be 6")
AssertionError: Should be 6

----------------------------------------------------------------------
Ran 2 tests in 0.001s

FAILED (failures=1)
You have just executed the test you created in test_sum_unittest.py from the nose2 test runner. nose2 offers many command-line flags for filtering the tests that you execute. For more information, you can explore the Nose 2 documentation.

pytest
pytest supports execution of unittest test cases. The real advantage of pytest comes by writing pytest test cases. pytest test cases are a series of functions in a Python file starting with the name test_.

pytest has some other great features:

Support for the built-in assert statement instead of using special self.assert*() methods
Support for filtering for test cases
Ability to rerun from the last failing test
An ecosystem of hundreds of plugins to extend the functionality
Writing the TestSum test case example for pytest would look like this:

def test_sum():
    assert sum([1, 2, 3]) == 6, "Should be 6"

def test_sum_tuple():
    assert sum((1, 2, 2)) == 6, "Should be 6"
You have dropped the TestCase, any use of classes, and the command-line entry point.

More information can be found at the Pytest Documentation Website.
Writing Your First Test
Let’s bring together what you’ve learned so far and, instead of testing the built-in sum() function, test a simple implementation of the same requirement.

Create a new project folder and, inside that, create a new folder called my_sum. Inside my_sum, create an empty file called __init__.py. Creating the __init__.py file means that the my_sum folder can be imported as a module from the parent directory.

Your project folder should look like this:

project/
│
└── my_sum/
    └── __init__.py
Open up my_sum/__init__.py and create a new function called sum(), which takes an iterable (a list, tuple, or set) and adds the values together:

def sum(arg):
    total = 0
    for val in arg:
        total += val
    return total
This code example creates a variable called total, iterates over all the values in arg, and adds them to total. It then returns the result once the iterable has been exhausted.

Where to Write the Test
To get started writing tests, you can simply create a file called test.py, which will contain your first test case. Because the file will need to be able to import your application to be able to test it, you want to place test.py above the package folder, so your directory tree will look something like this:

project/
│
├── my_sum/
│   └── __init__.py
|
└── test.py
You’ll find that, as you add more and more tests, your single file will become cluttered and hard to maintain, so you can create a folder called tests/ and split the tests into multiple files. It is convention to ensure each file starts with test_ so all test runners will assume that Python file contains tests to be executed. Some very large projects split tests into more subdirectories based on their purpose or usage.

Note: What if your application is a single script?

You can import any attributes of the script, such as classes, functions, and variables by using the built-in __import__() function. Instead of from my_sum import sum, you can write the following:

target = __import__("my_sum.py")
sum = target.sum
The benefit of using __import__() is that you don’t have to turn your project folder into a package, and you can specify the file name. This is also useful if your filename collides with any standard library packages. For example, math.py would collide with the math module.

How to Structure a Simple Test
Before you dive into writing tests, you’ll want to first make a couple of decisions:

What do you want to test?
Are you writing a unit test or an integration test?
Then the structure of a test should loosely follow this workflow:

Create your inputs
Execute the code being tested, capturing the output
Compare the output with an expected result
For this application, you’re testing sum(). There are many behaviors in sum() you could check, such as:

Can it sum a list of whole numbers (integers)?
Can it sum a tuple or set?
Can it sum a list of floats?
What happens when you provide it with a bad value, such as a single integer or a string?
What happens when one of the values is negative?
The most simple test would be a list of integers. Create a file, test.py with the following Python code:

import unittest

from my_sum import sum


class TestSum(unittest.TestCase):
    def test_list_int(self):
        """
        Test that it can sum a list of integers
        """
        data = [1, 2, 3]
        result = sum(data)
        self.assertEqual(result, 6)

if __name__ == '__main__':
    unittest.main()
This code example:

Imports sum() from the my_sum package you created

Defines a new test case class called TestSum, which inherits from unittest.TestCase

Defines a test method, .test_list_int(), to test a list of integers. The method .test_list_int() will:

Declare a variable data with a list of numbers (1, 2, 3)
Assign the result of my_sum.sum(data) to a result variable
Assert that the value of result equals 6 by using the .assertEqual() method on the unittest.TestCase class
Defines a command-line entry point, which runs the unittest test-runner .main()

If you’re unsure what self is or how .assertEqual() is defined, you can brush up on your object-oriented programming with Python 3 Object-Oriented Programming.

