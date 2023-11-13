
def isogram(n):
    n=n.replace(' ', '').replace('-', '')
    for i in n:
        if n.count(i) > 1:
            return False
    return True
n=isogram('six-year-old') 
print(n)

