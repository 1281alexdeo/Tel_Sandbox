#!c:\users\alex\desktop\v-dev-env\devnet_ios1\scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'virlutils==0.8.8','console_scripts','virl'
__requires__ = 'virlutils==0.8.8'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('virlutils==0.8.8', 'console_scripts', 'virl')()
    )
