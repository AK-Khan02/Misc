import requests
import zipfile
import os
import csv

# Constants for paths and URLs
BASE_PATH = "C:\\Users\\Hp\\PycharmProjects\\copy_congress"
ZIP_FILE_URL = "https://disclosures-clerk.house.gov/public_disc/financial-pdfs/{}.zip"
PDF_FILE_URL = "https://disclosures-clerk.house.gov/public_disc/ptr-pdfs/{}/"

# List of top 36 active members of Congress for trading
TOP_36_CONGRESS_MEMBERS = [
    "Warner", "Gianforte", "Buchanan", "Beyer", "Pelosi", "Hoeven",
    "Feinstein", "DelBene", "Upton", "Johnson", "Williams", "Carter",
    "Risch", "McConnell", "Daines", "Hern", "Peters", "Allen", "Norman",
    "Doggett", "Schneider", "Shelby", "Yarmuth", "Cooper", "Bennet", "Cheney",
    "Rice", "Foster", "Newhouse", "Maloney", "Blumenauer", "Kelly", "Mullin",
    "Wagner", "Speier", "Tillis", "Portman", "Rochester"
]

def download_and_unzip(year):
    """
    Downloads and unzips the disclosure file for the given year.
    """
    zip_file_name = os.path.join(BASE_PATH, f'{year}.zip')
    with requests.get(ZIP_FILE_URL.format(year), stream=True) as r:
        r.raise_for_status()
        with open(zip_file_name, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)
    
    with zipfile.ZipFile(zip_file_name, 'r') as zip_ref:
        zip_ref.extractall(BASE_PATH)

def get_trading_history(congress_members, year):
    """
    Retrieves the trading history for the given list of congress members and year.
    """
    download_and_unzip(year)  # Download and unzip data for the given year

    for member in congress_members:
        member_path = os.path.join(BASE_PATH, member)
        os.makedirs(member_path, exist_ok=True)

        with open(os.path.join(BASE_PATH, f'{year}FD.txt')) as f:
            for line in csv.reader(f, delimiter='\t'):
                if line[1] == member:
                    print(line)  # Display the line for verification
                    doc_id = line[8]
                    pdf_path = os.path.join(member_path, f"{doc_id}.pdf")

                    with requests.get(PDF_FILE_URL.format(year) + f"{doc_id}.pdf", stream=True) as r:
                        r.raise_for_status()
                        with open(pdf_path, 'wb') as pdf_file:
                            for chunk in r.iter_content(chunk_size=8192):
                                pdf_file.write(chunk)

def main():
    choice = int(input("Enter [1] for the top 36 active Congress traders, [2] for a specific member: "))
    while choice not in [1, 2]:
        choice = int(input("Invalid choice. Enter [1] for top 36, [2] for a specific member: "))

    year = int(input("Enter the year of trading history (at least 2008): "))
    while year < 2008:
        year = int(input("Invalid year. Enter a year at least 2008: "))

    if choice == 1:
        get_trading_history(TOP_36_CONGRESS_MEMBERS, year)
    else:
        member = input("Enter the last name of the Congress member: ")
        get_trading_history([member], year)

main()
