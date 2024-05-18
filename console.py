#!/usr/bin/python3
""" Consile for AirBnB clone """

import cmd
from models.base_model import BaseModel
from models.__init__ import storage
import re


class HBNBCommand(cmd.Cmd):

    prompt = '(hbnb) '

    def do_EOF(self, arg):
        """ Quits Gracefully with EOF """
        print()
        return True

    def do_exit(self, arg):
        """ Exits the interpretor """
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
