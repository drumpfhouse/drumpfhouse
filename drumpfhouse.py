# torify wget -E -k -p --no-clobber -m --domains www.whitehouse.gov https://www.whitehouse.gov
import fileinput
import os
import subprocess
import sys

def setup():
    try:
        subprocess.call(['torify wget -E -k -p --no-clobber -m --exclude-directories=videos --domains www.whitehouse.gov https://www.whitehouse.gov'],
                        shell=True);
    except Exception as err:
        sys.stderr.write(type(err))  # the exception instance
        sys.stderr.write(err.args)  # arguments stored in .args
        sys.stderr.write(err)  # __str__ allows args to be printed directly,


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
                try:
                        print(_replaceLine(line.encode(errors='ignore').decode()), end='')
                except Exception as err:
                        sys.stderr.write("Oops.  I shit the bed. {}".format(str(err)))
                        continue
        except Exception as err:
            sys.stderr.write("failed processing {}: {}".format(file.filename(), str(err)))

            pass

def _replaceLine(line):
    replacementPatterns = [
        ('reaffirm America\'s global leadership, continue building key relationships with world leaders, and deliver a message of unity to America\'s friends and allies', 'exploit his position to pad his own pockets, suck up to dictatorial strong men, and cut sweetheart deals for his businesses.'),
        ('shows respect for the people who pay the bills', 'shows he has no respect for the people who pay the bills'),
        ('will provide opportunities for economic growth and creation','will abandon the poor, sacrifice the environment to Big Pollution, and shit on the best aspirations of our nation'),
        ('Participate', 'Serve Drumpf'),
        ('Trump Speaks', 'Drumpf Lies'),
        ('Trump Makes Remarks', 'Drumpf Lies'),
        ('White House Press Briefing', 'Spicering the Press'),
        ('Press Briefing', 'Spicering the Press'),
        ('Remarks by', 'Lies by'),
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
        ('Believe in yourselves. Believe in your future.<br />', 'Nothing matters but what glorifies me.'),
        ('And believe, once more, in America.',''),
        ('The Movement Continues - The Work Begins!', 'Serve Me, You Ignorant Slobs!'),
        ('What\'s Happening', 'How We\'re Screwing You Over'),
        ('/profiles/forall/modules/custom/gov_whitehouse_www/images/icons/wh_logo_seal.png',
         '/dhAssets/WHlogo_trumpdoor.png'),
        ('../sites/whitehouse.gov/files/images/IMG_1086_0.JPG', '/dhAssets/thisWide.jpg'),

        ('His campaign slogan was Make America Great Again, and that is exactly what he intends to do.', 'His campaign slogan was Make America Great Again, but that\'s not at all what he intends to do.'),
        ('<img alt="First Lady Melania Drumpf" src="../sites/whitehouse.gov/files/images/inauguration.png">', '<img alt="Free Melania" src="/dhAssets/melaniaAdminMain.jpg">'),
        ('The Cabinet includes the Vice President and the heads of 15 executive departments',
         'The Cabinet includes Vladimir Putin, the Vice President and the heads of 15 executive departments'),
        ('and was born on April 26, 1970 in Slovenia.',
         'and was born on April 26, 1970 in Slovenia. She may not be especially bright but she don\'t hurt the eyes to look at it.'),
        ('potential and will go on to exceed anything that it has achieved in the past',
         'potential to make him richer and he\'s going to exploit it for all it\'s worth'),
        ('been married to his wife, Melania', 'owned his slave wife, Melania'),
        ('first-lady-michelle-obama.html', 'first-lady-melania-trump.html'),
        ('Watch the President\'s first address to a Joint Session of Congress and get more information here.', 'Watch Drumpf\'s speechwriters do their best to make him sound like a rational humanbeing and not the jabbering shit-gibbon he is.'),
        ('1600 Daily', 'Our Daily Email Blast of Bullshit'),
        ('Obamacare has led to higher costs and fewer health insurance options for millions of Americans.', 'Obamacare has secured health care for millions of Americans, but we want to take it away from you.')
    ]
    for orig, new in replacementPatterns:
        line = line.replace(orig, new)

    return line


if __name__ == '__main__':
    WGETDIR = 'www.whitehouse.gov'

    fileList = getHTMLFileList(WGETDIR)
    manageReplacement(fileList)
