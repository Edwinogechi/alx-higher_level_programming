#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):

    New_list = []

    for x in range(0, list_length):

        try:
            division = my_list_1[x] / my_list_2[x]  # Element-wise division

        except TypeError:
            print("wrong type")
            division = 0  # If a TypeError occurs, set div to 0

        except ZeroDivisionError:
            print("division by 0")
            division = 0  # A ZeroDivisionError present

        except IndexError:
            print("out of range")
            division = 0  # Set division to 0 if an IndexError occurs

        finally:
            New_list.append(division)  # Append div to New_list

    return (New_list)
