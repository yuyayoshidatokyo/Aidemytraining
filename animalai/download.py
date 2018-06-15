from flickrapi import FlickrAPI
from urllib.request import urlretrieve
from pprint import pprint
import os, time, sys

#APIキーの情報

key = "cac4453324edc9c239c16d65a204c1a6"
secret = "380d2addb3d20ba9"
wait_time = 1

#保存フォルダの指定
animalname = sys.argv[1]
savedir = "./" + animalname

flickr =  FlickrAPI(key, secret, format="parsed-json")
result = flickr.photos.search(
    text = animalname,
    per_page = 400,
    media = "photos",
    sort = "relevance",
    safe_search = 1,
    extras = "url_q, licence"

)

photos = result["photos"]
#pprint(photos)

for i,photo in enumerate(photos['photo']):
    url_q = photo ['url_q']
    filepath = savedir + "/" + photo["id"] + '.jpg'
    if os.path.exists(filepath):continue
    urlretrieve(url_q, filepath)
    time.sleep(wait_time)
