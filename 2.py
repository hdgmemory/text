# import re
# text = "1.txt"
# with open(text,"r")as fp:
#     f = fp.read()
#     frequency = {}
#     c = re.split(r'\W+',f)
#     c = [i.lower() for i in c if len(i) > 0]
#     # print(c)
#     c = [i for i in c if len(i)>0]
#     # print(c)
#     for i in c:
#         if i in frequency:
#             frequency[i]+=1
#         else:
#             frequency[i]=1
#     for word in text.split():
#         if word not in frequency:
#             frequency[word] = 1
#         else:
#             frequency[word] += 1
#     print(frequency)
#

import re
str = input("请输入字符串：")
def find(str):
    frequency = {}
    list1 =[]
    list2 = []
    c = re.split(r'\W+',str)
    c = [i.lower() for i in c if len(i) > 0]
    c = [i for i in c if len(i)>0]
    for i in c:
        if i in frequency:
            frequency[i]+=1
        else:
            frequency[i]=1
    for k,v in frequency.items():
        list1.append(k)
        list2.append(v)
    dt1 = zip(list1,list2)
    dt2 = sorted(dt1, key=lambda s: s[0])
    print(dict(dt2))
find(str)