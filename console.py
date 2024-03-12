#!/usr/bin/python3
"""The console aka command interpreter"""
import cmd
import models
from models.base_model import BaseModel
from models.user import User


class HBNBCommand(cmd.Cmd):
    """hbnb command interpreter"""
    prompt = '(hbnb) '
    classes = {
            "BaseModel": BaseModel,
            "User": User
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
        elif arguments in classes:
            instance = models.base_model.BaseModel()
            instance.save()
            print(instance.id)
        else:
            print("** class doesn't exist **")

    def do_show(self, arguments):
        """Prints the string representation of
        an instance based on the class name and id"""
        args = arguments.split()
        if len(args) == 0:
            print ("** class name missing **")
        elif args[0] not in classes:
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
        elif args[0] not in classes:
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
            for values in models.storage.all().values():
                print([str(values)])
        elif arguments in classes:
            for keys in models.storage.all():
                if arguments in keys:
                    print([str(models.storage.all()[keys])])
        else:
            print("** class doesn't exist **")

    def do_update(self, arguments):
        """Updates an instance based on the class
        name and id by adding or updating attribute
        (save the change into the JSON file)."""
        args = arguments.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in classes:
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



if __name__ == '__main__':
    HBNBCommand().cmdloop()
