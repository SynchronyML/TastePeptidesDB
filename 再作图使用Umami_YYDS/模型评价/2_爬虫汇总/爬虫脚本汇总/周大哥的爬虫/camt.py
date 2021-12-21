import re
import bs4
import openpyxl
import pandas as pd
import requests
from requests_toolbelt import MultipartEncoder

# 需要爬取的内容的文件名
old_file = "待爬取结果.xlsx"
# 爬取完毕的内容生成的文件名
new_file = "爬取结果.xlsx"


def parsing_table() -> list:
    results = []
    df = pd.read_excel(old_file, usecols=[0], names=None)
    data = df.values.tolist()
    for value in data:
        results.append(value[0])
    return results


def result(keys: str) -> str:
    data1 = """
> Test:
{}
    """.format(keys)
    parameter = MultipartEncoder(
        fields={'text': data1, 'file': ('', "", 'application/octet-stream')}
    )
    url = "http://camt.pythonanywhere.com/umamipredict"
    
    agent = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "zh-cn",
        "Content-Length": "290",
        "Origin": "http://camt.pythonanywhere.com",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.0 Safari/605.1.15",
        "Upgrade-Insecure-Requests": "1",
        "Referer": "http://camt.pythonanywhere.com/umamipredict",
        "Content-Type": parameter.content_type
    }
    
    content = requests.post(url, data=parameter, headers=agent)
    soup = bs4.BeautifulSoup(content.content, "html.parser").find_all("p")
    value = re.findall(r"(Score =[^.\d](\d+\.?\d+)[^.\d])", str(soup))
    return value[0][1]


if __name__ == '__main__':
    num = 1
    wb = openpyxl.Workbook()
    sheet = wb.active
    sheet["A1"].value = "PepName"
    sheet["B1"].value = "Scores"
    
    keys = parsing_table()
    for i in keys:
        values = result(i)
        print(i, values)
        num += 1
        str1 = "A" + str(num)
        str2 = "B" + str(num)
        sheet[str1].value = i
        sheet[str2].value = values
    wb.save(filename=new_file)