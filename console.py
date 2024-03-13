#!/usr/bin/python3
"""The console aka command interpreter"""
import cmd
import models
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """hbnb command interpreter"""
    prompt = '(hbnb) '
    classes = {
            "BaseModel": BaseModel,
            "User": User,
            "Place": Place,
            "State": State,
            "City": City,
            "Amenity": Amenity,
            "Review": Review
            }

    def do_quit(self, arg0):
        """command to exit the program"""
        return True

    def do_EOF(self, arg0):
        """command to exit the program"""
        return True

    def pls_help(self):
        """help command"""
        print("help command provides info on other existing commands")

    def emptyline(self):
        pass

    def do_create(self, arguments):
        """Creates a new instance of BaseModel, saves it
        (to the JSON file) and prints the id"""
        if arguments == "":
            print("** class name missing **")
        elif arguments in HBNBCommand.classes:
            cls = HBNBCommand.classes[arguments]
            instance = cls()
            instance.save()
            print(instance.id)
        else:
            print("** class doesn't exist **")

    def do_show(self, arguments):
        """Prints the string representation of
        an instance based on the class name and id"""
        args = arguments.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
        elif len(args) != 2:
            print("** instance id missing **")
        else:
            line = args[0] + "." + args[1]
            if line in models.storage.all():
                print(models.storage.all()[line])
            else:
                print("** no instance found **")

    def do_destroy(self, arguments):
        """Deletes an instance based on the class name
        and id (save the change into the JSON file)"""
        args = arguments.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
        elif len(args) != 2:
            print("** instance id missing **")
        else:
            line = args[0] + "." + args[1]
            if line in models.storage.all():
                del models.storage.all()[line]
                models.storage.save()
            else:
                print("** no instance found **")

    def do_all(self, arguments):
        """Prints all string representation of all
        instances based or not on the class name"""
        if arguments == "":
            for value in storage.all().values():
                print([str(value)])
        elif arguments in HBNBCommand.classes:
            for key, value in models.storage.all().items():
                if key.split(".")[0] == arguments:
                    print([str(value)])
        else:
            print("** class doesn't exist **")

    def do_update(self, arguments):
        """Updates an instance based on the class
        name and id by adding or updating attribute
        (save the change into the JSON file)."""
        args = arguments.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
        elif len(args) > 1:
            line = args[0] + "." + args[1]
            if line in models.storage.all():
                if len(args) == 2:
                    print("** attribute name missing **")
                elif len(args) == 3:
                    print("** value missing **")
                else:
                    args = args[0:4]
                    args[3] = eval(args[3])
                    setattr(models.storage.all()[line], args[2], args[3])
                    models.storage.all()[line].save()
            else:
                print("** no instance found **")
        elif len(args) == 1:
            print("** instance id missing **")

    def do_count(self, arguments):
        """retrieve the number of instances of a class"""
        count = 0
        for instance in models.storage.all().values():
            if instance.__class__.__name__ == arguments:
                count += 1
        print(count)

    def default(self, arguments):
        """accesses methods through a different format"""
        parts = arguments.split(".")
        command = parts[0]
        first_two= ["all()", "count()"]
        method = None
        if command in HBNBCommand.classes:
            if parts[1] == first_two[0]:
                all = getattr(self, 'do_all')
                all(command)
            elif parts[1] == first_two[1]:
                HBNBCommand.do_count(self, command)
            else:
                method_name, *args = parts[1].rstrip(')').split("(")
                if hasattr(self, f"do_{method_name}"):
                    method = getattr(self, f"do_{method_name}")
                if args:
                    args = args[0].split(", ")
                    args = [eval(arg) if arg.startswith('"')
                        and arg.endswith('"') else arg for arg in args]
                    arguments = f"{command} {' '.join(args)}"
                else:
                    arguments = command
            if method:
                method(arguments)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
