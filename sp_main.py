import subprocess
import sys # for sys.executable (The file path of the currently using python)
from spotdl import __main__ as spotdl # To get the location of spotdl

spotifylink = "https://open.spotify.com/track/2EhrFpsVC4rkiCf86AeVdv?si=655ab40a04ea4a26"
subprocess.check_call([sys.executable, spotdl.__file__, spotifylink])

spotdl.console_entry_point()

# in console spotdl url "link"