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
    <div style="background-color:tomato;padding:8px">
    <h2 style="color:white;text-align:center;">Youtube Video to Audio Converter </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
  
    url = st.text_input("Enter Youtube URL","Type Here")
    
    file_title=''

    if st.button("Convert"):
            buffer = BytesIO()
            st.text("P1")
            youtube_video = YouTube(url)
            st.text("P2")
            audio = youtube_video.streams.get_audio_only()
            st.text("P3")
            default_filename = audio.default_filename
            audio.stream_to_buffer(buffer)
            st.text("P4")
            default_filename, buffer = download_audio_to_buffer(url)
            st.text("P1")
        
            st.success('The file {} is converted to mp3'.format(default_filename))
        
            title_vid = Path(default_filename).with_suffix(".mp3").name
        
            st.audio(buffer, format='audio/mp3')
            
            st.download_button(label="Download mp3",data=buffer,file_name=title_vid,mime="audio/mp3")

    if st.button("About"):
        st.text("Demo to convert youtube Video to mp3")
        st.text("Built with Streamlit")

    with st.sidebar:
        html_sidebar = """
            <div style="background-color:white;padding:4px">
            <h2 style="color:black;text-align:center;">STEP1</h2>
            <h2 style="color:Green;text-align:center;">Enter Youtube URL</h2>
            <h2 style="color:black;text-align:center;">STEP2</h2>
            <h2 style="color:Green;text-align:center;">Click on Convert Button</h2>
            <h2 style="color:black;text-align:center;">STEP3</h2>
            <h2 style="color:Green;text-align:center;">Play audio or click Download to save the file</h2>
            </div>
            """
        st.markdown(html_sidebar,unsafe_allow_html=True)

if __name__=='__main__':
    main()
