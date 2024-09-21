"""
Created on 24-Sep-2024
@author: Pradeep Dekhane
"""

# import required modules
import os

import whisper
from pytubefix import YouTube
from pytubefix.cli import on_progress

import streamlit as st
import pandas as pd
import numpy as np

# center button in sidebar
st.markdown(
    """
    <style>
        [data-testid=stSidebar] [data-testid=stButton]{
            text-align: center;
            display: block;
            margin-left: auto;
            margin-right: auto;
            width: 100%;
        }
    </style>
    """, unsafe_allow_html=True
)

# Function to open a file
def startfile(fn):
    os.system('open %s' % fn)


# Function to create and open a txt file
def create_and_open_txt(text, filename):
    # Create and write the text to a txt file
    with open(filename, "w") as file:
        file.write(text)
    startfile(filename)

# Function to convert to audio
def to_audio(url):
    # Create a YouTube object from the URL
    yt = YouTube(url, on_progress_callback = on_progress)
    audio_stream = yt.streams.get_audio_only()
    
    # Download the audio stream
    #output_path = "Youtube_Audios"
    filename = yt.title + ".mp3"
    audio_stream.download(filename=filename)
    return filename


def main():
    st.title("YouTube Audio Downloader")
    
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Youtube Video to Audio Converter </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
  
    url = st.text_input("Enter Youtube URL","Type Here")
    
    file_title=''

    if st.button("Convert"):
        try:
            st.warning('Checkpint #1')
            file_title=to_audio(url)
            st.warning('Checkpint #2')
            st.success('The file {} is converted to mp3'.format(file_title))
            st.warning('Checkpint #3')
            st.audio(f"{file_title}", format="audio/mp3", loop=True)
            st.warning('Checkpint #4')
            
            with open(f"{file_title}", "rb") as f:

                st.download_button('Download Audio', f, file_name=f"{file_title}")
            
        except:
            st.warning('Enter the correct URL')
    
    if st.button("About"):
        st.text("Demo to convert youtube Video to mp3")
        st.text("Built with Streamlit")

if __name__=='__main__':
    main()
