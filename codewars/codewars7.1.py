#mesame codewars 7kiu
#Anagram Detection




def is_anagram(test, original):
    test = test.lower()
    original = original.lower()
    
    return sorted(test) == sorted(original)