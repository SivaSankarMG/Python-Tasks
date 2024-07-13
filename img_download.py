import os
import requests

def getExtensiion(url):

    extensions = [ '.png', '.jpeg', '.jpg', '.svg', '.gif' ]
    for extension in extensions:
        if extension in url:
            return extension
        
def downloadImg(url, name):

    if ext := getExtensiion(url):
        imgName = f'images/{name}{ext}'
    else:
        raise Exception('Extension not found....')

    if os.path.isfile(imgName):
        raise Exception ('Img name already exists...')
    
    try:
        imgContent = requests.get(url).content
        with open (imgName, 'wb') as handler:
            handler.write(imgContent)
            print("Downloaded successfully")
    except Exception as e:
        print(e)

if __name__ == '__main__':

    url = input("Enter a img url ")
    name = input("Enter a name for the img: ")
    
    print("Processing..")
    downloadImg(url, name)

            
