from gtts import gTTS
import streamlit as st
import pyttsx3
import time
import os
import pygame
# from pydub import AudioSegment
# from pydub.playback import play
# import playsound
# import simpleaudio as sa

# Initialize text-to-speech engine
# engine = pyttsx3.init()

# Function to speak the time
# def speak_time_gtts():
#     while True:
#         current_time = time.strftime("%I:%M %p")  # Format as "03:15 PM"
#         text = f"The current time is {current_time}"
#         tts = gTTS(text=text, lang='en')
#         tts.save("time.mp3")
#         playsound("time.mp3")
#         time.sleep(1 * 60)  # Wait for 5 minutes

# # Background thread to run the speak_time function
# def start_time_announcement():
#     thread = threading.Thread(target=speak_time_gtts, daemon=True)
#     thread.start()

# Streamlit UI
st.title("Time Announcer")
st.write("This app will speak the current time every 5 minutes.")

if st.button("Start Time Announcements"):
    st.write("Time announcements started!")
    # start_time_announcement()
    current_time = time.strftime("%I:%M %p")  # Format as "03:15 PM"
    text = f"The current time is {current_time}"
    st.write(f"text is {text}")
    # st.write(f"playsound is:{playsound}")
    tts = gTTS(text=text, lang='en')
    tts.save("time.mp3")
    
    # Initialize mixer
    pygame.mixer.init()
    print("pygame.mixer initialized successfully")
    # Load and play sound
    pygame.mixer.music.load("time.mp3")
    pygame.mixer.music.play()

    # Wait until the music finishes
    while pygame.mixer.music.get_busy():
        pass
        
    # # Load audio file
    # audio = AudioSegment.from_file("time.mp3")

    # # Play audio
    # play(audio)
    
    # playsound("time.mp3")
    # # Load the WAV file
    # wave_obj = sa.WaveObject.from_wave_file("time.mp3")
    
    # # Play the audio
    # play_obj = wave_obj.play()
    
    # Wait for playback to finish before exiting
    # play_obj.wait_done()
