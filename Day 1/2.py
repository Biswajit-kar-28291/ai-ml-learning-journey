
# Functions
# Lists
# Dictionaries

# def f(a):
#     return max(a)
# a=[i for i in range (10)]
# print(f(a))

# l=[11,2,4,5,8,7,7,9,9,3,2,3]
# l=list(set(l))
# print(l)

# l=[11,2,4,5,8,7,7,9,9,3,2,3]
# a={}
# for i in l:
#     a[i]=a.get(i,0)+1
# print(a)


# from collections import Counter

# print(Counter(l))

# l=[11,2,4,5,8,7,7,9,9,3,2,3]
# l.sort(reverse=True)

# print(l)

##########################################
# 1.

# Find second largest number

l = [5, 1, 4, 3]
a=0
b=0
for i in l:
    if a<i:
        a=i
    elif b<i and i!=a:
        b=i
       
print("second largest elemtn is :" ,b)