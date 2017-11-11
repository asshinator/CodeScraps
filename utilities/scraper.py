import requests
from bs4 import BeautifulSoup

def slugify(value):
    return "".join(x for x in value if x.isalnum())

def main():
    url = "https://zenpencils.com/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    comics = soup.findAll('form',attrs={'class':'comic-list-dropdown-form'})[0].findAll('option',attrs={'class':'level-0'})
    for comic in comics:
        get_image(comic['value'])
    
def get_image(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    image_url = soup.findAll('div',attrs={'id':'comic'})[0].findAll('img')[0]['src']
    img_data = requests.get(image_url).content
    name = soup.findAll('div',attrs={'id':'comic'})[0].findAll('img')[0]['alt']
    name = slugify(name)
    name = image_url.split('/')[-1] if len(name)==0 else (r"%s.%s" % (name,image_url.split('.')[-1]))
    image_saveName =r'C:\Personal\CodeScraps\data\ZenPencils\%s' % (name)
    with open(image_saveName, 'wb') as handler:
        handler.write(img_data)
    print("successfully saved %s to %s" % (image_url,image_saveName))

if __name__ == "__main__":
    if 'isNullRun' in globals():
        True
    else:
        main()