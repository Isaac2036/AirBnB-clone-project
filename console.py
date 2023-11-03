#!/usr/bin/python3
"""
Este módulo expone la clase
HBNBCommand(cmd.Cmd)
"""
import cmd
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """
    Esta clase hereda de cmd.Cmd, desde aqui se gestionará
    nuestro proyecto.
    """
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program\n"""
        return True

    def do_EOF(self, arg):
        """Quit command to exit the program\n"""
        return True

    def emptyline(self):
        pass

    def do_create(self, arg):

        if not arg:
            print("** class name missing **")
        elif arg == "BaseModel":
            bs = BaseModel()
            bs.save()
            print(f"{bs.id}")
        else:
            print("** class doesn't exist **")

    def do_show(self, arg):
        pass

    def do_destroy(self, arg):
        pass

    def do_all(self, arg):
        pass

    def do_update(self, arg):
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
