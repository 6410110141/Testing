def staircase(size, display):
    if 0 < size <= 30:
        text = ''
        for i in range(1, size+1):
            text += (' '*(size-i) + f'{display}'*i + '\n')
            
        return text
