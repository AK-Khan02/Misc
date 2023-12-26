import csv
import json
import zipfile
import requests
import pdfplumber
import PyPDF2
import os
import re
import shutil


choice = input(
            "Enter [1] if you would like to get the trade history of the top 36 active member of congress traders\n"
            "Enter [2] if you want to get the trade history for a specific member of congress\n")

choice = int(choice)

while choice != 1 and choice != 2:
    choice = input(
        "Enter [1] if you would like to get the trade history of the top 36 active member of congress traders\n"
        "Enter [2] if you want to get the trade history for a specific member of congress\n")
    choice = int(choice)

year = input("Enter which year of trading history you would live to retrieve. Value must be atleast 2008\n")
year = int(year)

while year < 2008:
    year = input("Enter which year of trading history you would live to retrieve. Value must be atleast 2008\n ")
    year = int(year)

def top_36():

    list_of_congress = ["Warner", "Gianforte", "Buchanan", "Beyer", "Pelosi", "Hoeven",
                        "Feinstein", "DelBene", "Upton", "Johnson", "Williams", "Carter",
                        "Risch", "McConnell", "Daines", "Hern", "Peters", "Allen", "Norman",
                        "Doggett", "Schneider", "Shelby", "Yarmuth", "Cooper", "Bennet", "Cheney"
                        "Rice", "Foster", "Newhouse", "Maloney", "Blumenauer", "Kelly", "Mullin"
                        "Wagner", "Speier", "Tillis", "Portman", "Rochester"]

    # get zip file
    zip_file_url = f"https://disclosures-clerk.house.gov/public_disc/financial-pdfs/{year}FD.ZIP"
    pdf_file_url = f"https://disclosures-clerk.house.gov/public_disc/ptr-pdfs/{year}/"

    path = "C:\\Users\\Hp\\PycharmProjects\\copy_congress"
    os.chdir(path)

    r = requests.get(zip_file_url)
    zip_file_name = f'{year}.zip'

    list_of_pdfs = []

    with open(zip_file_name, 'wb') as f:
        f.write(r.content)

    # unzip file
    with zipfile.ZipFile(zip_file_name) as z:
        z.extractall('.')

    list_of_recent = []

    for congress_person in list_of_congress:

        try:
            new_folder = f"{congress_person}"
            os.makedirs(new_folder)
        except:
            pass

        with open(f'{year}FD.txt') as f:
            for line in csv.reader(f, delimiter='\t'):
               if line[1] == congress_person:
                   print(line)
                   date = line[7]
                   doc_id = line[8]

                   r = requests.get(f"{pdf_file_url}{doc_id}.pdf")
                   path2 = path+'\\'+new_folder
                   pdf_name = f"{doc_id}.pdf"
                   completePath = os.path.join(path2, pdf_name)

                   with open(completePath, 'wb') as pdf_file:
                       pdf_file.write(r.content)
                       list_of_pdfs.append(f"{doc_id}.pdf")
        try:
            list_of_recent.append(list_of_pdfs[-1])
        except:
            pass
        try:
            while list_of_recent[-1] == list_of_recent[-2]:
                list_of_recent.remove(-1)
        except:
            pass

    print(list_of_recent)
    #ap = list_of_pdfs[-1]

    #with pdfplumber.open(ap) as pdf:
    #    page = pdf.pages[0]
    #    text = page.extract_text()

    #with open('file.txt','w') as f:
    #    f.write(text)
    #    f.close()

def specific_member():
    congress_person = input("Enter the last name of the congress member\n")

    # get zip file
    zip_file_url = f"https://disclosures-clerk.house.gov/public_disc/financial-pdfs/{year}FD.ZIP"
    pdf_file_url = f"https://disclosures-clerk.house.gov/public_disc/ptr-pdfs/{year}/"

    path = "C:\\Users\\Hp\\PycharmProjects\\copy_congress"
    os.chdir(path)

    r = requests.get(zip_file_url)
    zip_file_name = f'{year}.zip'

    list_of_pdfs = []

    with open(zip_file_name, 'wb') as f:
        f.write(r.content)

    # unzip file
    with zipfile.ZipFile(zip_file_name) as z:
        z.extractall('.')

    list_of_recent = []

    try:
        new_folder = f"{congress_person}"
        os.makedirs(new_folder)
    except:
        pass

    with open(f'{year}FD.txt') as f:
        for line in csv.reader(f, delimiter='\t'):
            if line[1] == congress_person:
                print(line)
                date = line[7]
                doc_id = line[8]

                r = requests.get(f"{pdf_file_url}{doc_id}.pdf")
                path2 = path + '\\' + new_folder
                pdf_name = f"{doc_id}.pdf"
                completePath = os.path.join(path2, pdf_name)

                with open(completePath, 'wb') as pdf_file:
                    pdf_file.write(r.content)
                    list_of_pdfs.append(f"{doc_id}.pdf")

    print(list_of_recent)
    # ap = list_of_pdfs[-1]

    # with pdfplumber.open(ap) as pdf:
    #    page = pdf.pages[0]
    #    text = page.extract_text()

    # with open('file.txt','w') as f:
    #    f.write(text)
    #    f.close()


if choice == 1:
    top_36()

else:
    specific_member()