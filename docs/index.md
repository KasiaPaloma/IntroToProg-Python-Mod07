# Error Handling and Pickling
*KRozanska, 12.15.2020*

## Introduction 
In this demonstration we will ask for a user’s name and age, calculate it into seconds, and save it as a binary file. This will help us discuss error handling with try and except blocks, as well as pickling. You may follow the GitHub repository to see the full script and follow below to understand specific snippets.

## Error Handling
As we have reviewed in previous demonstrations, you want to stay one step ahead of your user when asking for inputs. One way you do this is by controlling the data they can enter, for example, only allowing numeric characters in an age field. Another way is by controlling the error messages they receive, rather than the messages that Python would show. This allows for cleaner data and a user-friendly environment. 
Look at the below code.
```
age = float(input("How old are you? - "))
```
If the user does not enter a number, as our code expects, they will receive the below error. We understand it because we understand Python syntax, but this does not mean that your user will understand what they did incorrectly.
 
The try and except blocks, examples of structured error handling, were created to offer more consistency within programs and different developers. https://www.youtube.com/watch?v=nlCKrKGHSSk gives a quick overview of the four clauses in Python Exception handling. Below we will use the same code as above, but use try and except to help the user receive an error message that will guide them in the right direction. In this example we are replacing the specific exception ValueError message with “Age should be a number.”
```
while True:
    try:
        age = float(input("How old are you? - "))
    except ValueError:
        print("Age should be a number.\n")
```
The code will first execute the try clause, and if no exception occurs then it will skip the except clause. See below how much cleaner the error is now?
 
https://docs.python.org/3/library/exceptions.html gives a great overview of all the exceptions that are built into Python. When an exception occurs, it may have an argument, which is an associated value. You can display this argument by specifying a variable after the exception. 
```
try:
    age = float(input("How old are you? - "))
except Exception as e:
    print("That is not a valid age!")
    print(e)
```
Now the user will see exactly what created the error message. In the example below we have a simple version and we see that the issue is the “K” that was entered, but this error handling can become more useful with more advanced code. 
 
You can also group multiple exception types by listing them in a single except clause, by creating a comma-separated group enclosed in a set of parentheses:
```
while True:
    try:
        age = float(input("How old are you? - "))
    except (ValueError, TypeError):
        print("Age should be a number.\n")
```
### Subtopic 
## Summary
