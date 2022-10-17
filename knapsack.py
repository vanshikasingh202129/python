import re


weight = int(input("enter the sack weight: "))
w_values = (input("enter the weight of items: "))
w_values = w_values.split()
w_values = [int(x) for x in w_values]

Profit = (input("enter the profit value: "))
Profit = Profit.split()
Profit = [int(y) for y in Profit]

s_a = [(w_values[i], Profit[i]) for i in range(0,len(Profit))]
arr = sorted(s_a,key=lambda i: i[1],reverse=True)
print(arr)

def knapsack(sack_size,arr):

    total_profit = 0

    for item in arr:
        if item[0] <= sack_size:
            total_profit += item[1]
            sack_size -= item[0]

    return total_profit

knapsack1 = knapsack(weight,arr)
print(knapsack1)


