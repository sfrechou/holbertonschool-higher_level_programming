#!/usr/bin/python3
import hidden_4
if __name__ == "__main__":
    contenido = dir(hidden_4)
    for name in contenido:
        if name[:2] != "__":
            print("{}".format(name))
