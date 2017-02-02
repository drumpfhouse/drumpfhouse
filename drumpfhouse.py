# torify wget -E -k -p --no-clobber -m --domains www.whitehouse.gov https://www.whitehouse.gov
import fileinput
import os

def getHTMLFileList(targetpath):
	htmlFiles = []
	for dirname, dirpaths, dirfiles in os.walk(targetpath):
		for file in dirfiles:
			if file.endswith('.html'):
				htmlFiles.append(os.path.join(dirname, file))

	return htmlFiles

def manageReplacement(fileList):
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
        ('What\'s Happening', 'How We\'re Screwing You Over'),
        ('/profiles/forall/modules/custom/gov_whitehouse_www/images/icons/wh_logo_seal.png', '/dhAssets/WHlogo_trumpdoor.jpg'),
        ('../sites/whitehouse.gov/files/45/POTUS_Speech2.jpg', '/dhAssets/thisWide.jpg'),
        ('../sites/whitehouse.gov/files/45/FLOTUS_Melania1.jpg', '/dhAssets/melaniaAdminMain.jpg'),
        ('The Cabinet includes the Vice President and the heads of 15 executive departments', 'The Cabinet includes Vladimir Putin, the Vice President and the heads of 15 executive departments'),
        ('and was born on April 26, 1970 in Slovenia.', 'and was born on April 26, 1970 in Slovenia. She may not be especially bright but she don\'t hurt the eyes to look at it.'),
        ('potential and will go on to exceed anything that it has achieved in the past', 'potential to make him richer and he\'s going to exploit it for all it\'s worth'),
        ('been married to his wife, Melania', 'owned his slave wife, Melania'),
        ('first-lady-michelle-obama.html', 'first-lady-melania-trump.html')
		]
	for orig, new in replacementPatterns:
		line = line.replace(orig, new)

	return line


if __name__ == '__main__':
	WGETDIR = 'www.whitehouse.gov'
	
	fileList = getHTMLFileList(WGETDIR)
	manageReplacement(fileList)
