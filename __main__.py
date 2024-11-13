import os
from dotenv import load_dotenv
from libs.scraper import Scraper
from libs.xlsx import SpreadsheetManager

load_dotenv()
EXCEL_FILE = os.getenv("EXCEL_ROUTE")
EXCEL_SHEET = os.getenv("EXCEL_SHEET")
DOWNLOAD_FOLDER = os.getenv("DOWNLOAD_FOLDER")

def main():
    excel_reader = SpreadsheetManager(EXCEL_FILE)
    excel_reader.set_sheet(EXCEL_SHEET)
    data = excel_reader.get_data()
    #print(data)
    for row in range(1,len(data)):   
        scraper = Scraper()
        canva_video_path = scraper.download_canva_video(data[row][0], DOWNLOAD_FOLDER)
        scraper.upload_youtube_video(canva_video_path)
    

if __name__ == "__main__":
    main()
