def camelcase(s):
    count = 0
    for l in s:
        if l.isupper() == True:
           count+=1
    return count + 1