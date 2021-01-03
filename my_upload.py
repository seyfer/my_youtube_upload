# my_upload.py
import os
import sys
from datetime import datetime, timezone, timedelta
from youtube_upload import main, lib

# file path has to be first param
fpath = sys.argv[1]

# get file title from the filename, replacing underscores with spaces
title = os.path.basename(fpath)
title = os.path.splitext(title)[0]
title = title.replace('_', ' ')

# get file time and set its timezone to my local timezone
mtime = datetime.fromtimestamp(os.path.getmtime(fpath))
AEST = timezone(timedelta(hours=10), 'AEST') # Australia EST
mtime = mtime.replace(tzinfo=AEST)
mtime = mtime.replace(microsecond=1)

# upload args - Unlisted and playlist: Family
args = [
    '--client-secrets=client_secrets.json',
    '--privacy=unlisted',
    '--title=%s' % title,
    '--recording-date=%s' % mtime.isoformat('T'),
    '--playlist=Gaming',
    fpath,
]

# debug
print(args)

sys.exit(lib.catch_exceptions(main.EXIT_CODES, main.main, args))
