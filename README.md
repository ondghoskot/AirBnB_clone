# AirBnB clone - The console
---
## Descrption of the project:
In this project, we will be working towards the first step of building a full web application, which is essentially a clone of the already existing AirBnB webapp. This first step consists of writing a **command interpreter** to help us manage our objects better and more efficiently

## Description of the interpreter:
It's just like every command interpreter you've probably encountered, except it's limited to a specific use-case. In our case, we want to be able to manage the objects of our project:

* Create a new object (ex: a new User or a new Place)
* Retrieve an object from a file, a database etc…
* Do operations on objects (count, compute stats, etc…)
* Update attributes of an object
* Destroy an object

### how to start it:
To start our interpreter, we call our executable file (chmod u+x console.py) in interactive mode like this:
```bash
$./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$
```
In none interractive mode, we should see something like this:
```bash
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
```
### how to use it:
To use this command interpreter, all you have to do after starting it (see above), is enter one f these commands:

* <mark>create</mark>:  Creates a new instance of BaseModel, saves it (to the JSON file) and prints the id. **Ex: $ create BaseModel**
* <mark>show</mark>: Prints the string representation of an instance based on the class name and id.**Ex: $ show BaseModel 1234-1234-1234.**
* <mark>destroy</mark>:  Deletes an instance based on the class name and id (save the change into the JSON file). **Ex: $ destroy BaseModel 1234-1234-1234.**
* <mark>all</mark>: Prints all string representation of all instances based or not on the class name. **Ex: $ all BaseModel or $ all.**
* <mark>update</mark>: Updates an instance based on the class name and id by adding or updating attribute (save the change into the JSON file). **Ex: $ update BaseModel 1234-1234-1234 email "aibnb@mail.com".**
* <span style="background-color: lightgray">help</span>

* quit and EOF to exit the program

_See examples above
