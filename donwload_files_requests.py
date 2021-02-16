import requests

def download_file():
    url: str = 'https://balanca.economia.gov.br/balanca/bd/comexstat-bd/ncm/EXP_COMPLETA.zip'
    response = requests.get(url, stream=True, allow_redirects=True, verify=False)
    handle = open('EXP_COMPLETA.zip', "wb")
    for chunk in response.iter_content(chunk_size=512):
        if chunk:
            handle.write(chunk)

if __name__ == "__main__":
    download_file()