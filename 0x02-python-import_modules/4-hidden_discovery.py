#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    namees = dir(hidden_4)
    for name in names:
        if name[0:2] != "__":
            print("{}".format(name))
