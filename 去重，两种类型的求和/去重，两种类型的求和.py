nums = [0, 1, 'user_input', '2x', '2', '3', '3', '2', '6', '7', '9', '9']
result = 0
for num in set(nums):
    if type(num) == int or num.isdigit():
        result += int(num)
print(result)
#或者也以用reduce函数
# reduce(lambda x,y: x+y, [int(i) for i in set(nums) if type(i)==int or i.isdigit()])
# #或使用sum函数
# sum([int(i) for i in set(nums) if type(i)==int or i.isdigit()])
