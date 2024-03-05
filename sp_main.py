import subprocess
import sys # for sys.executable (The file path of the currently using python)
from spotdl import __main__ as spotdl # To get the location of spotdl


def Download_music(link):
    ZA_link = link
    subprocess.check_call([sys.executable, spotdl.__file__, ZA_link])

    spotdl.console_entry_point()
