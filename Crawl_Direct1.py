import requests
from bs4 import BeautifulSoup


url = "https://thuvienphapluat.vn/hoi-dap-phap-luat/839F6DB-hd-co-duoc-su-dung-dien-thoai-khi-tham-gap-nguoi-cai-nghien-ma-tuy-khong.html"

response = requests.get(url)


if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')

    legal_links = soup.select('header.fs-6.fw-bold.p-2.m-0 + ul.news-sub-list.ms-2.me-2.mb-2 a')


    for link in legal_links:
        print(link['href'], link.get_text(strip=True))
else:
    print("Lỗi")
