# mexute codewars 6 kiu
#Unique In Order




def unique_in_order(sequence):
    listn = []
    for item in sequence:
        if len(listn) < 1 or not item == listn[len(listn) -1]:
            listn.append(item)
    return listn