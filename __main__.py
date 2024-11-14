import os
from dotenv import load_dotenv
from libs.scraper import Scraper
from libs.xlsx import SpreadsheetManager

load_dotenv()
EXCEL_FILE = os.getenv("EXCEL_ROUTE")
EXCEL_SHEET = os.getenv("EXCEL_SHEET")
DOWNLOAD_FOLDER = os.getenv("DOWNLOAD_FOLDER")

# Open excel file
print("Reading excel file...")
excel_reader = SpreadsheetManager(EXCEL_FILE)
excel_reader.set_sheet(EXCEL_SHEET)

# start scraper
print("Opening browser...")
scraper = Scraper()


def download_videos():
    """ Download canva videos from excel file and upload them to youtube """

    data = excel_reader.get_data()

    for row in range(1, len(data)):

        canva_link = data[row][0]
        print(f"Video: {canva_link}")

        # Download video from canva
        print("\tDownloading video...")
        canva_video_path = scraper.download_canva_video(
            canva_link,
            DOWNLOAD_FOLDER
        )

        # Upload video to youtube
        print("\tUploading video to youtube...")
        scraper.upload_youtube_video(canva_video_path)


def update_excel():
    """ Save in excel all links from canva videos """
    
    print("Getting links from canva...")
    
    # Get links from canva
    links = scraper.get_canva_video_links()

    # Save links in excel
    print()
    

def main():
    print("Select an option:\n1. Download videos\n2. Update excel\n")
    option = input("Option: ")
    if option == "1":
        download_videos()
    elif option == "2":
        update_excel()
    else:
        print("Invalid option")


if __name__ == "__main__":
    main()
