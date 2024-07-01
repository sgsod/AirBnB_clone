#!/usr/bin/python3
"""Console: command interpreter"""


import cmd

class HBNBCommand(cmd.Cmd):
    self.prompt = "(hbnb)"
    
    def emptyline(self):
        """parse empty line without repeating last command"""
        pass

    def do_exit(self):
        """exit interpreter"""
        return True

    def do_EOF(self, line):
        """Exit the interpreter"""
        return True

    

if __name__ == '__main__':
    HBNBCommand().cmdloop()
