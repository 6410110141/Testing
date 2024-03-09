def alternate(s):
    chars = set(s)#เอาตัวซ้ำออก
    mx = 0
    for c1 in chars:
        for c2 in chars:
            if c1!=c2 :
                text = ''
                for t in s :
                    if t in (c1,c2):
                        if text==''  or t != text[-1] :
                            text += t
                        else :
                            text = ''
                            break
                if len(text) > mx :
                    mx = len(text)
    return mx
