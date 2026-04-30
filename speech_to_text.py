import speech_recognition as sr

def speech_to_text():
    # 1. Initialize the recognizer
    # The recognizer is responsible for processing the audio and converting it to text
    recognizer = sr.Recognizer()

    # 2. Use the default microphone as the audio source
    # You will need the 'PyAudio' library installed to use the microphone
    try:
        with sr.Microphone() as source:
            print("Adjusting for ambient noise... Please wait.")
            # Briefly listen to the background noise to calibrate the recognizer
            recognizer.adjust_for_ambient_noise(source, duration=1)
            
            print("Listening... Speak now!")
            # 3. Capture the audio from the user
            # timeout: How long to wait for speech to start (in seconds)
            # phrase_time_limit: Maximum duration of a single phrase (in seconds)
            audio_data = recognizer.listen(source, timeout=5, phrase_time_limit=15)
            
            print("Processing audio, please wait...")

            # 4. Convert the captured audio to text using Google's free Web Speech API
            text = recognizer.recognize_google(audio_data)
            
            # Print the successfully recognized text
            print("\n--- Recognized Text ---")
            print(text)
            print("-----------------------")

    # Handle the error if the user doesn't speak within the timeout period
    except sr.WaitTimeoutError:
        print("Error: No speech detected. You took too long to start speaking.")
    
    # Handle the error if the audio is unclear and cannot be understood
    except sr.UnknownValueError:
        print("Error: Could not understand the audio. Please try speaking more clearly.")
    
    # Handle the error if the computer cannot connect to the recognition service (e.g., no internet)
    except sr.RequestError as e:
        print(f"Error: Could not connect to the speech recognition service. ({e})")
        
    # Catch any issues finding the microphone
    except AttributeError:
        print("Error: Could not find a microphone. Please ensure PyAudio is installed (pip install pyaudio) and a mic is connected.")
        
    # Catch any other unexpected errors
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    # Run the function when the script is executed
    speech_to_text()
