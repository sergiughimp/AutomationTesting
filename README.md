Session 1
1. comments = lines of code that program not read, only for humans
2. variables = container to store values
3. data types = int, str, bool, float/double
4. type_casting = force the conversion from one data type to another
5. print() function = way to communicate with program (output)
6. assert = used to make verifications
7. input() function = to give data to program from user keyboard


Session 2 \
operators = operations with variables
```
assignation =, +=, -=, *=, /=
arithmetics +, -, *, /, **, % 
    concatenation = add one string/list to another
comparison: <, >, ==, <=, >=, !=
logical: and, or, not
```
control flow = check a condition
```
if
if - else = if condition is true goes on first branch, if condition is false goes on second branch
if - else - if - else
```
Session 3 \
data structures = collection of data to store multiple items in one variable. size of data collection use len() function
```
list = ordered, mutable, allow duplicates, allow slicing
dict = key:value pairs
set = unordered, unchangeable, un-indexed, no slicing
tuples = ordered and unchangeable, allow duplicates, allow slicing
```
Session 4 \
loops
```
for: to iterate (through the index) over a sequence of data. with a known number of steps
for each: to iterate (through the value) over a sequence of data. with a known number of steps
break: stop the iteration
for else: runs only when iteration of for ends without any taking something from for
continue: continues to the iteration to next step
while: iterates until the condition is true
while else: runs only when iteration of while ends without any taking something from while
nested loop: for in for
```
Session 5 \
functions = block of code that can be reused
```
simple functions
functions with parameters (variables that can be passed to function)
functions with 2 parameters
functions with return (value that a function sends back when it is called) 
```
Session 6 \
class = template to create objects from that class
```
objects = instance of a class
__init__ = constructor of the class, used as a start to create objects in the class.
self = keyword used to access variable that belongs to that class
methods = functions on objects
```
Session 7 \
Oriented Object Programming (OOP) concepts:
```
Inheritance = one class inherits the attributes and methods of another class.
Encapsulation = binding data (attributes) and methods (operations) together into objects and limiting the direct access to its internals. Use access modifiers public, __private (can be accessed only from inside the class), _protected (can be accessed from current class and child class).
Abstraction =  hides all but the relevant data about an object. used as a template for methods from the child class. doesn't have constructor. can't create abstract objects
Polymorphism = objects take different forms or behaviour in different ways depending on the context in which they are used.
```
Session 8 \
Selectors \
    1. pip install selenium (https://selenium-python.readthedocs.io/ library for testing websites) \
    2. pip install webdriver-manager (https://pypi.org/project/webdriver-manager/)\
    3. site for testing: (ex: https://formy-project.herokuapp.com/form) \

Selenium = library in python used to interact with webpages
```
find_element(By.ID, "id") - ID selector
find_element(By.LINK_TEXT, "TEXT") - LINK_TEXT selector
find_element(By.PARTIAL_LINK_TEXT, "TE"") - PARTIAL_LINK_TEXT selector
find_element(By.TAG_NAME, "input") - TAG_NAME selector (one 'input')
find_elements(By.TAG_NAME, "input"") - TAG_NAME selector (all 'inputs')
find_element(By.NAME, "email") - NAME selector
find_element(By.CLASS, "form-control") - CLASS selector
find_element(By.CSS, "h1") - CSS selector
    css selectors = can group multiple types of selectors (TAG_NAME, ID (#), CLASS (.), others (attribute_name = ["value"]), HTML structure)
find_element(By.XPATH, '//*[@id="password"]') - XPATH selector
    // - starts from root and takes all the descendants
    * - any type of tag
    [@something="value"] - selects only the tags that have the attribute "something = value"
    / - only direct descendant
```
Session 9 \
Waits
https://selenium-python.readthedocs.io/waits.html
```
sleep() - code sleeps x seconds, no matters of element or event from the code. the test will have more time to run
implicit wait - global setting that applies to all elements in a Selenium script. It waits a specified time before throwing an exception if the element is not found
explicit wait - when it waits for a certain condition to occur before to proceeding to further in the code
```
UnitTests = unittest library. create a class test that inherits TestCase

Mandatory methods
```
setUp() - everything before the testing
any number of test - mandatory all the test have to start with keyword 'test'
tearDown() - everything after the testing
```
Session 10 \
TestSuite \
pip install html-testRunner - to generate HTML reports
```
skip decorator @unittest.skip
alerts (JavaScript)
    Alert - //button[@onclick='jsAlert()']
    Confirm - //button[@onclick='jsConfirm()
    Prompt - //button[@onclick='jsPrompt()
syntax to 'log in' with basic authentication (pop-up from browser)
```
Session 11 \
BDD (Behaviour Driven Development) = process that comes from Test Driven Development (TDD) and goes to Acceptance criteria (DofD = Definition of Done)

TDD (Test Driven Development) = writing tests before writing the actual code

Gherkin Syntax = language used to define structure. (Cucumber Syntax: Given, When, Then, And, But - helps to describe the behavior of the tested application. User Story -> Test Syntax). Generates HTML reports.
```
Given: initial state of the test-case
When: actions the user is doing
Then: making assert, final state of the test-case
And, But: for making connection between: Give, When, Then
```
Gherkin test are in the .feature file:
```
Feature: Name of the feature (Register User)
Scenario: Name of scenario (Register with success)
    Given: initial stage
    When: actions of the user
    And: -> When
    Then: final stage
    And: -> Then
     
    
```
Feature file structure
```
feature file
    file1.feature
    file2.feature
    file3.feature
    ...
    environment.py # settings about behave
    steps
        steps/file1.py # steps for file1.feature
        steps/file2.py 
        ...
```

Python file with Gherkin steps structure
```
from behave import *

@given("we have behave installed")
def step_imp(context):
    pass

@when("we implement a test")
def step_imp(context):
    pass

@then("behave will test it for us!")
def step_imp(context):
    pass
```
Object 'context' is sent as a parameter to 'behave' to send information through stepts

To install:
1. pip install behave (https://behave.readthedocs.io/en/latest/ library for run the tests from Gherkin)
2. pip install selenium (https://selenium-python.readthedocs.io/ library for testing websites)
3. pip install behave-html-formatter (https://pypi.org/project/behave-html-formatter/ library to create HTML reports)
    3.1. It is a must to create a file 'behave.ini' in main folder in the same level with feature. Make the settings for this file to create the HTML report. \
    3.2.  To run the code and to generate a HTML report use this command: behave -f html -o behave-report.html
4. pip install webdriver-manager (https://pypi.org/project/webdriver-manager/)




One Feature can have multiple scenarios

POM (Project Object Model) = design pattern used to reduce code duplication and to minimize the effort involved in code maintenance. helps to organize the files in a logical way and easy to use. Each page of the project will have individual class where we can find the elements of the page.

Agile methodology = breaking the project into phases and emphasizes continuous collaboration and improvement \
The project is launched incrementally \
    1. MVP = minimum value product. to launch the project \
    2. Add functionalities + launch the product

Sprint = fixed length periods of work (3-4 days or 1-2 weeks). Start task -> End task. Every sprint has a piece of the project
```
Epic (Step 1) = functionality of the application (can be divided in tasks)
User Story (Step 2) - explication of the functionality or feature software
Acceptance criteria (Step 3 (Final)) (DD = definition of done) = conditions that must be satisfied for a product, user story, or increment of work to be accepted
```