#!/use/bin/env python

import os

if os.path.isdir("./temp"):
    print "/tmp is a directory."
else:
    print "/tmp is NOT a directory."
