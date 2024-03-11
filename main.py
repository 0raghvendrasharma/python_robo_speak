import pyttsx3

if __name__ == '__main__':
    print("Hi! I am Karishma, your virtual assistant")
    x = input("Enter how may I help you: ")
    
    # Initialize the text-to-speech engine
    engine = pyttsx3.init()

    # Set the rate property (words per minute)
    rate = engine.getProperty('rate')   # Get the current rate
    engine.setProperty('rate', rate - 50)  # Decrease the rate by 50 (you can adjust this value)

    # Use the engine to speak the input text
    engine.say(x)

    # Wait for the speech to finish
    engine.runAndWait()