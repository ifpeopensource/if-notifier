import requests
from bs4 import BeautifulSoup

class News:
	def __init__(self,title,description,thumbnail,link):
		self.thumbnail = thumbnail.rstrip()
		self.title = title.rstrip()
		if description:
			self.description = description.rstrip()
		else:
			self.description = "Sem descrição!"
		self.link = link.rstrip()

	def __repr__(self):
		return f"Title:{self.title}\nDescription:{self.description}\nLink:{self.link}\nImage Link:{self.thumbnail}\n"

	def __eq__(self,o):
		return all([self.title==o.title,self.description==o.description,self.link==o.link]) 



#Retorna a url para a imagem em tamanho completo
def get_image_url(prev_url):
	new_url=prev_url[:prev_url.index("@@")]
	return new_url

def get_news(campus):
		url = f"https://www.ifpe.edu.br/campus/{campus}/noticias/todas-as-noticias"
		headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 \    (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
		html = requests.get(url=url,headers=headers).text
		parsed = BeautifulSoup(html, 'html.parser')
		news = parsed.body.find_all('div', class_="tileItem visualIEFloatFix tile-collective-nitf-content")
		nlist=[]
		for n in news:
			title_tag=n.find('a', class_="summary url")
			title=title_tag.string
			try:
				description=n.find('span', class_="description").string
			except AttributeError:
				description=None
			thumbnail=get_image_url(n.find('img', class_="tileImage")['src'])
			link=title_tag['href']

			nobject=News(title,description,thumbnail,link)

			nlist.append(nobject)
		return nlist[::-1]


if __name__ == "__main__":
	get_news("caruaru")