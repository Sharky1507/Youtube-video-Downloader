import streamlit as st
from pytube import YouTube
import os

st.title("YouTube Video Downloader")
st.subheader("Enter the URL:")
url = st.text_input(label='URL')

if url:
    yt = YouTube(url)
    st.image(yt.thumbnail_url, width=300)
    st.subheader('''
    {}
    ## Length: {} seconds
    ## Rating: {} 
    '''.format(yt.title , yt.length , yt.rating))

    video_streams = yt.streams
    if video_streams:
        download_choice = st.radio(
            "Choose format to download",
            ('Video', 'Audio')
        )

        #download_button = st.button("Download")

        #if download_button:
        if download_choice == 'Video':
                video_file = video_streams.get_lowest_resolution().download()
                with open(video_file, 'rb') as file:
                    st.download_button(
                        label="File is ready! Click here to download the video",
                        data=file,
                        file_name=os.path.basename(video_file),
                        mime='video/mp4'
                    )
        elif download_choice == 'Audio':
                audio_file = video_streams.filter(only_audio=True).first().download()
                with open(audio_file, 'rb') as file:
                    st.download_button(
                        label="File is ready! Click here to download the audio",
                        data=file,
                        file_name=os.path.basename(audio_file),
                        mime='audio/mp3'
                    )
    else:
        st.subheader("Sorry, this video cannot be downloaded.")
