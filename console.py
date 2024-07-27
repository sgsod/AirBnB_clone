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

    def do_create(self, line):
        """
        create an instance of BaseModel and prints id
        Usage: $ create BaseModel
        """
        from models.base_model import BaseModel
        tocreate = line.split()
        if len(tocreate) > 0:
            if tocreate[0] == "BaseModel":
                b = BaseModel()
                b.save()
                print(b.id)
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def do_show(self, line):
        """
        Print string representation of provided instance
        Usage: show <class name> <instance id>
               example: $ show BaseModel 1234-1234-1234
        """
        from models import storage
        toshow = line.split()
        length = len(toshow)
        if length > 0:
            if toshow[0] == "BaseModel" and length > 1:
                key = "{}.{}".format(toshow[0], toshow[1])
                instances = storage.all()
                if key in instances.keys():
                    print(str(instances[key]))
                else:
                    print("** no instance found **")
            elif toshow[0] == "BaseModel":
                print("** instance id missing **")
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def do_destroy(self, line):
        """
        Delete the provided instance
        Usage: destroy <class name> <instance id>
               example: $ destroy BaseModel 1234-1234-1234
        """
        from models import storage
        todestroy = line.split()
        length = len(todestroy)
        if length > 0:
            if todestroy[0] == "BaseModel" and length > 1:
                key = "{}.{}".format(toshow[0], toshow[1])
                instances = storage.all()
                if key in instances.keys():
                    del storage._FileStorage__objects[key]
                    storage.save()
                else:
                    print("** no instance found **")
            elif todestroy[0] == "BaseModel":
                print("** instance id missing **")
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def do_all(self, line):
        """
        Print string representations of all instances in the file
        or instances of a provided class
        """
        if line != "":
            words = line.split(' ')
            if words[0] not "BaseeModel":
                print("** class doesn't exist **")
            else:
                strAll = [str(value) for key, value in storage.all().items()
                      if type(value).__name__ == words[0]]
                print(strAll)
        else:
            strAll = [str(value) for key, value in storage.all().items()]
            print(strAll)
"""
    def do_update(self, line):
        from models import storage
        todestroy = line.split()
        length = len(todestroy)
        if length > 0:
            if todestroy[0] == "BaseModel" and length > 1:
                key = "{}.{}".format(toshow[0], toshow[1])
                instances = storage.all()
                if key in instances.keys():
                    del storage._FileStorage__objects[key]
                    storage.save()
                else:
                    print("** no instance found **")                                elif todestroy[0] == "BaseModel":
                print("** instance id missing **")
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")
"""
    #Mandatory methods:
    def emptyline(self):
        """parse empty line without repeating last command"""
        pass

    def do_quit(self):
        """exit interpreter"""
        return True

    def do_EOF(self, line):
        """Exit the interpreter"""
        print()
        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()
