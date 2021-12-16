def my_func(x):
    try:
        data = int(x)
    except ValueError:
        raise ValueError("wrong type of data inputted")
    return data+1


if __name__ == "__main__":
    print(f"result is {my_func(2)}")
    print(f"result is {my_func('s')}")
