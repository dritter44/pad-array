#REMEMBER TO PSEUDOCODE
def pad(array, min_size, value = None):
    #establish case that if the min array size is less than or equal to the current array size, return the current array
    if len(array) == min_size:
        return array
    #establish the case where the min array size is greater than the array length
    else:
        for x in range(min_size-len(array)):
            array.append(value)
    return array
#print(pad([1,2,3], 5, 'apple'))
