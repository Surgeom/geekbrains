arr = [None, 1, IndexError, 'sometxt', b'\x00', [1, 2], (1, 2), {2, 3}, {'a': 1, 'b': 2}]
for element in arr:
    print(type(element))
