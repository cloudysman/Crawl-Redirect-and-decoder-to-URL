import requests

urls = [
    "https://thuvienphapluat.vn/documents/law.aspx?id=A=RNME56azTV&mode=0=JoMWIyNW5YM0JvZFd4MVl6TTWT",
    "https://thuvienphapluat.vn/documents/law.aspx?id=A=RNME56azTV&mode=09dsbGRWOHhNUTWk",
    "https://thuvienphapluat.vn/documents/law.aspx?id=g=RVMk9UVXTl&mode=h4dsbGRWOHhOVjWk",
    "https://thuvienphapluat.vn/documents/law.aspx?id=g=RVMk9UVXTl&mode=M=dsbGRWODWk",
    "https://thuvienphapluat.vn/documents/law.aspx?id=g=RVMk9UVXTl&mode=U9dsbGRWODFYekWk"
]

final_urls = []

for url in urls:
    try:
        response = requests.get(url, allow_redirects=True)
        final_urls.append(response.url)
    except requests.RequestException as e:
        final_urls.append(f"Error: {e}")

for final_url in final_urls:
    print(final_url)
