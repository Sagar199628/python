
# list1 = ["Java","Python","Php","Android","Java"]
# list2 = ["Tops",123,145.56,True]
# list3 = list((10,20,30,40,50))

# print(list1[0]) # java
# print(len(list1)) # 5
# print(type(list2)) # list



#Access list
# fruits = ["Mango","Banana","Apple","Orange"]

# print(fruits[1]) #Banana
# print(fruits[-2]) # Apple
# print(fruits[1:3]) #['Banana', 'Apple']
# print(fruits[2:]) #['Apple', 'Orange']
# print(fruits[:3]) #['Mango', 'Banana', 'Apple']
# print(fruits[-3:-1]) #['Banana', 'Apple']
# print("Banana" in fruits) #True

#Change list items
# fruits = ["Mango","Banana","Apple","Orange"]
# fruits[1] = "Kiwi" #['Mango', 'Kiwi', 'Apple', 'Orange']
# fruits[1:3] = ["Kiwi","Grapes","Draganfruit"] #['Mango', 'Kiwi', 'Grapes', 'Draganfruit', 'Orange']
# fruits.insert(1,"Kiwi") #['Mango', 'Kiwi', 'Kiwi', 'Grapes', 'Draganfruit', 'Orange']
# print(fruits)

#Add Items in list
# sports = ["Cricket","Football","Vollyball","Hockey","Tennis"]
# sports.insert(2,"Kabbaddi") #['Cricket', 'Football', 'Kabbaddi', 'Vollyball', 'Hockey', 'Tennis']
# sports.extend("abc") #['Cricket', 'Football', 'Kabbaddi', 'Vollyball', 'Hockey', 'Tennis', 'a', 'b', 'c']
# sports.extend(["chess","Carram","Ludo"]) #['Cricket', 'Football', 'Vollyball', 'Hockey', 'Tennis', 'chess', 'Carram', 'Ludo']
# sports.extend(123) - Not possible

# print(sports)

#Remove list items
# cars= ["Alto","Centro","Swift","jaz","innova","Fortuner"]

# cars.remove("Alto") #['Centro', 'Swift', 'jaz', 'innova', 'Fortuner']
# cars.pop(3) #['Alto', 'Centro', 'Swift', 'innova', 'Fortuner']
# cars.pop() #['Alto', 'Centro', 'Swift', 'jaz', 'innova']
#del cars[1] #['Alto', 'Swift', 'jaz', 'innova', 'Fortuner']
# del cars()
# cars.clear() #[]
# print(cars)

#Loop list
# for i in cars:
    # print(i)

# for i in range(len(cars)):
    # print(cars[i])


# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# newlist = []
# for i in fruits:
#     if "a" in i:
#         newlist.append(i)


# newlist = [i for i in fruits if "a" in i]
# newlist = [i.upper() for i in fruits if i != "apple"]
# newlist = ["abc" for i in fruits]

# newlist = [x if x != "banana" else "orange" for x in fruits]

# print(newlist)


# fruits = ["apple", "banana", "kiwi", "mango","cherry"]

# fruits.sort(reverse=True)
# fruits.reverse()
# print(fruits)

# k = fruits.copy()
# k = list(fruits)
# print(k)


# l1 = [1,2,3,4,5,2,2]
# l2 = [10,20,30,40,50]

# l3 = l1+l2

# for a in l1:
#     l2.append(a)

# print(l2)

# print(l1.count(2))

# print(l1.index(5))



# Tuppledemo.py
# l = ["Hello"]
# print(l)
# tpl = ("Hello",)
# print(tpl)

# l = list(t)
# l.append("SQL")
# t = tuple(l)
# print(t)

# x = ("test","tech")
# y = ("abc","xyz")

# x +=y
# print(x)

# fruits = ("apple", "banana", "cherry")

# (a,*b) = fruits

# print(b)

# a = {1,2,3,4,5}
# b = {3,4,5,6}
# c = {10,20,30,40}
# k = a.union(b)
# print(k)
# a.update(b)
# a.update(c)

# k = a.intersection(b)
# a.intersection_update(b)
#
# k= a.difference(b)
# print(k)
# a.difference_update(b)
#
# k = a.symmetric_difference(b)

# print(a)

