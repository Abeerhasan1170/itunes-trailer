import requests
import re
import os
import shutil

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
url = GENRES[genre]
# totalmovies = requests.get(url).json()['data']
gname = url.split("/")[-1].split(".")[0]
#numDownloads = int(input(f"How many trailer you want to download({len(totalmovies)} available) "))
numMerge = int(input("Merge per batch: "))
# quality = int(input("Select Quality\n1)480p\n2)720p\n3)1080p\n"))
# qualities = {1:"sd",2:"hd720",3:"hd1080"}
# trailers = []
# for i in totalmovies[:numDownloads]:
# 	trailerurl = f"https://trailers.apple.com{i['location']}"
# 	trailers.append(trailerurl)
# def getId(url):
# 	page = requests.get(url).text
# 	flimId = re.findall("[0-9]{5}",page)[1]
# 	return flimId
# def titleInfo(id,num,turl):
# 	url = f"https://trailers.apple.com/trailers/feeds/data/{id}.json"
# 	res = requests.get(url)
# 	if res.status_code == 200:
# 		res = res.json()
# 		title = re.sub("[\\/:\"*?<>|]+","",res['details']['locale']['en']['movie_title'])
# 		release_date = res['page']['release_copy']
# 		official_url = res['details']['official_url']
# 		os.mkdir(f"trailers/{gname}/{num}-{title}")
# 		playTime = ""
# 		for i in res['clips']:
# 			if i['title'].startswith('Trailer'):
# 				try:
# 					trailer_url = i['versions']['enus']['sizes'][qualities[quality]]['srcAlt']
# 					playTime = i['faded']
# 					vid = requests.get(trailer_url).content
# 					with open(f"trailers/{gname}/{num}-{title}/{num}-{title}.m4v",'wb') as w:
# 						w.write(vid)	
# 					print(f"Download finished {title}")
# 				except:
# 					print('Didn\'nt find any trailer')
# 		with open(f"trailers/{gname}/{num}-{title}/{num}-{title}.txt",'w') as w:
# 			ou = f"Official URL: {official_url}\n"
# 			w.write(f"{playTime}: {title}\nRelease Date: {release_date}\n{ou if official_url else ''}\n")
# 			# 
# 	else:
# 		print('Invalid Id')
# for (i,j) in zip(trailers, range(len(trailers))):
#     tid = getId(i)
#     titleInfo(tid,j,i)
try:
	os.mkdir(f"merged-{gname}")
except:
	pass
os.chdir(f'trailers/{gname}')
dirs = os.listdir()
dirs.sort(key=os.path.getctime)
p = 0
j = numMerge
import time
k = 0
for _ in range(int(len(dirs)/numMerge)):
	print(dirs[p:j])
	for i in dirs[p:j]:
		w = open(f"../../mylist.txt",'a')
		w.write(f"file 'trailers/{gname}/{i}/{i}.m4v'\n")
		w.close()
		d = open(f"../../merged-{gname}/description-{k}.txt",'a')
		with open(f"{i}/{i}.txt",'r',errors='ignore') as r:
			lines = r.read()
		d.write(lines)
		d.close()
	#os.system(f"ffmpeg -f concat -safe 0 -i ../../mylist.txt -c copy ../../merged-{gname}/merge-{k}.mp4")
	#os.remove('../../mylist.txt')
	p = j
	j +=numMerge
	k+=1
# for i in dirs[:numMerge]:
# 	numMerge += numMerge
# for i in dirs:
# 	shutil.rmtree(i)