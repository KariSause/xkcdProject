import requests, os, bs4
url = 'http://xkcd.com'
os.makedirs('xkcd', exist_ok = True)
comicElem = None

while not url.endswith('#'):
	print("Загружается страница %s..." % url)
	res = requests.get(url)
	res.raise_for_status()
	soup = bs4.BeautifulSoup(res.text)
	#print(soup)

	#comicElem = soup.select('img')
	for link in soup.find_all('img'):
		#print(link.get('src'))
		#print(link.get('src').find('comics'))
		if link.get('src').find('comics') == 16:
			comicElem = link
	
	if comicElem == []:
		print('')
	else:
		comicUrl = comicElem.get('src')
		#value = 0
		#for i in comicElem:
			#print(i)     
			#print(i[value])     
			#if i[value] == 'src':
			#	print('found')
			#	break
			#else:
				#print('no Found')
				#value = value + 1 
		#print(value)
		
		#print()
		#Download photo
		print('Загружаем %s...' % (comicUrl))
		#print('Da',comicUrl)
		res = requests.get('http:'+comicUrl)
		res.raise_for_status()
		imageFile = open(os.path.join('xkcd', os.path.basename(comicUrl)), 'wb')
		for chunk in res.iter_content(100000):
			imageFile.write(chunk)
		imageFile.close()

		prevLink = soup.select('a[rel ="prev"]')[0]
		url = 'http://xkcd.com' + prevLink.get('href')



print('Done')