from fastapi import APIRouter
from utils.response import response
from utils.dbconnect import mydb
from pytube import YouTube
import os
import urllib.parse

router = APIRouter()

mycol = mydb["streamspot"]

@router.get("/download_movies")
def download_movies_api(youtube_url):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
            'Referer': 'https://www.youtube.com/'
        }   
        # youtube_url = urllib.parse.unquote(youtube_url)
        # Initialize YouTube object
        yt = YouTube(youtube_url,headers)
        
        # Select the 1080p stream (or any other stream you need)
        ytdownload = yt.streams.filter(res='1080p',file_extension="mp4").first()
        
        if ytdownload is None:
            return response(1015)
        
        # Define the download directory (you can modify this path as per your requirement)
        download_path = "downloads"
        if not os.path.exists(download_path):
            os.makedirs(download_path)

        # Download the video to the specified path
        video_file = ytdownload.download(output_path=download_path)
        
        # Return the download path
        return os.path.join(download_path, os.path.basename(video_file))

    except Exception as e:
        # return {"error":str(e)}
        return response(1016)
        