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

    def do_help(self):
        """help command"""
        print("help command provides info on other existing commands")

    def empty_line(self):
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
