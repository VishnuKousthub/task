def isogram(s):
    a=[]
    for i in s:
        if i.isalpha() and i in a:
            return False
        a.append(i)
    return True

s='six-year - old'
print(isogram(s))