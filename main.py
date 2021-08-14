import requests
import re
import os

url = "https://trailers.apple.com/trailers/home/feeds/genres.json"
action = [0,28]
comedy = [29,67]
documentry = [68,98]
drama = [99,175]
family = [176,192]
fantasy =[193,194] 
foreign =[195] 
horror  =[196,226] 
musical =[227,228] 
romance =[229,231] 
science_fiction = [232, 233]
thriller= [234,272]

def genres(url):
	genres = requests.get(url).json()
	return genres

def getId(url):
	page = requests.get(url).text
	flimId = re.findall("[0-9]{5}",page)[1]
	return flimId

def titleInfo(id):
	url = f"https://trailers.apple.com/trailers/feeds/data/{id}.json"
	res = requests.get(url)
	if res.status_code == 200:
		res = res.json()
		title = res['details']['locale']['en']['movie_title']
		description = res['details']['locale']['en']['synopsis']
		os.mkdir(title)
		with open(f"{title}/{title}.txt",'w') as w:
			w.write(description)
		for i in res['clips']:
			if i['title']=='Trailer':
				try:
					trailer_url = i['versions']['enus']['sizes']['sd']['srcAlt']
					print(f"Downloading {title}")
					vid = requests.get(trailer_url).content
					with open(f"{title}/{title}.m4v",'wb') as w:
						w.write(vid)	
					print(f"Download finished {title}")
				except:
					print('Didn\'nt find any trailer')
	else:
		print('Invalid Id')

#titleInfo(26970)
titleInfo(27201)
#print(getId("https://trailers.apple.com/trailers/independent/emily--the-edge-of-chaos/"))
