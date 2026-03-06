def simple_hash(s):
    
    hash_value = 0
    for char in s:
        hash_value += ord(char)  
    return hash_value

print(simple_hash("hello"))
print(simple_hash("world"))
print(simple_hash("Python"))