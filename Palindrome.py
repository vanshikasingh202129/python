def check_palindrome(my_str):
    if my_str==my_str[::-1]:
        return True
    else:
        return False

def cutout_string(my_string,i_index):
    f_index_list = []
    for f_index in range(i_index+1,len(my_string)):
        if my_string[i_index] == my_string[f_index]:
            f_index_list.append(f_index)
    return f_index_list

#end_list=cutout_string('VANAVASNAV',0)


slice_str=[]
for f in end_list:
    slice_str.append('VANAVASNAV'[0:f+1])
print(slice_str)

for st in slice_str:
    if check_palindrome(st):
        print(st)
