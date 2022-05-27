
def find_anagrams(str1, str2):
    # [assignment] Add your code here
    if (sorted(str1) == sorted(str2)):
        print("True")
    else:
        print("False")

str1 = input("type in a word: ")
str2 = input("type in a word: ")
find_anagrams(str1, str2)
