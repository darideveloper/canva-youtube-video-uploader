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

        self.set_page(video_name)

        mp4_files = [f for f in os.listdir(dowload_path) if f.endswith('.mp4')]

        self.click("._38oWvQ")

        original_mp4_files = len(mp4_files)
        original_files = mp4_files

        print("Waiting for download to finish...")
        while len(mp4_files) <= original_mp4_files:
            mp4_files = [f for f in os.listdir(dowload_path) if f.endswith('.mp4')]
        print("Download finished")

        new_file = list(set(original_files) ^ set(mp4_files))[0]
        new_file_path = dowload_path + "\\" + new_file
        print(f"New video: {new_file_path}")

        return new_file_path

    def upload_youtube_video(self, video_path: str):
        """ Upload video to youtube

        Args:
            video_path (str): path of video to upload
        """

        selectors = {
            "upload_btn": "#upload-button",
            "input_video": "input[type='file']"
        }

        # Open upload page
        self.set_page(self.youtube_page)
        self.click(selectors["upload_btn"])
        
        # Upload video file
        sleep(2)
        # elems = self.count_elems(selectors["input_video"])
        # video_value = self.get_attrib(selectors["input_video"], "value")
        # video_value_2 = self.get_prop(selectors["input_video"], "value")
        # self.send_data(selectors["input_video"], video_path)
        # elems = self.count_elems(selectors["input_video"])
        # video_value = self.get_attrib(selectors["input_video"], "value")
        # video_value_2 = self.get_prop(selectors["input_video"], "value")
        # self.send_data_js(selectors["input_video"], video_path)
        # elems = self.count_elems(selectors["input_video"])
        # video_value = self.get_attrib(selectors["input_video"], "value")
        # video_value_2 = self.get_prop(selectors["input_video"], "value")
        self.set_attrib(selectors["input_video"], "value", video_path)
        elems = self.count_elems(selectors["input_video"])
        video_value = self.get_attrib(selectors["input_video"], "value")
        video_value_2 = self.get_prop(selectors["input_video"], "value")
        input("continue?")
        
