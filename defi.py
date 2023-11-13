a = 'The quick brown fox jumps over the lazy dog'
k = 13
temp = []
res = [] 
for i in a:
    temp.append(ord(i))
for i in temp:
    if 65 <= i <= 90:  
        if i + k > 90:
            i = 64 + (i + k - 90)
            res.append(chr(i))
        else:
            i = (i + k) 
            res.append(chr(i))
    elif 97 <= i <= 122:  
        if i + k > 122:
            i = 96 + (i + k - 122)
            res.append(chr(i))
        else:
            i = (i + k) 
            res.append(chr(i))
    else:
        res.append(chr(i))  
print(''.join(res))