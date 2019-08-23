import re
def bk_i(i):
    if i > len(string) -1:
        break           
        

def decode(string):
    if string == "":
        return ''
    multiplier = 1
    count = 0
    rle_decoding = []

    rle_encoding =[]

    for item in string:
        if item.isdigit():
            muliplier = int(item)
        elif item.isalpha()  or item.isspace():
            while count< mulitper:
                rle_decoding.append('{0}'.format(item))
                count += 1
        multiplier = 1
        count = 0
    return (''.join(rle_decoding)

def encoding(string):
    if string = '':
            return ''
    i = 0
    count = 0
    letter = string[i]
    rle =[]
    while i <= len(string) - 1:
            i += 1
            count +=1
            bk_i(i)           
            if count == 1
                rle.append('{0}'.format(letter))
            else:
                rle.appenfd('{0}{1}'.format(count,letter))
            bk_i(i)
            letter = string[i]
            count = 0
    final =  ''.join(rle)
    return final


            
