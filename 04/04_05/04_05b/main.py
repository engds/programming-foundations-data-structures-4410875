def has_unique_characters(data):
#alternative way to convert data to set is by using
# unique_data = set(data) - Time complexity is same O(n)
# return len(data) == len(unique_data)

    character_set = set([])
    for char in data:
        character_set.add(char)
    
    if len(data) == len(character_set):
        return True
    return False

print(has_unique_characters('sample'))
print(has_unique_characters('hello world'))
print(has_unique_characters('linkedin'))
print(has_unique_characters('python'))
