def number_pattern(n):
    if not isinstance(n,int):
        return "Argument must be an integer value"
    if n < 1:
        return "Argument must be an integer greater than 0"
    
    patt = ""
    for i in range(1, n+1):
        if i == n:
            patt = patt + str(i)
        else:
            patt = patt + str(i) + " "
    return patt

print(number_pattern(100))