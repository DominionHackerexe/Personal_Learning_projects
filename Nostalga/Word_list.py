import random
import pyttsx3

def words_spelling():
    words = ["cake", "apple", "banana", "orange", "grape", "watermelon", "strawberry", "blueberry", "pineapple", "mango", "dog", "cat", "flamingo", 
             "parrot", "turtle", "rabbit", "hamster", "fish", "lizard", "snake", "horse", "cow", "pig", "sheep", "chicken", 
             "duck", "goat", "deer", "elephant", "lion", "tiger", "bear", "money", "funny"]
    
    engine = pyttsx3.init()
    engine.setProperty('rate', 125)  # Speed of speech
    engine.setProperty('volume', 1)  # Volume level (0.0 to 1.0)
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)

    engine.say("Welcome to the spelling game! Let's learn!")
    random.shuffle(words)
    engine.say("I will say a word, and you will spell it.")
    engine.runAndWait()

    for word in words:
        engine.say(f"{word}, please spell it.")
        engine.runAndWait()
        user_spelling = input()

        if user_spelling.lower() == word:
            engine.say("Correct!")
            engine.runAndWait()
        else:
            engine.say(f"Incorrect. The correct spelling is {word}.")
            engine.say("Lets move to the next word.")
            engine.runAndWait()
        
    engine.say("Great job! You have completed the spelling game.")
    engine.say("To play again, please input 1, or to exit, input 0.")
    engine.runAndWait()

    play_again = input()
    if play_again == '1':
        words_spelling()
    else:
        engine.say("Thank you for playing! Goodbye!")
        engine.runAndWait()



words_spelling() #Runs the function to start the game