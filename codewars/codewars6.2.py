def sum_nested_numbers(arr):
    final_sum = 0
    listn = []
    
    for i in arr:
        listn.append(i)
        count_brackets = listn.count("]")
        i = i.replace("]", "")
        i = i.replace("[", "")
    final_sum += i * count_brackets   
    
    
    # return final_sum

    print(i)

sum_nested_numbers([1, 2, [3, 4], [5, [6, 7], 8], 9])