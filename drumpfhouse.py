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
        ('What Tax Cuts Have to Do with Making America Great Again',
         'What Tax Cuts Have to Do with Making Corporations Great Again'),
        ('>National Security<', '>National Insecurity<'),
        ('Christmas for Military Families at the Naval Observatory', 'VP Dunce Meets a Brown Person; is Confused'),
        ('America Will Once Again Reach for the Moon—and Beyond',
         'The Administration Will Carve Drumpf\'s Face Onto the Moon'),
        ('Of Taxes, Math, and Intellectual Honesty', 'Of Taxes, Math, and Congressional Dishonesty'),
        ('pay respect to 200 years of holiday traditions at the White House',
         'pay respect to 200 years of white privilege'),
        ('Sign Up for White House Updates', 'Sign Up for White House Propaganda'),
        ('We are MAKING AMERICA GREAT AGAIN, and much faster than anyone thought possible!',
         'We are MAKING AMERICA A POLLUTED OLIGARCHIC POLICE STATE, and much faster than anyone thought possible!'),

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
        ('Trump', 'Drumpf'),
        ('Pence', 'Dunce'),
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
