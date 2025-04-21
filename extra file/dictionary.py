# person = {
#     "name":"Sagar",
#     "email":"sagar@gmail.com",
#     "phone": ["989874858","7485858596"]
#     # "name":"Swapnil"   not allowed
#
# }

# print(person['phone'])
# print(person.get("name"))

# print(person.keys())

# person['name'] = "meet"

# print(person)

# print(person.values())
# print(person.items())
# print(person)

# person = {
#     "name" : "Sagar",
#     "email": "sagarkhodiyar6@gmail.com",
#     "phone": "930020293",
#     "address" : {
#         "country" : "India",
#         "state" : "gujarat",
#         "city" : "surat"
#     }
# }
# print(person['phone'])
# print(person.get("name"))
# print(person.key())
# person['name'] = "meet"


a = 10
def test():
    global a
    a = 20
    print(a)

print(a)
test()
print(a)

