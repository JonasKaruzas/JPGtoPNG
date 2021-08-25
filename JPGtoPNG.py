import sys
import os.path
from PIL import Image

directory_from = sys.argv[1]
directory_to = sys.argv[2]

from_path = './' + directory_from + '/'
to_path = './' + directory_to

if os.path.isdir(to_path) is False:
    os.mkdir(directory_to)
    print('folderis sukurtas')

with os.scandir(directory_from) as it:
    for entry in it:
        print(entry.name)
        img = Image.open(from_path + entry.name)
        img.save(to_path + '/' + entry.name.rstrip('.jpg') + '.png', 'png')
