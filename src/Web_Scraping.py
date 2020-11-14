from bs4 import BeautifulSoup
from urllib.request import Request, urlopen

#prosedur untuk melakukan web scraping dari parameter input, yaitu link yang diinput oleh pengguna
def web_scrap(input):
	#memasukkan link unik pada input ke dalam array link
	link = list(set(input.split()))

	#menyimpan banyaknya jumlah link ke dalam nLink
	nLink = len(link)
	HEADERS = {'User-Agent': 'NubesSkuy'}

	#memasukkan teks hasil web-scraping ke dalam array isiDokumen
	isiDokumen = ['*' for i in range(nLink)]
	judulWeb = ['*' for i in range(nLink)]
	slash = chr(92)
	for i in range(nLink):
		url = Request(link[i], headers=HEADERS)
		page = urlopen(url)
		html = page.read().decode("utf-8")
		soup = BeautifulSoup(html, "html.parser")
		judulTemp = soup.title.string
		judulWeb[i] = judulTemp.partition('|')[0] or judulTemp.partition('<')[0] or judulTemp.partition('>')[0] or judulTemp.partition('"')[0] or judulTemp.partition('?')[0] or judulTemp.partition('*')[0] or judulTemp.partition(':')[0] or judulTemp.partition('/')[0] or judulTemp.partition(slash)[0]
		dokumen = soup.get_text()
		isiDokumen[i] = dokumen.encode('utf-8')

	#memasukkan teks pada array isiDokumen ke dalam folder test
	for i in range(nLink):
		fname = "../test/link " + judulWeb[i] + ".txt"
		with open(fname, 'wb') as text_file:
			text_file.write(isiDokumen[i])

