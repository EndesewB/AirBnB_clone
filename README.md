## Getting Started
# What’s a command interpreter?

Do you remember the Shell? It’s exactly the same but limited to a specific use-case. In our case, we want to

be able to manage the objects of our project:



    * Create a new object (ex: a new User or a new Place).
    
    * Retrieve an object from a file, a database etc.

    * Do operations on objects (count, compute stats, etc…).

    * Update attributes of an object.

    * Destroy an object.


# Learning Objectives
# General

    * How to create a Python package

    * How to create a command interpreter in Python using the cmd module

    * What is Unit testing and how to implement it in a large project

    * How to serialize and deserialize a Class

    * How to write and read a JSON file

    * How to manage datetime

    * What is an UUID

    * What is *args and how to use it

    * What is **kwargs and how to use it

    * How to handle named arguments in a function

1. First ordered list item
2. Another item
  * Unordered sub-list. 
1. Actual numbers don't matter, just that it's a number
  1. Ordered sub-list
4. And another item.

   You can have properly indented paragraphs within list items. Notice the blank line above, and the leading spaces (at least one, but we'll use three here to also align the raw Markdown).

   To have a line break without a paragraph, you will need to use two trailing spaces.⋅⋅
   Note that this line is separate, but within the same paragraph.⋅⋅
   (This is contrary to the typical GFM line break behaviour, where trailing spaces are not required.)

* Unordered list can use asterisks
- Or minuses
+ Or pluses
# Execution

Your shell should work like this in interactive mode:

(hbnb)create Place
93d823aa-f03a-41f6-bf80-aecaa7445d1d
(hbnb)
(hbnb)create User
07563c34-e7f8-4b20-84bb-73ff9e30291b
(hbnb)
(hbnb)User.create()
b81095e8-1ad3-4ccf-b525-695baac4d071
(hbnb)
(hbnb)BaseModel.create()
5984b7e6-8c9b-4593-ac87-6bc17a9c400d
(hbnb)
(hbnb)

#Usage Examples

#Launching the console

$ ./console.py
(hbnb) 

#Creating a new object

(hbnb) create
** class name missing **
(hbnb) create User
670265eb-5982-489e-8b92-2dff054f0776

#Show an object

(hbnb) show User
** instance id missing **
(hbnb) show User 670265eb-5982-489e-8b92-2dff054f0776
[User] (670265eb-5982-489e-8b92-2dff054f0776) {'created_at': datetime.datetime(2020, 2, 19, 18, 8, 58, 458246), 'id': '670265eb-5982-489e-8b92-2dff054f0776', 'updated_at': datetime.datetime(2020, 2, 19, 18, 8, 58, 458261)}

#Update an object

(hbnb) all
["[User] (70f71c16-962b-48ad-9df8-9203fe23d612) {'created_at': datetime.datetime(2020, 2, 19, 18, 11, 32, 341144), 'id': '70f71c16-962b-48ad-9df8-9203fe23d612', 'updated_at': datetime.datetime(2020, 2, 19, 18, 11, 32, 341161)}"]
(hbnb) update
** class name missing **
(hbnb) update User
** instance id missing **
(hbnb) update User 70f71c16-962b-48ad-9df8-9203fe23d612
** attribute name missing **
(hbnb) update User 70f71c16-962b-48ad-9df8-9203fe23d612  Age "20"
(hbnb) all
["[User] (70f71c16-962b-48ad-9df8-9203fe23d612) {'Age': 20, 'created_at': datetime.datetime(2020, 2, 19, 18, 11, 32, 341144), 'id': '70f71c16-962b-48ad-9df8-9203fe23d612', 'updated_at': datetime.datetime(2020, 2, 19, 18, 13, 9, 937933)}"]
(hbnb)

Destroy an object

(hbnb) destroy
** class name missing **
(hbnb) destroy User
** instance id missing **
(hbnb) destroy User 670265eb-5982-489e-8b92-2dff054f0776
(hbnb)

