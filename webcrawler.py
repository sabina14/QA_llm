#import required libraries
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import os


# create folder to store data

folder_name = 'scraped_data'
if not os.path.exists(folder_name):
    os.makedirs(folder_name)
    print(f"Folder '{folder_name}' created successfully.")
else:
    print(f"Folder '{folder_name}' already exists.")

pdf_path = os.path.join(folder_name, 'output.txt')


url = 'https://docs.nvidia.com/cuda/' 
response = requests.get(url)
html_content = response.text


soup = BeautifulSoup(html_content, 'html.parser')


section_content = soup.find('section', id='cuda-toolkit-documentation-v12-6') 


with open(pdf_path, 'w',encoding='utf-8') as file:

    if section_content:
       file.write(section_content.text)
       print('Section content written successfully')
    else:
        print('section not found')

    count=0
    for link in soup.find_all('a'):
        if count==6:
            break
        else:
            
            sub_link = urljoin(url,link['href'])
            print(sub_link)
            response = requests.get(sub_link)
            html_content = response.text

        

            soup = BeautifulSoup(html_content, 'html.parser')
            div_content = soup.find('div', class_='wy-nav-content')


            if div_content:
                file.write(div_content.text)
                print('Div content written successfully')
            
            else:
                print('Div not found')
        count=count+1

