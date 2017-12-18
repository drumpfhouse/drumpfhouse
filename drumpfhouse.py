# torify wget -E -k -p --no-clobber -m --domains www.whitehouse.gov https://www.whitehouse.gov
import fileinput
import os
import subprocess
import sys

def setup():
    try:
        subprocess.call(['torify wget -E -k -p https://www.whitehouse.gov'],
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
        # Persistent
        ('Trump', 'Drumpf'),
        ('whitehouse.gov</title>', 'drumpfhouse.gov</title>'),
        ('The White House', 'The Drumpf House'),
        ('@whitehouse', '@drumpfhouse'),
        ('content="whitehouse.gov"', 'content="drumpfhouse.com"'),
        ('twitter.com/POTUS', 'twitter.com/drumpfhouse'),
        ('twitter.com/whitehouse', 'twitter.com/drumpfhouse'),
        ('wp-content/themes/whitehouse/assets/img/white-house-logo-footer-sm.png', 'dhAssets/WHlogo_trumpdoor.png'),
        ('wp-content/themes/whitehouse/assets/img/white-house-logo-sm-bl.png', 'dhAssets/WHlogo_trumpdoor.png'),
        ('href="https://www.whitehouse.gov/live/"', 'href="https://www.youtube.com/watch?v=oEwrsf02L_c" target=_blank'),

        # Transient
        ('A new National Security Strategy for a New Era', 'A new National Security Strategy for a New Era: Piss everyone off'),
        ('National Security', 'National inSecurity'),
        ('The Closing Argument for Tax Reform', 'Fuck the poor. Vive la rich!'),
        ('Budget That Puts America First', 'Budget That Puts Money in His Pockets'),
        ('pay respect to 200 years of holiday traditions at the White House', 'pay respect to 200 years of white privilege'),
        ('getting #2059more back in the pockets of everyday Americans', 'selling out everyday Americans')
    ]
    for orig, new in replacementPatterns:
        line = line.replace(orig, new)

    return line


if __name__ == '__main__':
    WGETDIR = 'www.whitehouse.gov'

    fileList = getHTMLFileList(WGETDIR)
    manageReplacement(fileList)
