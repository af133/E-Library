# # # from collections import Counter
# # # a=input().split(' ')
# # # print(Counter(a))
# # # from collections import defaultdict
# # # a=defaultdict(list)
# # # dibagi=input().split()
# # # for v, i in enumerate(dibagi):
# # #     for j in range(int(i)):
# # #         if dibagi[0]==i:
# # #             inputan=input()
# # #             a[inputan].append(v+1)
# # #         else:
# # #             inputan=input()
# # #             ada=False
# # #             for g, value in enumerate(a):
# # #                 if value[0]==inputan:
# # #                     ada=True
# # #             if ada==True:
# # #                 print(' '.join((str(x))for x in value[1]))
# # #             else:
# #                 # print(-1)
# from collections import defaultdict
# a=defaultdict(list)
# dibagi=input().split()
# v=0
# simpan=[]
# for z, i in enumerate(dibagi):
#     for j in range(int(i)):
#         if z==0:
#             inputan=input()
#             v+=1
#             a[inputan].append(str(v))
#         else:
#             inputan=input()
#             simpan.append(inputan)
# for j in simpan:
#     b=a[j]
#     if bool(b)==True:
#         print(' '.join(str(x) for x in b))
#     else:
#         print(-1)
# print(1/2)
# from collections import namedtuple
# Point = namedtuple('Point','x,y')
# pt1 = Point(1,2)
# pt2 = Point(3,4)
# print(pt1,'\n',pt2)
# dot_product = ( pt1.x * pt2.x ) +( pt1.y * pt2.y )
# print (dot_product)
#!/bin/python3

a=[3,4,8,2]
min=min(a)
v=[]
for i in a:
    if (i% min)==1:
        v.append(i) 
    else:
        v.append(i//min) 
# print(v)
a=[1,2]
b=[2,2]
if a==b:
    print('oke')
else:
    print('ooo')