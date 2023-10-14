# By Samuel Fisher (Sammy03g)
# COP2002.0T2
# Date Created (09/20/2023)
# This code uses functions, loops, and string concatenation to cipher a text provided by the user.

# Main function where the algorithm is stored.
def main():

# Parallel arrays used to encrypt.
    arrayOriginal=["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    arrayEncrypt=["B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "A", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s",  "t", "u", "v", "w", "x", "y", "z", "a"]
    
# User Input
    userInput=str(input("Enter the text to encrypt:  "))

# Empty variable to store the encrypted text.
    stringEncrypted=""

# Encryption.
    for i in userInput:  # For loop to search through every letter in the user input string.

        index=0  # Counter variable to ensure the while loop has an end point.
        found=False  # Variable that will be used to concatenate any punctuation left over, considering the array does not contain any punctuation.

        while(index<len(arrayOriginal)and not found):  # While loop that ensures the x variable is still in the domain of the array, since x is added by 1 every iteration.

            if(arrayOriginal[index]==i):  # Boolean function used to ensure the index of the arrayOriginal is equal to a letter in User Input.
                stringEncrypted+=arrayEncrypt[index]  # If the index of the original array is equal to a letter in User Input then, it will concatenate the same index from arrayEncrypt to the empty string.
                found=True  
            index+=1
            
        if(not found):  # Boolean function to ensure the punctuation will be concatenated to the string.
            stringEncrypted+=i
   
    print(stringEncrypted)

# Calling main
if (__name__=="__main__"):
    main()

