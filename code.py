import pytesseract
from PIL import Image
from termcolor import colored
import os


f = open('output.txt', 'w')
os.system('red')
for i in range(5):
	print(colored(str(i),'green'))
	print('\nfile '+str(i)+' : ',file=f)
	img = Image.open('test'+str(i)+'.png')
	#print(img.format) 
	print(pytesseract.image_to_string(img), file=f)

f.close()