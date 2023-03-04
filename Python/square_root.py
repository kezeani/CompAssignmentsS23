import math

def square_root(n):
    if not str(n).isdigit():
        return -1
    else:
        return math.sqrt(n)

def test():
    assert square_root(4) == 2
    assert square_root(0) == 0
    assert square_root("hello") == -1
    assert square_root(-10) == -1
    print("Success!")

if __name__ == "__main__":
    test()
