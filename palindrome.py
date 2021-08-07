def is_palindrome(string: str):
    string = string.replace(" ", "").lower()
    
    if string == string[::-1]:
        print("This is palindrome!!", string,"=", string[::-1])
    else:
        print("Not is a palindrome!!", string,"=", string[::-1])


def run():
    palindrome = input("Enter a word: ")

    is_palindrome(palindrome)

if __name__=="__main__":
    run()