#  -----------------------------------------------------------------------
#  Copyright (c) 2022.
#  Author: Amey Bhilegaonkar
#  Copyright (c) Amey Bhilegaonkar. All rights reserved.
#  Developer Email: bhilegaonkar11@gmail.com
#  -----------------------------------------------------------------------

from Resources.Constants import DEFAULT_OS, PTH_FILE_NAME, WINDOWS_PTH_FILE_PATH, LINUX_PATH_FILE_PATH
import sys
import platform
import os

# GET CURRENT OPERATING SYSTEM
os_name = platform.system()

# GET PYTHON VERSION INFORMATION
pythonMajorVersion = sys.version_info.__getattribute__("major")
pythonMinorVersion = sys.version_info.__getattribute__("minor")

# GET PRESENT WORKING DIRECTORY - IDEALLY SHOULD BE THE FOLDER PATH
# TO PROJECT BASE DIRECTORY
currDirectory = os.getcwd()


# CHECK IF THE OS IS WINDOWS OR NOT
if os_name.lower() != DEFAULT_OS.lower():

    # IF ITS OTHER THAN WINDOWS, THEN PREPARE PATH OF LINUX
    currDirectory = currDirectory.replace("\\", "/")
    filePathDestination = LINUX_PATH_FILE_PATH.format(pythonMajorVersion, pythonMinorVersion, PTH_FILE_NAME)

else:
    # OTHERWISE, PREPARE PATH FOR WINDOWS
    currDirectory = currDirectory.replace("\\", "\\\\")

    # GET PRESENT USER IF ITS WINDOWS - IDEALLY SHOULD BE THE FOLDER PATH
    # TO PROJECT BASE DIRECTORY
    currUser = os.path.expanduser('~')
    filePathDestination = WINDOWS_PTH_FILE_PATH.format(currUser, pythonMajorVersion, pythonMinorVersion, PTH_FILE_NAME)

    filePathDestination = filePathDestination.replace("\\", "\\\\")


# CREATE A FILE WITH .PTH EXTENSIONS TO COPY IT TO SITE-PACKAGES
f = open(filePathDestination, "w+")
f.write(currDirectory)
f.close()

print("Pth file was added successfully to the path: {}".format(filePathDestination))
