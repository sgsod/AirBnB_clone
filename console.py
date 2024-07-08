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


    def __init__(self):
        self.prompt = "(hbnb)"
    
    def emptyline(self):
        """
        parse empty line without repeating last command
        """

        pass

    def do_exit(self):
        """
        exit interpreter
        """

        return True

    def do_EOF(self, line):
        """
        Exit the interpreter
        """

        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()
