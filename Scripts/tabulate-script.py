#!c:\users\alex\desktop\v-dev-env\devnet_ios1\scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'tabulate==0.8.3','console_scripts','tabulate'
__requires__ = 'tabulate==0.8.3'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('tabulate==0.8.3', 'console_scripts', 'tabulate')()
    )
