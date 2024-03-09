def caesarCipher(s, k):
    alphabet_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    alphabet_lower = alphabet_upper.lower()
    text = ''
    for i in s :
        if i in alphabet_upper :#mod 26 ในกรณีที่บวกค่า k เเล้ว index เกินจำนวนตัวอักษร eng
            text += alphabet_upper[(alphabet_upper.index(i) + k)%26]
        
        elif i in alphabet_lower :
            text += alphabet_lower[(alphabet_lower.index(i) + k)%26]
        else :
            text += i#กรณีไม่ใช่ตัวอักษร
    return text

print(caesarCipher('xdfhgdfghdfdle-Outdhdfhsdfbz',10))
