Session 1 \
*********** comments = lines of code that program not read, only for humans \
*********** variables = container to store values \
*********** data types = int, str, bool, float/double \
*********** type_casting = force the conversion from one data type to another \
*********** print() function = way to communicate with program (output) \
*********** assert = used to make verifications \
*********** input() function = to give data to program from user keyboard \
Session 2 \
*********** operators = operations with variables \
**** assignation =, +=, -=, *=, /= \
**** arithmetics +, -, *, /, **, % \
** concatenation = add one string/list to another\
**** comparison: <, >, ==, <=, >=, != \
**** logical: and, or, not


*********** control flow = check a condition \
**** if \
**** if - else = if condition is true goes on first branch, if condition is false goes on second branch \
**** if - else - if - else

Session 3 \
*********** data structures = collection of data to store multiple items in one variable. size of data collection use len() function \
**** list = ordered, mutable, allow duplicates, allow slicing \
**** dict = key:value pairs \
**** set = unordered, unchangeable, un-indexed, no slicing \
**** tuples = ordered and unchangeable, allow duplicates, allow slicing


Session 4 \
*********** loops \
**** for: to iterate (through the index) over a sequence of data. with a known number of steps \
**** for each: to iterate (through the value) over a sequence of data. with a known number of steps \
**** break: stop the iteration \
**** for else: runs only when iteration of for ends without any taking something from for \
**** continue: continues to the iteration to next step \
**** while: iterates until the condition is true \
**** while else: runs only when iteration of while ends without any taking something from while \
**** nested loop: for in for

Session 5 \
*********** functions = block of code that can be reused \
**** simple functions \
**** functions with parameters (variables that can be passed to function) \
**** functions with 2 parameters \
**** functions with return (value that a function sends back when it is called) 

Session 6 \
*********** class = template to create objects from that class \
**** objects = instance of a class \
**** __init__ = constructor of the class, used as a start to create objects in the class. \
**** self = keyword used to access variable that belongs to that class \
**** methods = functions on objects

Session 7 \
*********** Oriented Object Programming (OOP) concepts: \
**** Inheritance = one class inherits the attributes and methods of another class. \
**** Encapsulation = binding data (attributes) and methods (operations) together into objects and limiting the direct access to its internals. Use access modifiers public, __private (can be accessed only from inside the class), _protected (can be accessed from current class and child class). \
**** Abstraction =  hides all but the relevant data about an object. used as a template for methods from the child class. doesn't have constructor. can't create abstract objects \
**** Polymorphism = objects take different forms or behaviour in different ways depending on the context in which they are used.

Session 8 \
*********** Selectors \
****** pip install selenium \
****** pip install webdriver-manager \
****** site for testing: (ex: https://formy-project.herokuapp.com/form) \
**** Selenium = library in python used to interact with webpages \
** find_element(By.ID, "id") - ID selector \
** find_element(By.LINK_TEXT, "TEXT") - LINK_TEXT selector \
** find_element(By.PARTIAL_LINK_TEXT, "TE"") - PARTIAL_LINK_TEXT selector \
** find_element(By.TAG_NAME, "input") - TAG_NAME selector (one 'input') \
** find_elements(By.TAG_NAME, "input"") - TAG_NAME selector (all 'inputs') \
** find_element(By.NAME, "email") - NAME selector \ 
** find_element(By.CLASS, "form-control") - CLASS selector

******* find_element(By.CSS, "h1") - CSS selector \
**** css selectors = can group multiple types of selectors (TAG_NAME, ID (#), CLASS (.), others (attribute_name = ["value"]), HTML structure)

******* find_element(By.XPATH, '//*[@id="password"]') - XPATH selector \
** // - starts from root and takes all the descendants \
** * - any type of tag \
** [@something="value"] - selects only the tags that have the attribute "something = value" \
** / - only direct descendant

Session 9 \
*********** Waits \
********* https://selenium-python.readthedocs.io/waits.html \
**** sleep() - code sleeps x seconds, no matters of element or event from the code. the test will have more time to run \
**** implicit wait - global setting that applies to all elements in a Selenium script. It waits a specified time before throwing an exception if the element is not found \
**** explicit wait - when it waits for a certain condition to occur before to proceeding to further in the code

********** UnitTests = unittest library. create a class test that inherits TestCase \
******* Mandatory methods \
***** setUp() - everything before the testing \
***** any number of test - mandatory all the test have to start with keyword 'test' \
***** tearDown() - everything after the testing

 