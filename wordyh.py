def answer(question):
    words = question.split()

    if "cubed" in words or "President" in words:
        raise ValueError("unknown operation") 
    
    result = 0
    op = None

    for i,word in words:
        if word == 'what' or word == 'is' or word == '?' or word == 'by':
            continue
        if word.isdigit() or (word[0] == '-' and word[1:].isdigit()):
            if op == "plus":
                result += int(word)
            elif op == "minus":
                result -= int(word)
            elif op == "multiplied":
                result *= int(word)
            elif op == "divided":
                result /= int(word)
            else:
                result = int(word)
        elif word in ["plus", "minus", "multiplied", "divided"]:
            if i > 0 and words[i - 1] in ["plus", "minus", "multiplied", "divided"]:
                raise ValueError("syntax error - consecutive operations")
            op = word
        else:
            raise ValueError("syntax error")

    return int(result)

try:
    res = answer(" what is 5 plus 13 plus 6 ?")
    print(res)

except ValueError as e:
    print(e)