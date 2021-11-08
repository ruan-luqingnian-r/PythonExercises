# 整型：可正可负，不带小数点，在python3中，整型没有大小限制，也可以储存长整型
# 浮点型：可正可负，带小数点，可以使用课学计数法表示，如1.1e2 = 110
# 复数：复数可由虚部和实部组成，可以用a + bj，或者complex(a,b),复数的实部和虚部都是浮点型
# 数字类型不可变
a = 1
print(id(a))
print(a)
a = 1.0
print(id(a))
print(a)
print("===========")
print(1.1e2)
print(type(1))
print(type(1.1))
print(type(1.1e2))