#1
# s = "Python"

# s1 = s[::-1]
# print(s1)
#2
# lst = [int(num) for num in input().split()]

# big = lst[0]

# for i in lst:
    # if i>big:
        # big = i
# print(big)
#3
# s = input('Enter Your Word:')

# s1 = s[::-1]

# if s1 == s:
    # print('palindrome')
# else:
    # print('Not palindrome')    
#4
# lst = [int(num) for num in input().split()]

# sum = 0

# for i in lst:
    # sum = sum+i

# print(sum)
#5

lst = [1,2,3,5,6]
max = max(list(set(lst)))

for i in range(1,max+1):
    if i not in lst:
        print(i)


