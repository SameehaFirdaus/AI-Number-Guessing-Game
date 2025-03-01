import random  

def ai_guess(low, high, attempts=0):  
    if low > high:  
        print("Something went wrong! Are you changing the number?")  
        return  

    guess = (low + high) // 2  
    print(f"AI's guess: {guess}")  
    feedback = input("If correct, enter 'c', if your number is higher enter 'h', if lower enter 'l': ").lower()  

    if feedback == 'c':  
        print(f"AI guessed it in {attempts+1} attempts! 🎉")  
        return  
    elif feedback == 'h':  
        ai_guess(guess + 1, high, attempts + 1)  
    elif feedback == 'l':  
        ai_guess(low, guess - 1, attempts + 1)  
    else:  
        print("Invalid input, please use 'c', 'h', or 'l'.")  
        ai_guess(low, high, attempts)  

print("Think of a number (1-100), and AI will try to guess it!")  
input("Press ENTER when you're ready...")  
ai_guess(1, 100)