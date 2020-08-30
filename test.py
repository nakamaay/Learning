import os,requests,sys,bs4,datetime

#画像のダウンロード
def download_image(url, timeout = 10):
    response = requests.get(url, allow_redirects = False, timeout=timeout)
    if response.status_code != 200:
        raise Exception("HTTP status: " + response.status_code)

    content_type = response.headers["content-type"]
    if 'image' not in content_type:
        raise Exception("content-type: " + content_type)

    return response.content

#画像のファイル名を決める
def make_filename(base_dir, number, url):
    ext = os.path.splitext(url)[1] #拡張子の取得
    if ext != "jpg" or ext != "png" or ext != "gif":
        ext = ".png"
    filename = number + ext #番号に拡張子をつけてファイル名にする
    fullpath = os.path.join(base_dir, filename)
    return fullpath

#画像を保存する
def save_image(filename,image):
    with open(filename, "wb") as fout:
        fout.write(image)

#保存をする際にimagesというフォルダを作る
try:
    os.mkdir("./images")
except:
    pass

#指定したurlのHTMLから画像のurlを抽出し、ダウンロードする
def main():
    url = input("URLを入力してください")
    urls = []
    res = requests.get(url)
    soup = bs4.BeautifulSoup(res.text)
    for tag in soup.find_all('img'):
        urls.append(tag.get("src"))
    images_dir = './images'
    for idx,url  in enumerate(urls):
        filename = make_filename(images_dir, str(idx) , url)
        try:
            image = download_image(url)
        except:
            pass
        else:
            save_image(filename, image)

if __name__ == '__main__':
    main()
