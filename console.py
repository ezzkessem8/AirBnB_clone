#!/usr/bin/python3
"""Console module for HBNB command interpreter."""
import cmd
import json
from models.base_model import BaseModel

class HBNBCommand(cmd.Cmd):
    """Command interpreter for HBNB project."""
    
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, arg):
        """Exit the program."""
        print()
        return True

    def emptyline(self):
        """Do nothing on empty input."""
        pass

    def do_create(self, arg):
        """Create a new instance of BaseModel, save it, and print the id."""
        if not arg:
            print("** class name missing **")
            return
        arg_list = arg.split()
        try:
            new_instance = BaseModel()
            new_instance.save()
            print(new_instance.id)
        except Exception as e:
            print(e)

    def do_show(self, arg):
        """Prints the string representation of an instance."""
        if not arg:
            print("** class name missing **")
            return
        arg_list = arg.split()
        try:
            if len(arg_list) < 2:
                print("** instance id missing **")
                return
            key = "{}.{}".format(arg_list[0], arg_list[1])
            print(models.storage.all()[key])
        except Exception as e:
            print(e)

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id."""
        if not arg:
            print("** class name missing **")
            return
        arg_list = arg.split()
        try:
            if len(arg_list) < 2:
                print("** instance id missing **")
                return
            key = "{}.{}".format(arg_list[0], arg_list[1])
            del models.storage.all()[key]
            models.storage.save()
        except Exception as e:
            print(e)

    def do_all(self, arg):
        """Prints all string representation of all instances."""
        arg_list = arg.split()
        obj_list = []
        if not arg:
            for value in BaseModel.all():
                obj_list.append(str(value))
            print(obj_list)
            return
        try:
            for value in BaseModel.all():
                if arg_list[0] == value.__class__.__name__:
                    obj_list.append(str(value))
            print(obj_list)
        except Exception as e:
            print(e)

    def do_update(self, arg):
        """Updates an instance based on the class name and id."""
        if not arg:
            print("** class name missing **")
            return
        arg_list = arg.split()
        try:
            if len(arg_list) < 2:
                print("** instance id missing **")
                return
            key = "{}.{}".format(arg_list[0], arg_list[1])
            obj_dict = models.storage.all()
            obj_instance = obj_dict[key]
            if len(arg_list) < 3:
                print("** attribute name missing **")
                return
            if len(arg_list) < 4:
                print("** value missing **")
                return
            setattr(obj_instance, arg_list[2], arg_list[3].strip('"'))
            obj_instance.save()
        except Exception as e:
            print(e)

if __name__ == '__main__':
    HBNBCommand().cmdloop()
            
