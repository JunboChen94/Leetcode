class Solution:
def romanToInt(self, s: str) -> int:
    #1) use list which include two digits symbol
    symbol_digit = [(1000, 'M'),
                    (900,  'CM'),
                    (500,  'D'),
                    (400,  'CD'),
                    (100,  'C'),
                    (90,   'XC'),
                    (50,   'L'),
                    (40,   'XL'),
                    (10,   'X'),
                    (9,    'IX'),
                    (5,    'V'),
                    (4,    'IV'),
                    (1,    'I')]
    i = 0
    ret = 0
    for digit, symbol in symbol_digit:
        count = 0
        while i + len(symbol) - 1 < len(s) and s[i:i+len(symbol)] == symbol:
            count += 1
            i += len(symbol)
        ret += count * digit
    return ret
    
    #2) using dictionary and not saving
    _symbol2digit = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
    ret = 0
    # 2a)
    for i, c in enumerate(s):
        #if i + 1 < len(s) and _symbol2digit[s[i]] < _symbol2digit[s[i+1]]:
        # the code above could be replaced with a slicing trick
        # s[i+1:i+2] would return '' if i is out of range
        curr, nxt = s[i], s[i+1:i+2]
        if nxt and _symbol2digit[curr] < _symbol2digit[nxt]:
            ret -= _symbol2digit[curr]
        else:
            ret += _symbol2digit[curr]
    # 2b)
    i = 0
    while i < len(s):
        curr, nxt = s[i], s[i+1:i+2]
        if nxt and _symbol2digit[curr] < _symbol2digit[nxt]:
            ret += _symbol2digit[nxt] - _symbol2digit[curr]
            i += 2
        else:
            ret += _symbol2digit[curr]
            i += 1
    # 2c)
    s = s[::-1]
    res = dt[s[0]]
    for i in range(1, len(s)):
        if dt[s[i]] >= dt[s[i-1]]:
            res += dt[s[i]]
        else:
            res -= dt[s[i]]
            
        
    
    return ret
    

