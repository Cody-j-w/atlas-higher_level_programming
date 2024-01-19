#!/usr/bin/python3

"""
Module containing MyList subclass of list object
"""


class MyList(list):
    """
    The Mylist class, inherits from list class
    """

    def print_sorted(self):
        """
        print_sorted prints the list it belongs to, sorted low to high
        """
        temp_list = []
        for i in self:
            temp_list.append(i)
        for i in range(len(temp_list)):
            min = temp_list[i]
            mindex = i
            for j in range(i, len(temp_list)):
                if temp_list[j] < temp_list[mindex]:
                    min = temp_list[j]
                    mindex = j
            if mindex != i:
                temp_list[mindex] = temp_list[i]
                temp_list[i] = min
        print(temp_list)
