"""
Created on 24-Sep-2024
@author: Pradeep Dekhane
"""

# import required modules
import os
from io import BytesIO
from pathlib import Path

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
def download_audio_to_buffer(url):
    buffer = BytesIO()
    youtube_video = YouTube(url)
    audio = youtube_video.streams.get_audio_only()
    default_filename = audio.default_filename
    audio.stream_to_buffer(buffer)
    return default_filename, buffer


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
            default_filename, buffer = download_audio_to_buffer(url)
            st.success('The file {} is converted to mp3'.format(default_filename))
            title_vid = Path(default_filename).with_suffix(".mp3").name
            st.audio(buffer, format="audio/mp3", loop=True)
            
            st.download_button(
            label="Download mp3",
            data=buffer,
            file_name=title_vid,
            mime="audio/mpeg")
            
        except:
            st.warning('Enter the correct URL')
    
    if st.button("About"):
        st.text("Demo to convert youtube Video to mp3")
        st.text("Built with Streamlit")

if __name__=='__main__':
    main()
