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
pldrome1=palindrome('CDOZVZOROBA')
pldrome1.substring()
print(pldrome1.unique_set)