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
	old = [slash,'/',':','*','?','"','<','>','|'] #inisialisasi simbol-simbol yang tidak dapat menjadi bagian nama file
	new = ['','','','','','','','','']
	for i in range(nLink):
		url = Request(link[i], headers=HEADERS)
		page = urlopen(url)
		html = page.read().decode("utf-8")
		soup = BeautifulSoup(html, "html.parser")
		tmp = soup.title.string
		for k in range(len(old)):
			tmp = tmp.replace(old[k],new[k]) #mengganti simbol-simbol tersebut dengan spasi kosong pada array new
		judulWeb[i] =  tmp
		dokumen = soup.get_text()
		isiDokumen[i] = dokumen.encode('utf-8')

	#memasukkan teks pada array isiDokumen ke dalam folder test
	for i in range(nLink):
		fname = "../test/[web] " + judulWeb[i] + ".txt"
		with open(fname, 'wb') as text_file:
			text_file.write(isiDokumen[i])

