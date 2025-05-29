import streamlit as st
import speech_recognition as sr
import os

# Initialize recognizer
recognizer = sr.Recognizer()

# Streamlit UI
st.title("Speech to Text ")
st.write("Upload a WAV audio file to transcribe it to text.")

# File uploader for WAV files
uploaded_file = st.file_uploader("Choose a WAV file", type=["wav"])

if uploaded_file is not None:
    # Save uploaded file temporarily
    with open("temp_audio.wav", "wb") as f:
        f.write(uploaded_file.read())
    
    # Process the audio file
    with sr.AudioFile("temp_audio.wav") as source:
        st.write("Processing audio file...")
        try:
            audio = recognizer.record(source)
            text = recognizer.recognize_google(audio)
            st.success(f"Transcribed text: {text}")
        except sr.UnknownValueError:
            st.error("Could not understand the audio.")
        except sr.RequestError as e:
            st.error(f"Error with speech recognition service: {e}")
        except Exception as e:
            st.error(f"An unexpected error occurred: {e}")
