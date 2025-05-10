import img2pdf
import requests
from bs4 import BeautifulSoup
import lxml

def  get_data():
    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "user-agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36"
    }
    img_list =[]
    for i in range(1,49):
        url  =f'https://www.recordpower.co.uk/flip/Winter2020/files/mobile/{i}.jpg'
        req  =requests.get(url =url, headers=headers)
        response =req.content
        img_list.append(f"media/{i}.jpg")
        with open(f'media/{i}.jpg','wb') as f:
            f.write(response)
            print(f'Download {i} of 48')

    print('#' *20)
    print(img_list)

    with open("result.pdf","wb") as f:
        f.write(img2pdf.convert(img_list))
        print("PDF file was converted")

def main():
    get_data()


if __name__ == '__main__':
    main()