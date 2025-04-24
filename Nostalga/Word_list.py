# filename: Word_list_edgetts.py
import random
import edge_tts
import asyncio
import os
import tempfile
from playsound import playsound # Import playsound

# --- Configuration ---
VOICE = "en-US-JennyNeural" # Example voice, find others with `edge-tts --list-voices`
RATE = "-25%"  # Slow down speech slightly (approximates pyttsx3 rate=125)
VOLUME = "+0%" # Default volume
OUTPUT_FILE = os.path.join(tempfile.gettempdir(), "temp_speech.mp3") # Use temp directory
# --- End Configuration ---

async def speak(text: str) -> None:
    """Uses edge-tts to speak the given text."""
    try:
        communicate = edge_tts.Communicate(text, VOICE, rate=RATE, volume=VOLUME)
        await communicate.save(OUTPUT_FILE)

        # Use playsound to play the generated file
        playsound(OUTPUT_FILE)

    except Exception as e:
        print(f"Error during text-to-speech: {e}")
    finally:
        # Clean up the temporary file
        if os.path.exists(OUTPUT_FILE):
            try:
                os.remove(OUTPUT_FILE)
            except PermissionError:
                # Handle cases where the file might still be in use briefly
                # In a more robust application, you might retry or log this
                print(f"Warning: Could not delete temporary file {OUTPUT_FILE} immediately.")
            except Exception as e_del:
                 print(f"Error deleting temporary file {OUTPUT_FILE}: {e_del}")


async def words_spelling():
    """Runs the spelling game logic."""
    words = ["cake", "apple", "banana", "orange", "grape", "watermelon", "strawberry", "blueberry", "pineapple", "mango", "dog", "cat", "flamingo",
             "parrot", "turtle", "rabbit", "hamster", "fish", "lizard", "snake", "horse", "cow", "pig", "sheep", "chicken",
             "duck", "goat", "deer", "elephant", "lion", "tiger", "bear", "money", "funny"] #

    await speak("Welcome to the spelling game! Let's learn!") #
    random.shuffle(words) #
    await speak("I will say a word, and you will spell it.") #


    for word in words: #
        print("-" * 10) # Separator for clarity
        await speak(f"{word}, please spell it.") #
        user_spelling = input(f"Spell the word: ") # Prompt user clearly

        if user_spelling.lower() == word: #
            await speak("Correct!") #
            print("Correct!")
        else:
            await speak(f"Incorrect. The correct spelling is {word}.") #
            print(f"Incorrect. The correct spelling is: {word}")
            await speak("Let's move to the next word.") #

    await speak("Great job! You have completed the spelling game.") #


async def main():
    """Main async function to run the game loop."""
    while True:
        await words_spelling()
        await speak("To play again, please input 1, or to exit, input 0.") #
        play_again = input("Play again? (1 for yes, 0 for no): ") #
        if play_again != '1': #
            await speak("Thank you for playing! Goodbye!") #
            print("Goodbye!")
            break

if __name__ == "__main__":
    # Ensure the script is run in an environment where asyncio can run
    # (like a standard Python interpreter).
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\nExiting game.")
    finally:
         # Final cleanup attempt for the temp file if it still exists
        if os.path.exists(OUTPUT_FILE):
            try:
                os.remove(OUTPUT_FILE)
            except Exception:
                 pass # Ignore errors during final cleanup





































































































# import random
# import pyttsx3

# play_again = '1'
# def words_spelling():
#     words = ["cake", "apple", "banana", "orange", "grape", "watermelon", "strawberry", "blueberry", "pineapple", "mango", "dog", "cat", "flamingo", 
#              "parrot", "turtle", "rabbit", "hamster", "fish", "lizard", "snake", "horse", "cow", "pig", "sheep", "chicken", 
#              "duck", "goat", "deer", "elephant", "lion", "tiger", "bear", "money", "funny"]
    

    
#     engine = pyttsx3.init()
#     engine.setProperty('rate', 125)  # Speed of speech
#     engine.setProperty('volume', 1)  # Volume level (0.0 to 1.0)
#     voices = engine.getProperty('voices')
#     engine.setProperty('voice', voices[1].id)

#     engine.say("Welcome to the spelling game! Let's learn!")
#     random.shuffle(words)
#     engine.say("I will say a word, and you will spell it.")
#     engine.runAndWait()
#     engine.endLoop()


#     for word in words:
#         engine.say(f"{word}, please spell it.")
#         engine.runAndWait()
#         engine.endLoop()
#         user_spelling = input()

#         if user_spelling.lower() == word:
#             engine.say("Correct!")
#             engine.runAndWait()
#             engine.endLoop()
#         else:
#             engine.say(f"Incorrect. The correct spelling is {word}.")
#             engine.say("Lets move to the next word.")
#             engine.runAndWait()
#             engine.endLoop()
        
#     engine.say("Great job! You have completed the spelling game.")
#     engine.say("To play again, please input 1, or to exit, input 0.")
#     engine.runAndWait()
#     engine.endLoop()

#     play_again = input()
#     if play_again == '1':
#         words_spelling()
#     else:
#         engine.say("Thank you for playing! Goodbye!")
#         engine.runAndWait()
#         engine.endLoop()
#         engine.stop()


# if play_again == '1':
#     words_spelling()