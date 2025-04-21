
# *****
# *****
# *****
# *****
# *****

# r = 5
# for i in range (r):
#     for j in range (r):
#         print ("*", end= "")
#     print()

# *
# *  *
# *  *  *
# *  *  *  *
# *  *  *  *  *

# r = 5
# for i in range (1,r+1):
#     for j in range (1,i+1):
#         print("*", end="  ")
#     print()

# *  *  *  *  *
# *  *  *  *
# *  *  *
# *  *
# *

# lines = 5
# stars =  lines
#
# for i in range (lines):
#     for j in range (stars):
#         print("*", end="  ")
#     print()
#     stars -=1


#          *
#         **
#        ***
#       ****
#      *****
#     ******
#    *******
#   ********
#  *********
# **********

# lines = 10
# stars = 1
# space = lines-1
#
# for i in range (lines):
#     for k in range (space):
#         print(" ", end="")
#     for j in range (stars):
#         print ("*",end="")
#
#     print()
#     stars +=1
#     space -=1

# **********
#  *********
#   ********
#    *******
#     ******
#      *****
#       ****
#        ***
#         **
#          *


# lines = 10
# stars = lines
# space = 0
#
# for i in range (lines):
#     for k in range (space):
#         print(" ", end="")
#     for j in range (stars):
#         print ("*",end="")
#
#     print()
#     stars -=1
#     space +=1

#     *
#    * *
#   * * *
#  * * * *
# * * * * *


# lines = 5
# stars = 1
# space = lines-1
#
# for i in range (lines):
#     for k in range (space):
#         print(" ", end="")
#     for j in range (stars):
#         print ("*",end=" ")
#
#     print()
#     stars +=1
#     space -=1

       #   *
       #  ***
       # *****
       # *****
       # *****

# lines = 5
# stars = 1
# space = lines-1
# mid = (lines//2)+1
# for i in range (1,lines+1):
#     for k in range (space):
#         print(" ", end="")
#     for j in range (stars):
#         print ("*",end="")
#     print()
#     if i<mid :
#         stars +=2
#         space -=1


         #   *
         #  ***
         # *****
         #  ***
         #   *

# lines = 5
# stars = 1
# space = lines-1
# mid = (lines//2) +1
# for i in range (1,lines+1):
#     for k in range (space):
#         print(" ", end="")
#     for j in range (stars):
#         print ("*",end="")
#     print()
#     if i<mid :
#         stars +=2
#         space -=1
#     else:
#         stars -= 2
#         space += 1

  #   *
  #  * *
  # *   *
  #  * *
  #   *
  #

# lines = 5
# stars = 1
# space = lines-1
# mid = (lines//2) +1
# for i in range (1,lines+1):
#     for k in range (space):
#         print(" ", end="")
#     for j in range (stars):
#         if j==0 or j==stars-1:
#             print ("*",end="")
#         else:
#             print(" ", end="")
#     print()
#     if i<mid :
#         stars +=2
#         space -=1
#     else:
#         stars -= 2
#         space += 1


# lines = 5
# stars = 1
# space = lines-1
# mid = (lines//2) +1
# for i in range (1,lines+1):
#     for k in range (space):
#         print(" ", end="")
#     for j in range (stars):
#         if j==0 or j==stars-1:
#             print ("*",end="")
#         else:
#             print(" ", end="")
#     print()
#         stars +=2
#         space -=1

# *


# r = 5
# for i in range (r):
#     for j in range (r):
#         print ("*", end= "")
#     print()

      #      *
      #     *  *
      #    *     *
      #   *        *
      #  *  *  *  *  *

# lines = 5
# for i in range (1,lines+1):
#     for j in range (1,i+1):
#         if j==1 or j==i or  i==lines:
#             print("*", end="")
#         else:
#             print(" ",end="")
#     print()

# *
# * *
# *   *
# *     *
# * * * * *

# for i in range (5):
#     for j in range (i+1):
#         if j==0 or j==i or i==4:
#             print("*", end=" ")
#         else:
#             print(" ",end=" ")
#     print()

# for i in range (5):
#     for j in range (i,5):
#         print(" ",end="")
#     for j in range (i):
#         print("*",end="")
#     for j in range (i+1):
#         print("*",end="")
#     print()



# for i in range (5):
#     for j in range (i,5):
#         # if j==0 or j==i or  i==4:
#             print(" ", end=" ")
#     for j in range (i+1):
#             print("*",end=" ")
#         # else:
#         #     print(" ",end=" ")
#     print()

# for i in range (5):
#     for j in range (i,5):
#         print(" ",end="")
#     for j in range (i):
#         print("*",end="")
#     for j in range (i+1):
#         print("*",end="")
#     print()

# a = 15
# for i in range (1,11):
#     print(f"{a}x{i}={a*i}")

# area of rectangle = length x width
# l= 5
# w= 5
# area = (l*w)
# print((f"area of rectangle {area} sq mtr"))

# import math
# print(math.sqrt(16))










