import os
from dotenv import load_dotenv
from libs.scraper import Scraper


load_dotenv()
VAR = os.getenv("VAR")


def main():
    scraper = Scraper()
    canva_video_path = scraper.download_canva_video("sample video 1")
    scraper.upload_youtube_video(canva_video_path)


if __name__ == "__main__":
    main()
