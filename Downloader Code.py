import os
from pytube import YouTube

def download(url,save_path="D:\Downloaded Videos"):
    try:
        yt= YouTube(url)
        video_stream=yt.streams.get_highest_resolution()
        
        video_stream.download(output_path=save_path)
        print(f"Video Downloaded Successfully to{save_path}")
    except Exception as e:
        print(f"Error:{e}")
        
def main():
    url=input("Enter the video url to be downloaded: ")
    save_directory="Downloaded Videos"
    
    if not os.path.exists(save_directory):
        os.makedirs(save_directory)
    
    download(url,save_path=save_directory)
    
if __name__ =="__main__":
    main()
        