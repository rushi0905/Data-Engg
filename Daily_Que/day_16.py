#How to remove whitespaces from a string in Python?
str = "  Sting with space  "
# strnew=str.replace(" ","")
cleaned_str=str.strip()
print(cleaned_str)

s = "Python is fun"

s = s.replace(" ", "")
print(s)

text = "  example string with spaces  "
cleaned_text = text.strip()
print(cleaned_text)  # Output: "example string with spaces"

print("**************************************************************************")

#Generator function
def fun(max):
    cnt = 1
    while cnt <= max:
        yield cnt
        cnt += 1

ctr = fun(5)
for n in ctr:
    print(n)

print("**************************************************************************")
#Pickling or Unpickling
import pickle

# Sample object
data = {'name': 'John Doe', 'age': 30, 'city': 'New York'}

# Pickling (serialization)
with open('data.pickle', 'wb') as file:
    pickle.dump(data, file)

# Unpickling (deserialization)
with open('data.pickle', 'rb') as file:
    loaded_data = pickle.load(file)

print(loaded_data)
