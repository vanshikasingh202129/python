from msilib.schema import CustomAction


class Stack:
    def __init__ (self):
        self.list=[1,2,3,4]
    #to check if list is empty or not
    def isEmpty(self):
        if self.list == []:
           return True
        else:
            return False
    #insert element
    def push(self,value):
        self.list.append(value)
        return self.list
    #delete topmost element
    def pop(self):
        if self.isEmpty():
            return "empty"
        else:
         return self.list.pop()
    #display topmost element
    def peek(self):
        if self.isEmpty():
            return "empty"
        else:
            return self.list[len(self.list)-1]
    def delete(self):
        self.list = None
customStack = Stack()
print(customStack.isEmpty())
print(customStack.push(6))
print(customStack.pop())
#print(customStack)
print(customStack.peek())