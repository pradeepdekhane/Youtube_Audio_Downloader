"""
Created on 24-Sep-2024
@author: Pradeep Dekhane
"""

# import required modules
import os

import whisper
#from pytubefix import YouTube
from pytubefix.cli import on_progress

from io import BytesIO
from pathlib import Path

from pytube import YouTube

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

#st.set_page_config(page_title="Download Audio", page_icon="🎵", layout="centered", initial_sidebar_state="collapsed")

#@st.cache_data(show_spinner=False)
def download_audio_to_buffer(url):
    buffer = BytesIO()
    youtube_video = YouTube(url)
    st.warning('Checkpint in download_audio_to_buffer #1')
    audio = youtube_video.streams.get_audio_only()
    st.warning('Checkpint in download_audio_to_buffer #2')
    default_filename = audio.default_filename
    audio.stream_to_buffer(buffer)
    st.warning('Checkpint in download_audio_to_buffer #3')
    return default_filename, buffer

# Function to convert to audio
def to_audio(url):
    # Create a YouTube object from the URL
    yt = YouTube(url, on_progress_callback = on_progress)
    st.warning('Checkpint in to_audio #1')
    audio_stream = yt.streams.get_audio_only()
    st.warning('Checkpint in to_audio #2')
    
    # Download the audio stream
    #output_path = "Youtube_Audios"
    filename = yt.title + ".mp3"
    audio_stream.download(filename=filename)
    st.warning('Checkpint in to_audio #3')
    return filename


def main():
    st.title("Download Audio from Youtube")
    url = st.text_input("Insert Youtube URL:")
    if url:
        with st.spinner("Downloading Audio Stream from Youtube..."):
            default_filename, buffer = download_audio_to_buffer(url)
        st.subheader("Title")
        st.write(default_filename)
        title_vid = Path(default_filename).with_suffix(".mp3").name
        st.subheader("Listen to Audio")
        st.audio(buffer, format='audio/mpeg')
        st.subheader("Download Audio File")
        st.download_button(
            label="Download mp3",
            data=buffer,
            file_name=title_vid,
            mime="audio/mpeg")
        
if __name__=='__main__':
    main()
