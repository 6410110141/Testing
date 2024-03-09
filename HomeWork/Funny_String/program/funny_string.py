def funnyString(s:str):
    lst_s = [ord(i) for i in s]
    lst_r = lst_s.copy() # copy list s to list r
    lst_r.reverse() # reverse list r
    n = len(lst_r)
    for i in range(n-1):
        x = abs(lst_s[i]-lst_s[i+1])
        y = abs(lst_r[i]-lst_r[i+1])
        if x!=y :
            return "Not Funny"
    return "Funny"
