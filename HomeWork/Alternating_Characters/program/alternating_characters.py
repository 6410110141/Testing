def alternatingCharacters(s):
    deleteCount = 0
    for i in range(1,len(s)):
        if s[i] ==  s[i-1]:
            deleteCount+=1
    return(deleteCount)
