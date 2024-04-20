from bs4 import BeautifulSoup

html = '''<div style="display:block; margin:0 auto; margin-top:15px; margin-bottom:20px">
    <a class="label label-important labelMy" href="/anekdoty-pro/vovochka">анекдоты про Вовочку</a>	
    <a class="label label-important labelMy" href="/anekdoty-pro/чебурашка">анекдоты про Чебурашку</a>
    <a class="label label-important labelMy" href="/anekdoty-pro/medved">анекдоты про медведя</a>
</div>'''

soup = BeautifulSoup(html, features='lxml')
a_tags = soup.find_all('a')
data = []
for a_tag in a_tags:
    url = 'https://vse-shutochki.ru' + a_tag['href']
    category = a_tag.text
    data.append([category, url])

print(data)
