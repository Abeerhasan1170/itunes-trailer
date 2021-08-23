from numpy import mod
from pandas.io.parsers import read_csv
import requests
import re
import os
import shutil
import pandas as pd

GENRES = {
	1:"https://trailers.apple.com/trailers/home/feeds/genres/action_and_adventure.json",
	2:"https://trailers.apple.com/trailers/home/feeds/genres/comedy.json",
	3:"https://trailers.apple.com/trailers/home/feeds/genres/documentary.json",
	4:"https://trailers.apple.com/trailers/home/feeds/genres/drama.json",
	5:"https://trailers.apple.com/trailers/home/feeds/genres/family.json",
	6:"https://trailers.apple.com/trailers/home/feeds/genres/fantasy.json",
	7:"https://trailers.apple.com/trailers/home/feeds/genres/horror.json",
	8:"https://trailers.apple.com/trailers/home/feeds/genres/musical.json",
	9:"https://trailers.apple.com/trailers/home/feeds/genres/romance.json",
	10:"https://trailers.apple.com/trailers/home/feeds/genres/science_fiction.json",
	11:"https://trailers.apple.com/trailers/home/feeds/genres/thriller.json",
	}
genre=int(input("""
Select The Genre:
1) Action and Adventure
2) Comedy
3) Documentary
4) Drama
5) Family
6) Fantasy
7) Horror
8) Musical
9) Romance
10) Science Fiction
11) Thriller
"""))
# df_dl = pd.read_csv('test.csv')
# url_exists = df_dl['iTunes_URL'].to_list()
url = GENRES[genre]
# totalmovies = requests.get(url).json()['data']
gname = url.split("/")[-1].split(".")[0]
# numDownloads = int(input(f"How many trailer you want to download(available: {len(totalmovies)} Downloaded: {len(url_exists)}) "))
numMerge = int(input("Merge per batch: "))
# quality = int(input("Select Quality\n1)480p\n2)720p\n3)1080p\n"))
# qualities = {1:"sd",2:"hd720",3:"hd1080"}
# trailers = []
# for i in totalmovies[:numDownloads]:
# 	trailerurl = f"https://trailers.apple.com{i['location']}"
# 	trailers.append(trailerurl)
# diff = list(set(trailers)-set(url_exists))
# def getId(url):
# 	page = requests.get(url).text
# 	flimId = re.findall("[0-9]{5}",page)[1]
# 	return flimId
# def titleInfo(id,num,turl):
# 	url = f"https://trailers.apple.com/trailers/feeds/data/{id}.json"
# 	res = requests.get(url)
# 	if res.status_code == 200:
# 		res = res.json()
# 		title = [re.sub("[\\/:\"*?<>|\']+","",res['details']['locale']['en']['movie_title'])]
# 		release_date = [res['page']['release_copy']]
# 		official_url = [res['details']['official_url']]
# 		try:
# 			os.mkdir(f"trailers/{gname}/{num}-{title[0]}")
# 		except:
# 			pass
# 		playTime = ""
# 		for i in res['clips']:
# 			if i['title'].startswith('Trailer'):
# 				try:
# 					trailer_url = i['versions']['enus']['sizes'][qualities[quality]]['srcAlt']
# 					playTime = [i['faded']]
# 					# print(f'Downloading {title[0]}')
# 					# vid = requests.get(trailer_url).content
# 					# with open(f"trailers/{gname}/{num}-{title[0]}/{num}-{title[0]}.m4v",'wb') as w:
# 					# 	w.write(vid)	
# 					# with open(f"trailers/{gname}/{num}-{title}/{num}-{title}.txt",'w') as w:
# 					# 	ou = f"Official URL: {official_url}\n"
# 					# 	w.write(f"{playTime}: {title}\nRelease Date: {release_date}\n{ou if official_url else ''}\n")
# 					df = pd.DataFrame({
# 						"Title":title,
# 						"Playtime":playTime,
# 						"Official Url":official_url,
# 						"Release Date":release_date,
# 						"iTunes_URL":turl,
# 						"path":[f"trailers/{gname}/{num}-{title[0]}/{num}-{title[0]}.m4v"]
# 					}) 
# 					df.to_csv('test.csv',mode="a",header=None,index=False)
# 					break
# 				except:
# 					print('Didn\'nt find any trailer')
# 			# 
# 	else:
# 		print('Invalid Id')
# for (i,j) in zip(trailers, range(len(trailers))):
#     tid = getId(i)
#     titleInfo(tid,j,i)
# df_dl = pd.read_csv('test.csv')
# df_dl = df_dl.fillna(0)
try:
	os.mkdir(f"merged-{gname}")
except:
	pass
os.chdir(f'trailers/{gname}')
dirs = os.listdir()
dirs.sort(key=os.path.getctime)
os.chdir('../..')
p = 0
j = numMerge
k = 0
df_dl = pd.read_csv('test.csv').fillna(0)
import numpy as np
split = len(dirs)//numMerge
print(split)
df_dl = np.array_split(df_dl,split)
for i in df_dl:
	ts = i['Playtime'].to_list()
	ts.insert(0,'0:00')
	ts.pop(-1)
	i['Playtime'] = ts
	i['Playtime']=i['Playtime'].apply(lambda x:float(x.replace(':',".")))
	i['Playtime'] = i['Playtime'].cumsum()
	i['Playtime'] = i['Playtime'].apply(lambda x: format(x,'.2f').replace('.',':'))

	title = i['Title'].to_list()
	playTime = i['Playtime'].to_list()
	release_date = i['Release_Date'].to_list()
	official_url = i['Official_URL'].to_list()
	paths = i['Path'].to_list()

	for i in range(len(title)):
		d = open(f"merged-{gname}/description-{k}.txt",'a')
		ou = f"Official URL: {official_url[i]}\n"
		d.write(f"{playTime[i]} {title[i]}\nRelease Date: {release_date[i]}\n{ou if official_url[i] else ''}\n")
		d.close()
		w = open(f"mylist.txt",'a')
		w.write(f"file '{paths[i]}'\n")
		w.close()
# for _ in range(int(len(dirs)/numMerge)):
# 	for (i,n) in zip(dirs[p:j],range(len(dirs[p:j]))):
# 		w.close()
# 		d = open(f"merged-{gname}/description-{k}.txt",'a')
# 		title = df_dl['Title'].to_list()[int(i.split('-')[0])]
# 		playTime = df_dl['Playtime'].to_list()[int(i.split('-')[0])]
# 		release_date = df_dl['Release_Date'].to_list()[int(i.split('-')[0])]
# 		official_url = df_dl['Official_URL'].to_list()[int(i.split('-')[0])]
# 		ou = f"Official URL: {official_url}\n"
# 		d.write(f"{playTime}: {title}\nRelease Date: {release_date}\n{ou if official_url else ''}\n")
# # 				with open(f"trailers/{gname}/{i}/{i}.txt",'r',errors='ignore') as r:
# # 					lines = r.read()
# # 				d.write(lines)
# 		d.close()
	try:
		os.system(f"ffmpeg -f concat -safe 0 -i mylist.txt -c copy merged-{gname}/merge-{k}.m4v")
		#os.system(f"ffmpeg -i intro.mp4 -s hd720 -r 30000/1001 -video_track_timescale 30k -c:a copy merged-{gname}/merge-{k}.m4v")
		os.remove('mylist.txt')
	except:
		pass
# 	p = j
# 	j +=numMerge
	k+=1
# for i in dirs:
# 	shutil.rmtree(i)
