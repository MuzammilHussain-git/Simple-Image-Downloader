import requests
import random
def get_file(url,ext):
    r=requests.get(url)
    if r.status_code != 200:
        print("Failed to fetch the page.")
        return
    
    with open(f"Images/image {random.randint(1,999999)}.{ext}", 'wb') as f:
        f.write(r.content)
    print("File downloaded successfully.")
url=input('Enter the download link of the image: ')
ext=input('Enter the extension of the image: ')
get_file(url,ext)