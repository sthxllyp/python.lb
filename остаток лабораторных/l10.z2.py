sequence = 'asdf1233515SDf3asdfasd55121390xzuwy'
unique_set = set(sequence)
letters_set = sorted({x for x in unique_set if (x.isalpha() and ((x.upper() >= 'A' and x.upper() <= 'F') or (x.upper() >= 'X' and x.upper() <= 'Z')) )})
print(letters_set)