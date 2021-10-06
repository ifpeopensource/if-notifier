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


def dictToNews(d):
	title = d["title"]
	description = d["description"]
	link = d["link"]
	thumbnail = d["thumbnail"]
	return News(title,description,thumbnail,link)