#!/usr/bin/python3

class MyList(list):

    def print_sorted(self):
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
