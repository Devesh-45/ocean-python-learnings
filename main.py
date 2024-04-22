print("Finding the length and printing the word ")
Word=str(input("Enter a word:"))
Length=len(Word)
if Length%2==0:
    print(Word.upper())
elif Length%3==0:
    Slice=Word[::-1]
    print(Slice)
else:
    print(Word.lower())
