#!/usr/bin/python3
""" Consile for AirBnB clone """

import cmd
from models.base_model import BaseModel
from models.__init__ import storage
import re


class HBNBCommand(cmd.Cmd):

    prompt = '(hbnb) '

    def do_EOF(self, arg):
        """ Enable quiting the console with EOF """
        print()
        return True

    def do_exit(self, arg):
        """ Exits the console """
        return True

    def do_quit(self, arg):
        """ Quits the console """
        return True

    def emptyline(self):
        """ Do nothing on empty string """
        pass

    def __arg_validate(self, args):
        """
        Validates the input of commands that require:
            - Supported class as arg[0]
            - Valid uuid string as arg[1]
        """
        if not args:
            print("** class name missing **")
            return True
        if args[0] not in storage.classtype():
            print("** class doesn't exist **")
            return True
        if len(args) < 2:
            print("** instance id missing **")
            return True
        if len(args) > 2:
            print("Usage: <command> <class name> <id>")
            return True
        if not self.__checkid(args[1]):
            pass

    def do_create(self, arg):
        """
        Creates a new instance of BaseModel, saves it to the json file and
        prints the instances id.
            Usage: create BaseModel()
        """
        try:
            if arg == "":
                print("** class name missing **")
                return
            if arg not in storage.classtype():
                print("** class doesn't exist **")
                return
            obj = BaseModel()
            obj.save()
            print(obj.id)
        except ValueError:
            print("Usage: create BaseModel()")

    def do_show(self, arg):
        """
        Prints the string representation of an instance based on the class name
        and id.
            Usage: show BaseModel 1234-1234-1234
        """
        try:
            args = arg.split()
            if self.__arg_validate(args):
                return
            key = args[0] + "." + args[1]
            storage.reload()
            loaded = storage.all()
            print(loaded[key])
        except KeyError:
            print("** no instance found **")

    def do_destroy(self, arg):
        """
        Deletes an object and saves changes to storage
        """
        try:
            args = arg.split()
            if self.__arg_validate(args):
                return
            key = args[0] + "." + args[1]
            storage.reload()
            loaded = storage.all()
            del(loaded[key])
            storage.save()
        except KeyError:
            print("** no instance found **")

    def do_all(self, arg):
        """
        Prints all string representation of all instances based or not on the
        class name
        """
        if arg is not None and arg != "":
            args = arg.split()
            if args[0] not in storage.classtype():
                print("** class doesn't exist **")
            else:
                objs = []
                for key, obj in storage.all().items():
                    if type(obj).__name__ == args[0]:
                        objs.append(str(obj))
                print(objs)
        else:
            objs = [str(obj) for key, obj in storage.all().items()]
            print(objs)

    def do_update(self, arg):
        """
        Updates attribute of a choosen house
        """
        if arg is None or arg == "":
            print("** class name missing **")
            return
        pattern = r'^(\S+)(?:\s+(\S+)(?:\s+(\S+)(?:\s+(\S+))?)?)?'
        match = re.match(pattern, arg)
        obj_class = match.group(1)
        obj_id = match.group(2)
        attribute = match.group(3)
        value = match.group(4)
        if not match:
            print("** class name missing **")
            return
        if obj_class not in storage.classtype():
            print("** class doesn't exist **")
            return
        if obj_id is None or obj_id == "":
            print("** instance id missing **")
            return
        key = "{}.{}".format(obj_class, obj_id)
        if key not in storage.all():
            print("** no instance found **")
            return
        if attribute is None or attribute == "":
            print("** attribute name missing **")
            return
        if value is None or value == "":
            print("** value missing **")
            return
        print(obj_class)
        print(obj_id)
        print(attribute)
        print(value)
        if not re.search('^".*"$', value):
            if '.' in value:
                value = float(value)
            else:
                value = int(value)
        else:
            value = value.replace('"', '')
        setattr(storage.all()[key], attribute, value)
        storage.all()[key].save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
