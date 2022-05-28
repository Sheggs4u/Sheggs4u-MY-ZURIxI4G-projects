 # Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagram(string1, string2):
        return sorted(string1) == sorted(string2)

print (find_anagram("peach", "cheap"))

print (find_anagram("class", "slack"))



#####A SECOND METHOD THAT ACCEPTS INPUT#######

def find_anagram(word, anagram):

    if(sorted(word)== sorted(anagram)):
        answer=True
    else:
        answer=False
    return answer
word = input("Enter first word: ")
anagram = input("Enter Second word: ")
answer = find_anagram(word,anagram)

print(answer)
