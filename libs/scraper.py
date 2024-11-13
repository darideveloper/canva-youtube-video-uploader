from libs.chrome_dev import ChromDevWrapper
import os
from time import sleep

class Scraper(ChromDevWrapper):
    
    def __init__(self):
        
        # Start scraper
        super().__init__(start_killing=True)
        self.youtube_page = 'https://studio.youtube.com/'
        self.canva_page = 'https://www.canva.com/projects/'
    
    def download_canva_video(self, video_name: str, dowload_path) -> str:
        """ Download video from canva
        
        Args:
            video_name (str): name of video to download
            download_path (str): path where the path will be downloaded

        Returns:
            str: path of downloaded video
        """
        
        print(video_name)
        self.set_page(video_name)

        mp4_files = [f for f in os.listdir(dowload_path) if f.endswith('.mp4')]

        print(mp4_files)

        self.click("._38oWvQ")

        original_mp4_files = len(mp4_files)
        original_files = mp4_files

        #print(original_mp4_files)
        while len(mp4_files) <= original_mp4_files:
            mp4_files = [f for f in os.listdir(dowload_path) if f.endswith('.mp4')]    
            #print(len(mp4_files))
        
        new_file = list(set(original_files) ^ set(mp4_files))[0]
        new_file_path = dowload_path+"\\"+new_file
        print(new_file_path)

        return new_file_path
    
    def upload_youtube_video(self, video_path: str):
        """ Upload video to youtube

        Args:
            video_path (str): path of video to upload
        """
        self.set_page(self.youtube_page)
        self.click('.yt-spec-touch-feedback-shape.yt-spec-touch-feedback-shape--touch-response-inverse')
        #self.click('#select-files-button .yt-spec-touch-feedback-shape__stroke')
        sleep(5)
        self.send_data("input[type='file']", video_path)
        input("continue?")