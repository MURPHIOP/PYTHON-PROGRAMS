original_dict = {'a':1, 'b':2, 'c':3}
keys = ['a', 'c']

new_dict = dict((k, original_dict[k]) for k in keys if k in original_dict)
print(new_dict)
