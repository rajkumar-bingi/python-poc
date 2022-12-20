'''
JSON : Java Script Object Notation
=> JSON is data exchange format similar to XML

In JSON Module ,it will have two methods:

1. dumps(): it will take python file,python object as a input and converts into a JSON string
2. loads(): it will take JSON string file as a input and it can parse it to Python object 

'''
# importing json module:
import json

# creating a file:
book = {}
book['rak'] = {
    'name': 'Rak',
    'address': '1 street HYD',
    'phone': 12345
}
book['reddy'] = {
    'name': 'Reddy',
    'address': '2 street HYD',
    'phone': 54321
}

# converting into JSON string using dumps()
s = json.dumps(book)
# print(s)

# writing into file
with open("https://github.com//rajkumar-bingi//python-poc//json-book.txt", "w") as f:
    f.write(s)

# parse it into python object:
r = json.dumps(s)
print(r)
