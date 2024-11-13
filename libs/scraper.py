import os
from libs.chrome_dev import ChromDevWrapper


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

        print("\t\tWaiting for download to finish...")
        while len(mp4_files) <= original_mp4_files:
            mp4_files = [f for f in os.listdir(dowload_path) if f.endswith('.mp4')]
        print("\t\tDownload finished")

        new_file = list(set(original_files) ^ set(mp4_files))[0]
        new_file_path = dowload_path + "\\" + new_file
        print(f"\t\tNew video: {new_file_path}")

        return new_file_path

    def upload_youtube_video(self, video_path: str):
        """ Upload video to youtube

        Args:
            video_path (str): path of video to upload
        """

        selectors = {
            "upload_btn": "#upload-button",
            "input_video": "input[type='file']",
            "preview_play_btn": '[icon="av:play-arrow"]',
            "video_title": "#textbox",
        }

        # Open upload page
        self.set_page(self.youtube_page)
        self.click(selectors["upload_btn"])
        
        # Upload video
        print("\t\tUploading file...")
        self.wait_load(selectors["input_video"])
        self.send_input_file(selectors["input_video"], video_path)
        
        # Wait until video is processed (until preview play button is available)
        print("\t\tWaiting youtube to process video...")
        self.wait_load(selectors["preview_play_btn"], max_wait=300)
        
        # Write video data
        print("\t\tWriting video data...")
        self.set_innerhtml(selectors["video_title"], "Sample Video 1")
        
        input("Press enter to continue...")
        