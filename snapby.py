from clarifai.client import ClarifaiApi
from tkinter.filedialog import askopenfilename
from nltk.util import ngrams
import webbrowser

app_id = '6XIVPtSr1oEE6WeFi5RPARxZP52jTZ99GJ8Dz9du'
client_secret = '2A-b8xB6kzmeZJp7suqstJ3L67BzmMcoc-ehOT9b'

clarifai_api = ClarifaiApi(app_id, client_secret)

n = input('File or URL?\n')

if n.lower() == 'file':
    filename = askopenfilename()
    result = clarifai_api.tag_images(open(filename, "rb"))
else:
    filename2 = input("Enter URL")
    result = clarifai_api.tag_image_urls(filename2)

classes = result['results'][0]['result']['tag']['classes']

p = int(input("Enter the level of precision 2-5\n"))

ng = ngrams(classes, p)

templist = []
for ik in ng:
    templist.append(ik)

nresults = int(input("How many results would you like to see?"))
nsites = input("ebay or Amazon or both?")

x = 0

while nresults != 0:
    if nsites.lower() == 'ebay':
        eurl = 'http://www.ebay.com/sch/' + templist[x][0] + '%20' + templist[x][1]
        webbrowser.open(eurl, 2)
    elif nsites.lower() == 'amazon':
        aurl = 'http://www.amazon.com/s/ref=nb_sb_noss_2?url=search-alias%3Daps&field-keywords=' + templist[x][0] + '%20' + templist[x][1]
        webbrowser.open(aurl, 2)
    else:
        eurl = 'http://www.ebay.com/sch/' + templist[x][0] + '%20' + templist[x][1]
        aurl = 'http://www.amazon.com/s/ref=nb_sb_noss_2?url=search-alias%3Daps&field-keywords=' + templist[x][0] + '%20' + templist[x][1]
        webbrowser.open(eurl, 2)
        webbrowser.open(aurl, 2)
    nresults -= 1
    x += 1




