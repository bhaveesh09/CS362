
def reverse_string(x):
    return x[::-1]

def target_sum(array, target):
    temp = {}
    for i in range(len(array)):
        if target - array[i] in temp:
            return [temp[target - array[i]], i]
        else:
            temp[array[i]]=i
