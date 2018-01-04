# torify wget -E -k -p --no-clobber -m --domains www.whitehouse.gov https://www.whitehouse.gov
import fileinput
import os
import subprocess
import sys

def setup():
    try:
        subprocess.call(['torify wget -E -k -p -r -l 1 --exclude-directories=wp-content/uploads,live https://www.whitehouse.gov'],
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
        # Transient, front page
        ('&#039;The Rising Tide That Will Lift All Americans&#039; Boats&#039;',
         'All Your Money Are Belong To Me'),
        ('Las Vegas Review-Journal: President Reverses Rule &#039;Intended to Punish Oil and Gas Producers&#039;',
         'FDA: Fracking Pollution Part of a Complete Breakfast'),
        ('Briefing by Press Secretary Sarah Sanders 1/2/18',
         'A Verbal Train-Wreck by Press Sycophant Sarah Sanders 1/2/18'),
        ('What Vice President Pence told American Troops in Afghanistan',
         'What Lies Vice President Pence told American Troops in Afghanistan'),
        ('Every president since John Adams has occupied the White House, and the history of this building extends far beyond the construction of its walls.',
         'Every president since John Adams has occupied the White House, and they\'re all embarrassed by the current ass-clown residing there.'),
        ('Sign Up for White House Updates', 'Sign Up for White House Propaganda'),
        ('You will see great support from the United States at the appropriate time!',
         'You will see great support from the United States at the appropriate time: when you have something to off me!'),

        # Immigration page
        ('an immigration system that serves the national interest', 'an immigration system that keeps brown people out'),
        ('To restore the rule of law and secure our border', 'Out of ignorance and racist fear'),
        ('ensuring the swift removal of unlawful entrants', 'several other foolish and costly measures which will inevitably prove ineffective'),
        ('merit-based entry system', 'merit-based entry system where only the wealthy will be allowed to remain'),
        ('new citizens assimilate and flourish', 'new citizens glorify dear leader Drumpf'),

        # Economy page
        ('helping more Americans build wealth and secure their futures. Through needed tax cuts and reform, the Administration will bring jobs back to our country. The President is helping U.S. workers by expanding apprenticeship programs, reforming job training programs, and bringing businesses and educators together to ensure high-quality classroom instruction and on-the-job training.',
         'exactly as we would expect with a President who willingly sacrifices the people and the environment in the name of god money.'),

        # Persistent
        (' Trump', ' Drumpf'),
        (' Pence', ' Dunce'),
        ('whitehouse.gov</title>', 'drumpfhouse.gov</title>'),
        ('The White House', 'The Drumpf House'),
        ('@whitehouse', '@drumpfhouse'),
        ('content="whitehouse.gov"', 'content="drumpfhouse.com"'),
        ('twitter.com/POTUS', 'twitter.com/drumpfhouse'),
        ('twitter.com/whitehouse', 'twitter.com/drumpfhouse'),
        ('https://www.whitehouse.gov/wp-content/uploads/2017/12/cropped-WH.gov_favicon_512X512.png', 'http://www.drumpfhouse.com/dhAssets/WHlogo_trumpdoor.png'),
        ('https://www.whitehouse.gov/wp-content/uploads/2017/12/cropped-WH.gov_favicon_512X512-1-32x32.png', 'http://www.drumpfhouse.com/dhAssets/WHlogo_trumpdoor.png'),
        ('https://www.whitehouse.gov/wp-content/uploads/2017/12/cropped-WH.gov_favicon_512X512-1-192x192.png', 'http://www.drumpfhouse.com/dhAssets/WHlogo_trumpdoor.png'),
        ('https://www.whitehouse.gov/wp-content/uploads/2017/12/cropped-WH.gov_favicon_512X512-1-180x180.png', 'http://www.drumpfhouse.com/dhAssets/WHlogo_trumpdoor.png'),
        ('https://www.whitehouse.gov/wp-content/uploads/2017/12/cropped-WH.gov_favicon_512X512-1-270x270.png', 'http://www.drumpfhouse.com/dhAssets/WHlogo_trumpdoor.png'),
        ('wp-content/themes/whitehouse/assets/img/white-house-logo-footer-sm.png', '/dhAssets/WHlogo_trumpdoor.png'),
        ('wp-content/themes/whitehouse/assets/img/white-house-logo-sm-bl.png', '/dhAssets/WHlogo_trumpdoor.png'),
        ('href="https://www.whitehouse.gov/live/"', 'href="https://www.youtube.com/watch?v=oEwrsf02L_c" target=_blank'),
        ('../../wp-content/themes/whitehouse/assets/img/white-house-logo-sm-wh.png', '/dhAssets/WHlogo_trumpdoor.png'),
        ('Filed Under', 'Lies About'),
        ('>National Security<', '>National Insecurity<'),
    ]
    for orig, new in replacementPatterns:
        line = line.replace(orig, new)

    return line

def rebuild():
    setup()
    WGETDIR = 'www.whitehouse.gov'

    fileList = getHTMLFileList(WGETDIR)
    manageReplacement(fileList)

if __name__ == '__main__':
    rebuild()
