def swap_case(s):
    res = ""
    for i in s:
        if i.isalpha():
            if i.isupper():
                i = i.lower()
                res = res+i
            elif i.islower():
                i = i.upper()
                res = res+i
        else:
            res = res+i
        
    return res

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
