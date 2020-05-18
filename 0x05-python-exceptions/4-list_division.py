def list_division(my_list_1, my_list_2, list_length):
    _list = []
    for i in range(list_length):
        try:
            r = 0
            r = my_list_1[i] / my_list_2[i]
        except TypeError:
            print("wrong type")
        except ZeroDivisionError:
            print("division by 0")
        except IndexError:
            print("out of range")
        finally:
            _list.append(r)
    return(_list)
