#coding=utf8
# nums = range(2,20)
# for i  in nums:
#     nums=filter( lambda x :x==i or x%i,nums)
# print(nums)
# print(type(nums))


# import re
# a = 'abbbccc'
# b = re.sub(r'b+','b',a)
# print(b)


# print(dir('a'))

# a = [1,2,4,3,6,5]
# b = [2,2,3,6,7,8,9]
# c = set(a)^set(b)
# d = set(a)&set(b)
# print(list(d))
# print(list(c))


# name = 'huodongge'
# print(name[::-1])


# a=1
# b=2
# a,b=b,a
# print(a,b)
#
# def index(list,k):
#     if k<list[0]:
#        position = 0
#     elif k>list[-1]:
#         position = len(list)-1
#     else:
#         position = 0
#         for l in list:
#             if k>l:
#                 position+=1
#     return position
# list = [1,2,4,5,7,8]
# print(index(list,3))




# #装饰器
# def warp(name):
#     def decorator(func):
#         def dec(*args):
#             print(name)
#             print("aaaaaaaaa")
#             b = func(*args)
#             print('bbbbbbbb')
#             return b
#         return dec
#     return decorator
#
#
# @warp('f1')
# def fak(c):
#     print(c)
#
# fak('c')

#
# d={'a':24,'g':52,'l':12,'k':33}
# result = sorted(d.items(),key=lambda x:x[1],reverse=True)
# print(result)
# print(dict(result))

# a=[('小明',3),('小红',2),('小东',4)]
# b=[('小明',3),('小东',1)]
# e=[('小明',2),('小东',1)]
# c=[a,b,e]
# b={}
# #结果
# #c=[('小明',6),('小红',2),('小东',1)]
#
# for i in c:
#     #print(i)
#     for k,v in i:
#         if k in b:
#             b[k]+=v
#         else:
#             b[k]=v
#
# print(b)

# import re
# text = "I'm a hand     some boy        hand !"
# frequency = {}
# c = re.split(r'\W+',text)
# print(c)
# c = [i for i in c if len(i)>0]
# print(c)
# for i in c:
#     if i in frequency:
#         frequency[i]+=1
#     else:
#         frequency[i]=1
#
# print(frequency)

# for word in text.split():
#     if word not in frequency:
#         frequency[word] = 1
#     else:
#         frequency[word] += 1
# print(frequency)



import collections

text = "I'm a hand some boy  some !"
frequency = collections.Counter(text.split())
print(frequency)


# s1="aa bb  cc"
# a = s1.split('  ')
# print(a)
#

# import re
# a = 'This is an apple. Do you like apple?'
# b = re.split(r'\W+',a)
# c = [i.lower()for i in b if len(i)>0]
# print(c)
import re
with open('1.txt','r')as fp:
   f = fp.read()
print(f)
b = re.split(r'\W+',f)
print(b)
c={}
for i in b:
    if i in c:
        c[i]+=1
    else:
        c[i]=1
print(c)