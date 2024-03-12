#!/usr/bin/python3
"""The console aka command interpreter"""
import cmd
import models


class HBNBCommand(cmd.Cmd):
    """hbnb command interpreter"""
    prompt = '(hbnb) '

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

    def do_create(self, arg0):
        """Creates a new instance of BaseModel, saves it
        (to the JSON file) and prints the id"""
        if arg0 == "":
            print("** class name missing **")
        elif arg0 == "BaseModel":
            instance = models.base_model.BaseModel()
            instance.save()
            print(instance.id)
        else:
            print("** class doesn't exist **")

    def do_show(self, arg0):
        """Prints the string representation of
        an instance based on the class name and id"""
        arguments = arg0.split()
        if len(arguments) == 0:
            print ("** class name missing **")
        elif arguments[0] != "BaseModel":
            print("** class doesn't exist **")
        elif len(arguments) != 2:
            print("** instance id missing **")
        else:
            line = arguments[0] + "." + arguments[1]
            if line in models.storage.all():
                print(models.storage.all()[line])
            else:
                print("** no instance found **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
