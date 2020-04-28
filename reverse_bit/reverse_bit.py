def to_bits(n):
    return '{0:08b}'.format(n)

def reverse_num_bits(n):
    s=to_bits(n)
    lst=[int(x) for x in s]
    lst.reverse()
    l=32-len(lst)
    if(l==0):
        res = int("".join(str(x) for x in lst), 2)
        return res
    else:
        lst1=[0 for i in range(l)]
        lst.extend(lst1)
        print(len(lst))
        res = int("".join(str(x) for x in lst), 2)
        return res
print(to_bits(1234))
# 10011010010
print(reverse_num_bits(1234))
# 1260388352
print(to_bits(reverse_num_bits(1234)))
# 1001011001000000000000000000000