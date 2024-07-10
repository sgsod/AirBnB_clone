#!/usr/bin/python3
"""
Console command interpreter.

Class:

    HNBHCommand
"""

import cmd


class HBNBCommand(cmd.Cmd):
    """
    Shell class for HBNB project

    Attributes:
        prompt : str
            prompt at the beginning of line

    Methods:
        emptyline
        EOF
        exit
    """


    prompt = "(hbnb) "

    def do_create(self):
        pass

    def emptyline(self):
        """
        parse empty line without repeating last command
        """

        pass

    def do_quit(self):
        """
        exit interpreter
        """

        return True

    def do_EOF(self, line):
        """
        Exit the interpreter
        """
        print()
        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()
