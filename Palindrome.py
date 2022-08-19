#def check_palindrome(my_str):
#    if my_str==my_str[::-1]:
#        return True
#    else:
#        return False
#
#def cutout_string(my_string,i_index):
#    f_index_list = []
#    for f_index in range(i_index+1,len(my_string)):
#        if my_string[i_index] == my_string[f_index]:
#            f_index_list.append(f_index)
#    return f_index_list
#
#end_list=cutout_string('VANAVASNAV',0)
#
#
#slice_str=[]
#for f in end_list:
#    slice_str.append('VANAVASNAV'[0:f+1])
#print(slice_str)
#
#for st in slice_str:
#    if check_palindrome(st):
#        print(st)
#

# Function to check palindrome
#def ispalindrome(str):
#    for i in range(0,int(len(str)/2)):
#        if str[i]!=str[len(str)-i-1]:
#            return False
#    return True
## Function to print palindromic sub-strings            
#def printallpalindrome(str):
#    if (len(str)<2):
#        return True
#    for i in range(0,len(str)):
#        for j in range(i+1,len(str)+1):
#            s = str[i : j+1]
#            if(ispalindrome(s)):
#                print(s)
#
#print(printallpalindrome('avanaava'))

# Expand in both directions of low and high to find all palindromes
#def expand(s, low, high, palindromes):
# 
#    # run till s[low.high] is not a palindrome
#    while low >= 0 and high < len(s) and s[low] == s[high]:
# 
#        # push all palindromes into a set
#        palindromes.add(s[low: high + 1])
# 
#        # Expand in both directions
#        low = low - 1
#        high = high + 1
#  
## Function to find all unique palindromic substrings of a given string
#def findPalindromicSubstrings(s):
# 
#    # create an empty set to store all unique palindromic substrings
#    palindromes = set()
# 
#    for i in range(len(s)):
# 
#        # find all odd length palindrome with s[i] as a midpoint
#        expand(s, i, i, palindromes)
# 
#        # find all even length palindrome with s[i] and s[i+1]
#        # as its midpoints
#        expand(s, i, i + 1, palindromes)
# 
#    # print all unique palindromic substrings
#    print(palindromes, end='')
# 
# 
#if __name__ == '__main__':
# 
#    s = 'Sabaduda'
#    findPalindromicSubstrings(s)
# 

class palindrome:
    def __init__(self,string):
        self.str1=string
        self.unique_set=set()
    def substring(self):
        i = 0
        while i <len(self.str1):
            j = len(self.str1) - 1
            while (j>i):
                if self.str1[i] == self.str1[j]:
                    if self.is_palindrome(i,j):
                        self.unique_set.add(self.str1[i:j+1])
                        i = (i+j)//2
                        break
                j -= 1
            i+=1
    def is_palindrome(self,strt,end):
        while(strt<=end):
            if(self.str1[strt]==self.str1[end]):
                strt+=1
                end-=1
            else:
                return False
        return True
string="abcbadefeda"
pldrome1=palindrome(string)
pldrome1.substring()
print(pldrome1.unique_set)