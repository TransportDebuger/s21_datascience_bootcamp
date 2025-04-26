def data_types():
    a = 42
    b = "Hello"
    c = 3.14
    d = True
    e = [1, 2, 3]
    f = {'a': 1}
    g = (1, 2)
    h = {1, 2, 3}
    type_names = [type(var).__name__ for var in (a, b, c, d, e, f, g, h)]
    print("[{}]".format(", ".join(type_names)))

if __name__ == '__main__':
    data_types()