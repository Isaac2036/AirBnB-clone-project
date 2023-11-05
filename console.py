#!/usr/bin/python3
"""
Este módulo expone la clase
HBNBCommand(cmd.Cmd)
"""
import cmd
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """
    Esta clase hereda de cmd.Cmd, desde aqui se gestionará
    nuestro proyecto.
    """

    prompt = "(hbnb) "
    __BASE_MODEL = "BaseModel"
    __CLS_NAME_MISSING = "** class name missing **"
    __CLS_NOT_EXIST = "** class doesn't exist **"
    __ID_MISSING = "** instance id missing **"
    __NO_INST_FOUND = "** no instance found **"

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
            print(HBNBCommand.__CLS_NAME_MISSING)
        elif arg == HBNBCommand.__BASE_MODEL:
            bs = BaseModel()
            bs.save()
            print(f"{bs.id}")
        else:
            print(HBNBCommand.__CLS_NOT_EXIST)

    def do_show(self, arg):
        args = arg.split()

        if not args:
            print(HBNBCommand.__CLS_NAME_MISSING)
        elif args[0] != HBNBCommand.__BASE_MODEL:
            print(HBNBCommand.__CLS_NOT_EXIST)
        elif len(args) <= 1:
            print(HBNBCommand.__ID_MISSING)
        else:
            storage.reload()
            bms = storage.all()
            for bs in bms.values():
                if bs.id == args[1]:
                    print(bs)
                    break
            else:
                print(HBNBCommand.__NO_INST_FOUND)

    def do_destroy(self, arg):
        args = arg.split()

        if not args:
            print(HBNBCommand.__CLS_NAME_MISSING)
        elif args[0] != HBNBCommand.__BASE_MODEL:
            print(HBNBCommand.__CLS_NOT_EXIST)
        elif len(args) <= 1:
            print(HBNBCommand.__ID_MISSING)
        else:
            storage.reload()
            bms = storage.all()
            for k, bs in bms.items():
                if args[1] == bs.id:
                    del bms[k]
                    break
            # storage.save()
            else:
                print(HBNBCommand.__NO_INST_FOUND)

    def do_all(self, arg):
        args = arg.split()

        if not args:
            storage.reload()
            bms = storage.all()
            print([str(bs) for bs in bms.values()])
        elif len(args) == 1:
            if args[0] != HBNBCommand.__BASE_MODEL:
                print(HBNBCommand.__CLS_NOT_EXIST)
            else:
                storage.reload()
                bms = storage.all()
                print([str(bs) for bs in bms.values()])

    def do_update(self, arg):
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
