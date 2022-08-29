from unittest import result

#function to return all permuations of string of length 3
def permutations(mystring):
    if len(mystring) == 1: #if length of string is 1 it return the string itself
        return mystring


    perms = permutations(mystring[1:])  #recurssive call 
    char = mystring[0] #first letter 
    result = []

    for perm in perms:
        for i in range(len(perm) +1):
            result.append(perm[:i] + char + perm[i:]) #keeps the char in all the possible positions
    return result
print(permutations('abc'))
