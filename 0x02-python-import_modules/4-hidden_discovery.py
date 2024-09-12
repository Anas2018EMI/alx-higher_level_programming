#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    items = dir(hidden_4)
    a = len(items)
    for i in range(1, a):
        if items[i][:2] != "__":
            print(items[i])
