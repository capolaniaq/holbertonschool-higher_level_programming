# 0x0B. Python - Input/Output

Foundations - Higher-level programming ― Python

By Guillaume, CTO at Holberton School

Author [Carlos Andres Polania](https://twitter.com/timberdev) (capolaniaq@correo.udistrital.edu.co)
## Learning Objectives

-   Why Python programming is awesome
-   How to open a file
-   How to write text in a file
-   How to read the full content of a file
-   How to read a file line by line
-   How to move the cursor in a file
-   How to make sure a file is closed after using it
-   What is and how to use the  `with`  statement
-   What is  `JSON`
-   What is serialization
-   What is deserialization
-   How to convert a Python data structure to a JSON string
-   How to convert a JSON string to a Python data structure


![enter image description here](https://github.com/capolaniaq/holbertonschool-higher_level_programming/blob/main/0x0B-python-input_output/img/encode-archiving.png) 

## Tasks

### 0. Read file
Write a function that reads a text file (`UTF8`) and prints it to stdout:

-   Prototype:  `def read_file(filename=""):`
-   You must use the  `with`  statement
-   You don’t need to manage  `file permission`  or  `file doesn't exist`  exceptions.
-   You are not allowed to import any module

### 1. Write to a file
Write a function that writes a string to a text file (`UTF8`) and returns the number of characters written:

-   Prototype:  `def write_file(filename="", text=""):`

Write a function that appends a string at the end of a text file (`UTF8`) and returns the number of characters added:

-   Prototype:  `def append_write(filename="", text=""):

### 3. To JSON string
Write a function that returns the JSON representation of an object (string):

-   Prototype:  `def to_json_string(my_obj):`
-   You don’t need to manage exceptions if the object can’t be serialized.
### 4. From JSON string to Object
Write a function that returns an object (Python data structure) represented by a JSON string:

-   Prototype:  `def from_json_string(my_str):`
-   You don’t need to manage exceptions if the JSON string doesn’t represent an object.
### 5. Save Object to a file
Write a function that writes an Object to a text file, using a JSON representation:

-   Prototype:  `def save_to_json_file(my_obj, filename):`
### 6. Create object from a JSON file
Write a function that creates an Object from a “JSON file”:

-   Prototype:  `def load_from_json_file(filename):`
-   You must use the  `with`  statement
### 7. Load, add, save
Write a script that adds all arguments to a Python list, and then save them to a file:

-   You must use your function  `save_to_json_file`  from  `5-save_to_json_file.py`
-   You must use your function  `load_from_json_file`  from  `6-load_from_json_file.py`
-   The list must be saved as a JSON representation in a file named  `add_item.json`
### 8. Class to JSON
Write a function that returns the dictionary description with simple data structure (list, dictionary, string, integer and boolean) for JSON serialization of an object:

-   Prototype:  `def class_to_json(obj):`
### 9. Student to JSON
Write a class  `Student`  that defines a student by:

-   Public instance attributes:
    -   `first_name`
    -   `last_name`
    -   `age`
-   Instantiation with  `first_name`,  `last_name`  and  `age`:  `def __init__(self, first_name, last_name, age):`
-   Public method  `def to_json(self):`  that retrieves a dictionary representation of a  `Student`  instance (same as  `8-class_to_json.py`)
-   You are not allowed to import any module
### 10. Student to JSON with filter
Write a class  `Student`  that defines a student by: (based on  `9-student.py`)

-   Public instance attributes:
    -   `first_name`
    -   `last_name`
    -   `age`
-   Instantiation with  `first_name`,  `last_name`  and  `age`:  `def __init__(self, first_name, last_name, age):`
-   Public method  `def to_json(self, attrs=None):`  that retrieves a dictionary representation of a  `Student`  instance (same as  `8-class_to_json.py`):
    -   If  `attrs`  is a list of strings, only attribute names contained in this list must be retrieved.
    -   Otherwise, all attributes must be retrieved
 
 ### 11. Student to disk and reload
 Write a class  `Student`  that defines a student by: (based on  `10-student.py`)

-   Public instance attributes:
    -   `first_name`
    -   `last_name`
    -   `age`
-   Instantiation with  `first_name`,  `last_name`  and  `age`:  `def __init__(self, first_name, last_name, age):`
-   Public method  `def to_json(self, attrs=None):`  that retrieves a dictionary representation of a  `Student`  instance (same as  `8-class_to_json.py`):
    -   If  `attrs`  is a list of strings, only attributes name contain in this list must be retrieved.
    -   Otherwise, all attributes must be retrieved
-   Public method  `def reload_from_json(self, json):`  that replaces all attributes of the  `Student`  instance:
    -   You can assume  `json`  will always be a dictionary
    -   A dictionary key will be the public attribute name
    -   A dictionary value will be the value of the public attribute
  
  ### 12. Pascal's Triangle
  -   You are not allowed to google anything
-   Whiteboard first

Create a function  `def pascal_triangle(n):`  that returns a list of lists of integers representing the Pascal’s triangle of  `n`:

-   Returns an empty list if  `n <= 0`
-   You can assume  `n`  will be always an integer
-   You are not allowed to import any module