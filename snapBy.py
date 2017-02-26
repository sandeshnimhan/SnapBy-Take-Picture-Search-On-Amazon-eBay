from clarifai.client import ClarifaiApi
from tkinter.filedialog import askopenfilename
import webbrowser

app_id = 'KHdkLgXpiELM8iboxRLouFngP17GvNFBFQZvbHOU'
client_secret = 'GqwSx5732R5zwLCFhM42A8CAZJITFpID64in-5ZI'

clarifai_api = ClarifaiApi(app_id, client_secret)

n = input('File or URL?\n')

if n.lower() == 'file':
    filename = askopenfilename()
    result = clarifai_api.tag_images(open(filename, "rb"))
else:

    filename2 = input()
    result = clarifai_api.tag_image_urls(filename2)



classes = result['results'][0]['result']['tag']['classes']
print(classes)

url = 'http://www.ebay.com/sch/' + classes[0] + '%20' + classes[1] + '%20' + classes[2]

webbrowser.open(url, 2)