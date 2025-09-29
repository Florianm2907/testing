from google_images_search import GoogleImagesSearch
import glob
import time as t

gis = GoogleImagesSearch('private key nuh uh', '44a80d11e0ff70296')
texturen = []
texturepackpng = r'C:\Users\Florian\Downloads\Pack\assets\minecraft\textures/**/*.png'
texturepackjpg = r'C:\Users\Florian\Downloads\Pack\assets\minecraft\textures/**/*.jpg'

for file in glob.glob(texturepackpng, recursive=True):
    texturen.append(file)
for file in glob.glob(texturepackjpg, recursive=True):
    texturen.append(file)
i=0

print(texturen[0].split("\\")[-1].split(".")[0])
for x in texturen:
    texturen[i].split("\\")
    suche = texturen[i].split("\\")[-1].split(".")[0]
    _search_params = {
        'q': suche + " -minecraft",
        'num': 1,
        'safe': 'off',
        'fileType': 'png',
        'imgType': 'photo',
        'imgSize': 'LARGE',
        # 'imgDominantColor': 'black|blue|brown|gray|green|orange|pink|purple|red|teal|white|yellow',
        'imgColorType': 'color',
        'rights': 'cc_publicdomain|cc_attribute|cc_sharealike|cc_noncommercial|cc_nonderived'
    }
    gis.search(search_params=_search_params, path_to_dir='./testtest/'+suche+'.png')
    print('./testtest/'+suche+'.png gespeichert.')
    t.sleep(5)