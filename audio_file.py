import pyttsx3
from pydub import AudioSegment

def speak(text, gender="male", file_name="output.mp3"):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')


    if gender == "male":
        engine.setProperty('voice', voices[0].id)  
    elif gender == "female":
        engine.setProperty('voice', voices[1].id)  

    engine.setProperty('rate', 150)  

    engine.save_to_file(text, file_name)
    engine.runAndWait()

    print(f"Saved {gender} voice at: {file_name}")
    
speak("Helo, I am from Mumbai.", gender="male", file_name="data_file/personal/maudio5.mp3")
speak("Hello, I am from Delhi.", gender="female", file_name="data_file/personal/faudio5.wav")

