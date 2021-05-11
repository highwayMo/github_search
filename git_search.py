import click
import requests
import json
import os
import pandas as pd
proxies = { "http": None, "https": None}
@click.command()
@click.option('--page', '-p', default='all', help = 'Number of messages')
@click.option('--keys', '-k', required=True, multiple=True, help = 'Key for message')
def getdata(page, keys):
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) \
                     Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3741.400 QQBrowser/10.5.3863.400"}
    # 判断文件是否存在
    datas = []
    response = None
    for key in keys:
        path = key + '.csv'
        if page != 'all':
            url = "https://api.github.com/search/repositories?q=" + key + "&sort=updated&per_page=" + str(page)
        else:
            url = "https://api.github.com/search/repositories?q=" + key + "&sort=updated&order=desc"
        if os.path.exists(path):
            df = pd.read_csv(path, header=None)
            datas = df.where(df.notnull(), None).values.tolist()  # 将提取出来的数据中的nan转化为None
        response = requests.get(url=url, headers=headers, proxies=proxies)
        data = json.loads(response.text)
        count = 0
        for i in data['items']:
            s1 = [i['name'], i['html_url'], i['description']]
            if s1 not in datas:
                print("搜索结果" + str(count) + ':' + str(s1) + "\n")
                count += 1
                datas.append(s1)
            else:
                print("搜索结果" + str(count) + "已存在!")
        pd.DataFrame(datas).to_csv(path, header=None, index=None)

if __name__ == '__main__':
  getdata()