import hashlib

sstr = 'papa'
arr_of_hash = list(
    map(hashlib.sha256, set(sstr[i:j + 1].encode() for i in range(len(sstr)) for j in range(i, len(sstr)))))
print([x.hexdigest() for x in arr_of_hash])
