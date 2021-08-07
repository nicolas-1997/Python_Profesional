# This code is for practicing static typing

def is_palindrome(string: str):
    string = string.replace(" ", "").lower() #we clean the word and save it in a variable
    
    #we compare the word with same but other way around
    if string == string[::-1]:  #[::-1 serves to turn]
        print("This is palindrome!!", string,"=", string[::-1]) 
    else:
        print("Not is a palindrome!!", string,"=", string[::-1])


def run():
    palindrome = input("Enter a word: ") #we ask the user for a word

    is_palindrome(palindrome) #we pass this word as a parameter for the function

if __name__=="__main__":
    run()


