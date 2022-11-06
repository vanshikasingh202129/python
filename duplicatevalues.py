#list = input("enter the list of nos.")

def find_dupli(lis):
	uniqueList = []
	duplicateList = []

	for i in lis:
		if i not in uniqueList:
			uniqueList.append(i)
		elif i not in duplicateList:
			duplicateList.append(i)
	return duplicateList

lis = [1, 2, 1, 2, 3, 4, 5, 1, 1, 2, 5, 6, 7, 8, 9, 9]
print(find_dupli(lis))
