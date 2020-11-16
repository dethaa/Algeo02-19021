# Algeo02-19021
> Sebuah website lokal bernama "My Simple Search Engine" sebagai mesin pencarian 

## Daftar Isi
* [Info General](#info-general)
* [Teknologi](#teknologi)
* [Persiapan program](#persiapan-program)
* [Cara menggunakan program](#cara-menggunakan-program)
* [Status](#status)
* [Referensi](#referensi)
* [Kontak](#kontak)

## Info General
Tujuan dari pembuatan proyek ini adalah untuk memenuhi tugas besar II mata kuliah IF2123 Aljabar Linier dan Geometri semester 3 Teknik Informatika Institut Teknologi Bandung tahun ajaran 2020/2021.

## Teknologi
Python - version 3.7+

## Persiapan program
1. Download Python versi 3 di https://www.python.org/downloads/ sesuai OS masing-masing. Kami menyarankan untuk mendownload Python versi 3.7 ke atas.
2. Instal Python (Centang pilihan "*Add Python 3.X to PATH*" agar packages Python dapat diinstal melalui Command Prompt)
3. Klik kanan Command Prompt lalu klik "*Open as Administrator*"
4. Instal Python Packages berikut dengan mengetik "pip install **packages-yang-harus-diinstal**"
```bash
pip install sastrawi
```
```bash
pip install flask
```
```bash
pip install beautifulsoup4
```
5. Salin link https://github.com/dethaa/Algeo02-19021.git
6. Pilih direktori yang ingin Anda jadikan sebagai tempat programnya dengan perintah **cd**  *nama-direktori-anda*/
7. Klon link *git repository* dengan perintah berikut
```bash
git clone "https://github.com/dethaa/Algeo02-19021.git"
``` 
8. Buka folder *repository* tersebut dan persiapkan dokumen-dokumen yang menjadi data base search engine di folder test
9. Buka kembali Command Prompt
10. Buka *directory* folder src pada Command Prompt dengan perintah **cd src/**
11. Jalankan program app.py dengan perintah
```bash
python app.py
```
12. Tunggu hingga program men-generate link alamat lokal http://**alamat-lokal**/
13. Salin link tersebut secara manual (Jangan menggunakan perintah CTRL-C karena akan mengakhiri program app.py) dan buka di browser seperti Firefox atau Google Chrome
14. Program *My Simple Search Engine* dapat dijalankan

## Cara Menggunakan Program
* **Melakukan pencarian**
1. Klik tab *home* 
2. Masukkan *query*
3. Tekan enter
* **Melihat daftar dokumen**


   Klik tab daftar dokumen
* **Menambah dokumen uji dari perangkat**
1. Klik tab unggah
2. Klik *choose files*
3. Pilih file .*txt* atau .*html* yang ingin ditambahkan
4. Klik unggah


   Tunggu hingga keluar alamat lokal kembali di Command Prompt-nya, program akan *restart* karena ada perubahan pada direktori test
* **Menambah dokumen uji dengan *web scraping***
1. Klik tab unggah
2. Klik *internet (dengan url)*
3. Masukkan url
4. Tekan enter


   Tunggu hingga keluar alamat lokal kembali di Command Prompt-nya, program akan *restart* karena ada perubahan pada direktori test
* **Melihat informasi general tentang *website* My Simple Search Engine**


   Klik tab perihal

## Status
Selesai

## Referensi
* https://realpython.com/python-web-scraping-practical-introduction/
* https://stackoverflow.com/questions/53271669/count-unique-words-in-a-text-file-python
* https://www.w3schools.com/css/default.asp
* https://stackoverflow.com/questions/20668786/finding-the-index-of-sorted-elements-in-python-array
* https://www.codegrepper.com/code-examples/delphi/how+to+get+filename+without+extension+in+python
* https://www.w3schools.com/html/default.asp
* https://informatika.stei.itb.ac.id/~rinaldi.munir/AljabarGeometri/2020-2021/Algeo-12-Aplikasi-dot-product-pada-IR.pdf
* https://pypi.org/project/Sastrawi/
* https://getbootstrap.com/docs/3.3/examples/starter-template/
* https://devtrik.com/python/stopword-removal-bahasa-indonesia-python-sastrawi/
* https://stackoverflow.com/questions/39886038/writing-to-multiple-files
* https://flask.palletsprojects.com/en/1.1.x/

## Kontak
Dibuat oleh:
> KELOMPOK 20 "HMMM"
* Arjuna Marcelino - 13519021@std.stei.itb.ac.id
* Epata Tuah - 13519120@std.stei.itb.ac.id
* Sharon Bernadetha Marbun 13519092@std.stei.itb.ac.id
