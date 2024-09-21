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
def to_audio_mod(url):
    buffer = BytesIO()
    youtube_video = YouTube(url)
    audio = youtube_video.streams.get_audio_only()
    default_filename = audio.default_filename
    audio.stream_to_buffer(buffer)
    return default_filename, buffer

# Function to convert to audio
def download_audio_to_buffer(url):
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
            with st.spinner("Downloading Audio Stream from Youtube..."):
                default_filename, buffer = download_audio_to_buffer(url)
                st.subheader("Title")
                st.write(default_filename)
            st.success('The file {} is converted to mp3'.format(file_title))

            st.audio(f"{buffer}", format="audio/mp3", loop=True)
            
            with open(f"{buffer}", "rb") as f:

                st.download_button('Download Audio', f, file_name=f"{buffer}")
            
        except:
            st.warning('Enter the correct URL')
    
    if st.button("About"):
        st.text("Demo to convert youtube Video to mp3")
        st.text("Built with Streamlit")

if __name__=='__main__':
    main()
