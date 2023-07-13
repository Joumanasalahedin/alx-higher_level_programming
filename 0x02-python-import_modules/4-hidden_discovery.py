#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
sorted_list = sorted(dir(hidden_4))
for name in sorted_list:
    if name[0] != '_' and name[1] != '_':
        print(name)
