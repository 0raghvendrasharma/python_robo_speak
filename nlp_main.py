import pyttsx3
import speech_recognition as sr
import nltk

# Download the NLTK punkt package for tokenization
nltk.download('punkt')

def get_user_input():
    # Use the speech recognition library to get user input
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        user_input = recognizer.recognize_google(audio)
        print("You said:", user_input)
        return user_input
    except sr.UnknownValueError:
        print("Sorry, I didn't catch that. Can you please repeat?")
        return get_user_input()
    except sr.RequestError as e:
        print(f"Error connecting to Google API: {e}")
        return None

def main():
    print("Hi! I am Karishma, your virtual assistant")

    # Initialize the text-to-speech engine
    engine = pyttsx3.init()

    # Set the rate property (words per minute)
    rate = engine.getProperty('rate')
    engine.setProperty('rate', rate - 50)  # Decrease the rate by 50

    # Get user input
    user_input = get_user_input()

    if user_input:
        # Use the engine to speak the input text
        engine.say(user_input)

        # Wait for the speech to finish
        engine.runAndWait()

if __name__ == '__main__':
    main()
