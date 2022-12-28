def BB26_to_int(s: str) -> int:

    result = 0
   
    for c in s.lower():
        result *= 26
        result += 1 + ord(c) - ord('a')
    
    return result
    
    
def int_to_BB26(n: int) -> str:

    result = ""

    while n > 0:
        n, remainder = divmod(n, 26)
        
        if remainder == 0:
            remainder = 26
            n -= 1
        
        result = chr(ord('a') + (remainder - 1)) + result
    return result
