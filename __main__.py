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
excel_manager = SpreadsheetManager(EXCEL_FILE)
excel_manager.set_sheet(EXCEL_SHEET)
data = excel_manager.get_data()

# start scraper
print("Opening browser...")
scraper = Scraper()


def download_videos():
    """ Download canva videos from excel file and upload them to youtube """

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
        
        # TODO: update status in data
        
        # TODO: Save new data data in excel
        ## ---- all data, starting in row 2
        
        
    print("All videos uploaded to youtube")


def update_excel():
    """ Save in excel all links from canva videos """

    print("Getting links from canva...")

    # Get links from canva
    old_links = list(map(lambda row: row[0], data))
    links = scraper.get_canva_videos_links()

    # Save links in excel
    print("Saving links in excel...")
    current_rows = len(data)
    for link in links:
        
        # Skip if link already exists
        if link in old_links:
            print(f"\tLink already in excel: {link}, skipping...")
            continue
        print(f"\tSaving link: {link}...")
        
        # Save link in excel
        excel_manager.write_data([[link, "No", "No", "Yes"]], current_rows + 1)
        current_rows += 1
        excel_manager.save()

    print("Links saved in excel")


def main():
    print("Select an option:\n1. Download videos\n2. Update excel")
    option = input("Option: ")
    if option == "1":
        download_videos()
    elif option == "2":
        update_excel()
    else:
        print("Invalid option")

    update_excel()


if __name__ == "__main__":
    main()
