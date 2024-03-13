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
        for instance in models.storage.all().keys():
            if instance.split(".")[0] == arguments:
                count += 1
        print(count)
    def format(self, arguments):
        """accesses methods through a different format"""
        methods = ["all()", "count()"]
        args = arguments.split(".")
        arguments = args[0]
        if arguments in HBNBCommand.classes:
            if args[1] == method[0]:
                all = getattr(self, 'do_all')
                all(arguments)
            elif args[1] == methods[1]:
                HBNBCommand.do_count()
            elif args[1].startswith('show("') and args[1].endswith('")'):
                id = args[1][6:-2]
                line = line + " " + id
                show = getattr(self, 'do_show')
                show(line)
            elif args[1].startswith('destroy("') and args[1].endswith('")'):
                id = args[1][9:-2]
                line = line + " " + id
                destroy = getattr(self, 'do_destroy')
                destroy(line)
            elif args[1].startswith('update(') and args[1].endswith(')'):
                args[1] = args[1][7:-1]
                args = args[1].split(", ")
                for i in range(min(len(args), 2)):
                    args[i] = eval(args[i])
                line += " " +  " ".join(args)
                update = getattr(self, 'do_update')
                update(line)



if __name__ == '__main__':
    HBNBCommand().cmdloop()
