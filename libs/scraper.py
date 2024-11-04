from libs.chrome_dev import ChromDevWrapper


class Scraper(ChromDevWrapper):
    
    def __init__(self):
        
        # Start scraper
        super().__init__(start_killing=True)
        self.youtube_page = 'https://studio.youtube.com/'
        self.canva_page = 'https://www.canva.com/projects/'
    
    def download_canva_video(self, video_name: str) -> str:
        """ Download video from canva
        
        Args:
            video_name (str): name of video to download

        Returns:
            str: path of downloaded video
        """
        
        self.set_page(self.canva_page)
        input("continue?")
    
    def upload_youtube_video(self, video_path: str):
        """ Upload video to youtube

        Args:
            video_path (str): path of video to upload
        """
        self.set_page(self.youtube_page)
        input("continue?")