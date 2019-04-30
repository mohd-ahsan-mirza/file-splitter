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
if  splitter.can_split():
    splitter.generate()
    print("Files generated under folder "+splitter.get_folder_name())
else:
    print("Rows provided in the parameters are greater than rows in the file")

