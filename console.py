#!/usr/bin/python3
"""Console module for HBNB command interpreter."""
import cmd
import json
import models

COMMANDS = {
    "create": BaseModel.create,
    "show": BaseModel.show,
    "destroy": BaseModel.destroy,
    "all": BaseModel.all,
    "update": BaseModel.update,
    "User": User,
    "show User": BaseModel.show,
    "create User": BaseModel.create,
    "destroy User": BaseModel.destroy,
    "update User": BaseModel.update,
    "all User": BaseModel.all
}

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
            new_instance = models.classes[arg_list[0]]()
            new_instance.save()
            print(new_instance.id)
        except KeyError:
            print("** class doesn't exist **")

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
        except KeyError:
            print("** no instance found **")

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
        except KeyError:
            print("** no instance found **")

    def do_all(self, arg):
        """Prints all string representation of all instances."""
        arg_list = arg.split()
        obj_list = []
        if not arg:
            for key, value in models.storage.all().items():
                obj_list.append(str(value))
            print(obj_list)
            return
        try:
            for key, value in models.storage.all().items():
                if arg_list[0] == value.__class__.__name__:
                    obj_list.append(str(value))
            print(obj_list)
        except KeyError:
            print("** class doesn't exist **")

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
        except KeyError:
            print("** no instance found **")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
          
