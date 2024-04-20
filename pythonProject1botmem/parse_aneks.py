from bs4 import BeautifulSoup

with open('aneks_html' 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f.strip(), features='lxml')

aneks_list = []
posts = soup.find_all('div', class_='post noSidePadding')
for post in posts:
    if not post.div:
        aneks_list.append(post.div.text.strip())
    print(aneks_list)