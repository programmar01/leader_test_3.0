#meeqvse codewars 6 kiu
#Sum of nested numbers





def sum_nested_numbers(arr):
    final_sum = 0
    listn = []

    for i in arr:
        listn.append(i)
        i = str(i)
        cb = i.count("]")
        i = i.replace("]", "")
        i = i.replace("[", "")
        if i == 0:
            return 0
        else:
            final_sum += int(i) * int(cb)
    
    return final_sum