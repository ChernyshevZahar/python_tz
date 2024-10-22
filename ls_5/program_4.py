def substrings(s):

    length = len(s)
    
    for start in range(length):
    
        for end in range(start + 1, length + 1):
            yield s[start:end]
            
for substring in substrings('abc'):
    print(substring)