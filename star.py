#   #                      ------- star pattern----------
# *
# **
# ***
# ****
# *****
# print this pattern
# i=1
# while i<=6:
#     j=1
#     while j<=6:
#         if(j<i):
#             print("*",end='')
#         j+=1
#     print()
#     i+=1        


#  *****
#   ****
#    ***
#     **
#      *
# i=1
# while i<=4:
#     j=1
#     while j<=4:
#         if(j>=i):
#             print("*",end='')
#         else:
#             print(" ",end='')    
#         j+=1
#     print()
#     i+=1     



# ****
# ***
# **
# *
# i=1
# while i<=4:
#     j=1
#     while j<=4:
#         if(j<=5-i):
#             print("*",end='')
#         j+=1
#     print()
#     i+=1        

# #  
#       *
#      ***
#     *****
#    *******   
# i=1
# while i<=4:
#       j=1
#       while j<=7:
#             if(j>=5-i and j<=3+i):
#                   print("*",end='')
#             else:
#                   print(" ",end='')        
#             j+=1
#       print()
#       i+=1    

# *******
#  ***** 
#   ***  
#    *                                     
# i=4
# while i>=1:
#       j=7
#       while j>=1:
#             if(j>=5-i and j<=3+i):
#                   print("*",end='')
#             else:
#                   print(" ",end='')        
#             j-=1
#       print()
#       i-=1    

#    1
#    0 1
#    0 1 0
#    1 0 1 0
# flag=1
# i=1
# while i<=4:
#       j=1
#       while j<=4:
#             if(j<=i):
#                   print(int(flag),end='')
#                   flag= not flag             
#             j+=1
#       print()
#       i+=1   
# 1
# 1 0
# 1 0 1
# 1 0 1 0
# i=1
# while i<=4:
#       j=1
#       flag=1
#       while j<=4:
#             if(j<=i):
#                   print(int(flag),end='')
#                   flag=not flag
#             else:
#                   print(' ',end=' ')     
#             j+=1
#       print()      
#       i+=1             


#reverse number programe---

# k=int(input("enter your value:"))
# sum=0
# while(k!=0):
#       rem=k%10
#       sum=sum*10+rem
#       k//=10
# print(sum)

# A   
# AA  
# AAA 
# AAAA


# for i in range(1,5):
#       for j in range(1,5):
#             if(j<=i):
#                   print("A",end='')
#             else:
#                   print(" ",end='') 
#       print()                 

