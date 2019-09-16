# This file is for importing all required modules for the program.
import sys
import os
import os.path
import subprocess
import io

# Use subprocess if failed to import 
try:
	import pickle
except:
	subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'pickle'])
import pickle

try:
	import googleapiclient
except:
	subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'googleapiclient'])
import googleapiclient

from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

try:
	import apiclient.http
except:
	subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'apiclient.http'])
import apiclient.http

from apiclient.http import MediaIoBaseDownload
from apiclient.http import MediaFileUpload

