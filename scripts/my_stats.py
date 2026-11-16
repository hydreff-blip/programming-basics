def average(numbers):
    if len(numbers) == 0:
        print("Empty list, please enter some numbers")
    elif len(numbers) != 0:
        total = 0
        for n in numbers:
            total +=n
        return total/len(numbers)

#def int_or_float(number):



#minimum(numbers):
#    min = 0
#    for n in numbers:
#        min = n
#        if n+1 < n:
#            min = n+1
#    return min