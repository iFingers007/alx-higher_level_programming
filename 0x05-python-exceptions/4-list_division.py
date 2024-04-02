#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    if not my_list_1 or not my_list_2:
        print("Input lists cannot be empty")
        return []
    res = []
    try:
        for i in range(list_length):
            num1 = my_list_1[i]
            num2 = my_list_2[i]
            try:
                res.append(num1 / num2)
            except TypeError:
                print("wrong type")
                res.append(0)
            except ZeroDivisionError:
                print("division by 0")
                res.append(0)
    except IndexError:
        print("out of range")
        res.append(0)
    except ValueError:
        print("list cannot be Empty")
    finally:
        return res
