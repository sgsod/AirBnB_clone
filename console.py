#!/usr/bin/python3
"""Console: command interpreter"""
import cmd

class HBNBCommand(cmd.Cmd):
    self.prompt = "(hbnb)"
    
    def emptyline(self):
        pass

    def do_EOF(self, line):
        "Exit the interpreter"
        return True

    

if __name__ == '__main__':
    HBNBCommand().cmdloop()
