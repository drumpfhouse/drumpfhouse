# torify wget -E -k -p --no-clobber https://www.whitehouse.gov/

import os
import fileinput

def getHTMLFileList(targetpath):
	htmlFiles = []
	for dirname, dirpaths, dirfiles in os.walk(targetpath):
		for file in dirfiles:
			if file.endswith('.html'):
				htmlFiles.append(os.path.join(dirname, file))

	return htmlFiles

def manageReplacement(filelist):
	with fileinput.FileInput(fileList, inplace=True) as file:
		try:
			for line in file:
				print(_replaceLine(line), end='')
		except:
			pass


def _replaceLine(line):
	replacementPatterns = [
		('Trump', 'Drumpf'),	
		('whitehouse.gov</title>', 'drumpfhouse.gov</title>'),
		('https://www.whitehouse.gov', 'http://www.drumpfhouse.com'),
		('The White House', 'The Drumpf House'),
		('@WhiteHouse', '@DrumpfHouse'),
		('content="whitehouse.gov"', 'content="drumpfhouse.com"'),
		('twitter.com/POTUS', 'twitter.com/drumpfhouse'),
		('twitter.com/whitehouse', 'twitter.com/drumpfhouse'),
		('embed/VBgNoP-DXWo', 'embed/7ceLnMT0rps'),
		('WHITE HOUSE', 'DRUMPF HOUSE'),
		('Let\'s Make America Great Again, Together', 'Let\'s Rape America Again, Together'),
		('The Movement Continues - The Work Begins!', 'Serve Me, You Ignorant Slobs!'),
                ('What\'s Happening', 'How We\'re Screwing You Over')
		]
	for orig, new in replacementPatterns:
		line = line.replace(orig, new)

	return line


if __name__ == '__main__':
	WGETDIR = 'www.whitehouse.gov'
	
	fileList = getHTMLFileList(WGETDIR)
	manageReplacement('fileList')
