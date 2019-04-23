import os
import sys
from splitter import *

preserve_headers = False
if "-preserve-headers"  in sys.argv:
    preserve_headers = True

debug = False
if "-debug" in sys.argv:
    print("---DEBUG MODE ON---")
    debug = True

splitter = Splitter(sys.argv[1],sys.argv[2],preserve_headers,debug)
if splitter.generate():
    print("Files generated under folder "+splitter.get_folder_name())
else:
    print("File can't be split")

