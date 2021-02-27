import re
import random
import urllib.request
uapools = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:71.0) Gecko/20100101 Firefox/71.0",
    ]
def ua(uapools):
    thisua = random.choice(uapools)
    headers = ("User-Agent", thisua)
    opener = urllib.request.build_opener()
    opener.addheaders = [headers]
    urllib.request.install_opener(opener)
def get_content(page, lastId):
    url = "https://video.coral.qq.com/varticle/5963120294/comment/v2?callback=_varticle5963120294commentv2&orinum=10&oriorder=o&pageflag=1&cursor=" + lastId + "&scorecursor=0&orirepnum=2&reporder=o&reppageflag=1&source=132&_=" + str(
        page)
    html = urllib.request.urlopen(url).read().decode("utf-8", "ignore")
    return html
def get_comment(html):
    pat = '"content":"(.*?)"'
    rst = re.compile(pat, re.S).findall(html)
    return rst
def get_lastId(html):
    pat = '"last":"(.*?)"'
    lastId = re.compile(pat, re.S).findall(html)[0]
    return lastId
def saveData(comment):
    with open("comments.txt", "a+", encoding="utf-8") as file:
        for i in comment:
            i = i.replace("\n", "")
            file.write(i)
            file.write("\n")
def main():
    ua(uapools)
    page = 1614342258415
    lastId = "0"
    for i in range(0, 1000):
        html = get_content(page,lastId)
        comment = get_comment(html)
        saveData(comment)
        lastId = get_lastId(html)
        page = int(page) + 1
        print(page)
main()
