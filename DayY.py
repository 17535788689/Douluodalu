#爬取斗罗大陆小说
import requests
from lxml import etree

url = 'https://dldl1.815322.xyz/xiaoshuo/1/1.html'

while True:
    headers = {
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36'
    }

    resp = requests.get(url, headers=headers)
    resp.encoding = 'utf-8'
    tree = etree.HTML(resp.text)

    url = 'https://dldl1.815322.xyz/' + tree.xpath("//td[2]/a/@href")[0]
    # url = f'https://dldl1.815322.xyz/{tree.xpath("//td[2]/a/@href")[0]}'

    info = '\n'.join(tree.xpath('//div[@class="m-post"]/p/text()'))
    title = '\n'.join(tree.xpath('//div[@class="entry-tit"]/h1/text()'))

    with open('斗罗大陆.txt', 'a+', encoding='utf-8') as f:
        f.write(title + '\n\n' + info + '\n\n')
    if url == 'https://dldl1.815322.xyz//xiaoshuo/1/':
        break