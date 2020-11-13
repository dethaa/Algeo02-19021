from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import Input_File as IF 
################# WEB SCRAPING ##################
nLink = 2
isiDokumen = ['*' for i in range(2)]
link = ['https://id.wikipedia.org/wiki/Kecerdasan_buatan','https://www.dewaweb.com/blog/kecerdasan-buatan/']
HEADERS = {'User-Agent': 'NubesSkuy'}
for i in range(nLink):
	url = Request(link[i],headers=HEADERS)
	page = urlopen(url)
	html = page.read().decode("utf-8")
	soup = BeautifulSoup(html, "html.parser")
	dokumen = soup.get_text()
	isiDokumen[i] = dokumen.encode('utf-8')
link_list = []
for i in range(2):
	link_list.append(i)
	fname = "../test/pranala" + str(i) + ".txt"
	with open(fname,'wb') as text_file:
		text_file.write(isiDokumen[i])
