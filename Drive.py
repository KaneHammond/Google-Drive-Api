# install google-api-python-client

import modules
from modules import *

####################################################################################
# Hello there!					                                                   #
# This short section of code will allow you to upload/download files from a Google #
# Drive account. The queries will request information when needed to accomodate    #
# the transfer. A single pickle file is needed to access your account. This will be#
# automatically created. If you wish to change the account being used, the pickle  #
# will need to be deleted and the script will make a new one. If placing this on a #
# remote device, api verification can be done by copying and pasting the link      #
# (provided in the command prompt) to a web browser. File paths for uploads must   #
# contain the file drive location as well. Meaning you must start from C:\ or      #
# whatever the location is.                           							   #
####################################################################################

# Primary files supported: (The ones I needed)
# File Download = .zip and .tif
# File Upload = .pdf, .zip, and .csv


# Request which path is desired. Upload or download
print '\nPlease choose a Google Drive request:\n1) File Download\n2) File Upload'
query = raw_input('Selection (1 or 2): ')

try:
	query = int(query)
except:
	print 'Incorrect query entry: '
	print query
	sys.exit()

if query<0 or query>2:
	print 'Incorrect query entry: '
	print query
	sys.exit()


# Define possible scopes for use
# If modifying these scopes, delete the file token.pickle. These are here for 
# choosing the permission for the api connection. Each one will allow different 
# options in drive. We use SCOPESRO for listing files for download and SCOPESUP for
# the download section. SCOPES is the general one provided in a tutorial which I left
# as an option, but would have to be edited in the code.
SCOPES = ['https://www.googleapis.com/auth/drive.metadata.readonly']
SCOPESRO = ['https://www.googleapis.com/auth/drive.readonly']
# Upload
SCOPESUP = ['https://www.googleapis.com/auth/drive']

#########################################################################################
# The code


def DOWNLOAD():
	creds = None
	# The file token.pickle stores the user's access and refresh tokens, and is
	# created automatically when the authorization flow completes for the first
	# time.
	if os.path.exists('token.pickle'):
		with open('token.pickle', 'rb') as token:
			# Add try and except to pass. If teh pickle file is empty,
			# it raises an EOFError and will not continue to write creds.
			try:
				creds = pickle.load(token)
			except:
				pass
	# If there are no (valid) credentials available, let the user log in.
	if not creds or not creds.valid:
		if creds and creds.expired and creds.refresh_token:
			creds.refresh(Request())
		else:
			flow = InstalledAppFlow.from_client_secrets_file(
				'credentials.json', SCOPESRO)
			creds = flow.run_local_server(port=0)
		# Save the credentials for the next run
		with open('token.pickle', 'wb') as token:
			pickle.dump(creds, token)

	service = build('drive', 'v3', credentials=creds)

	# Call the Drive v3 API

	results = service.files().list(
		fields="nextPageToken, files(id, name)").execute()

	# Select which file type you would like to download. Currently only filters through
	# .tif and zip files.

	print ('Available file formats for downloading:\n1) .zip\n2) .tif')

	query = input('\nWhich type of file are you downloading?\n(Select 1-2):')

	if query<=0 or query>2:
		print 'Invalid selection: %i' % query
		sys.exit()
	if type(query)!=int:
		print 'Invalid selection: %f' % query
		sys.exit()
	# collect raw file data
	items = results.get('files', [])

	# Filter items by type: Only text, zip, jpg, and tif for download. Can
	# always add more if needed. I filter through to define Text and Picture files
	# but I did not need them for download just yet. But the lists are still available.
	Text = []
	Zip = []
	Pictures = []
	TIFFFILE = []
	for file in items:
		if file['name'][-4::]=='.zip':
			Zip.append(str(file['name']))

		if file['name'][-4::]=='.txt':
			Text.append(str(file['name']))

		if file['name'][-4::]=='.tif':
			TIFFFILE.append(str(file['name']))

		if file['name'][-4::]=='.jpg' or file['name'][-4::]=='.JPG':
			Pictures.append(str(file['name']))

	# Use query
	###############################
	if query==1:
		# Write list of all .tif files on the drive for download.
		# Will download all files ending with .tif
		if not Zip:
			print('No files found.')
			sys.exit()
		else:
			pass
		# Ask to download all
		print ('\n%i .zip files found...' % len(Zip))
		query = raw_input('\nDownload all .zip files?(Y/N): ')
		query=query.upper()

		# Check validity of query 
		if query != 'Y' and query != 'N':
			print '%s is not a correct entry. Please enter Y or N at prompt.' % query
			sys.exit()
		# Download all
		if query=='Y':
			# Check all Landsat Codes from images to write folders for the B4 and B3 download
			dir = 'ZipFiles/'
			if not os.path.exists(dir):
			    os.makedirs(dir)

			# Loop through available .zip to download
			for afile in Zip:
				BaseName = afile
				for item in items:
					if item['name']==BaseName:
						file_id = (item['id'])

				service = build('drive', 'v3', credentials=creds)
				request = service.files().get_media(fileId=file_id)

				print'Downloading all files...'
				fh = io.FileIO('ZipFiles/'+BaseName, 'wb')
				downloader = MediaIoBaseDownload(fh, request)
				done = False
				while done is False:
					status, done=downloader.next_chunk()
					print ("Downloaded %s" % (BaseName))
		if query=='N':
			print 'Please select the zip files your heart desires:'

			# Print the files and index values for selection.
			i = 1
			for aItem in Zip:
				print ('%i) %s' % (i, aItem))
				i=i+1 
			query = raw_input('\nEnter index values of files separated by commas (or select single file):\n')

			query = query.replace(' ', '')
			query = query.split(',')

			# Select only files chosen in query
			selection = []
			for aItem in query:
				index = int(aItem)-1
				selection.append(Zip[index])

			dir = 'ZipFiles/'
			if not os.path.exists(dir):
			    os.makedirs(dir)

			# Loop through available .zip files and download them 
			print ('Downloading selected files...')
			for afile in selection:
				BaseName = afile
				# Filter file names to select item ID
				for item in items:
					if item['name']==BaseName:
						file_id = (item['id'])

				service = build('drive', 'v3', credentials=creds)
				request = service.files().get_media(fileId=file_id)

				fh = io.FileIO('ZipFiles/'+BaseName, 'wb')
				downloader = MediaIoBaseDownload(fh, request)
				done = False
				while done is False:
					status, done=downloader.next_chunk()
					print ("Downloaded %s" % (BaseName))
	###############################
	if query==2:
		# Write list of all .tif files on the drive for download.
		# Will download all files ending with .tif if prompted
		Images = TIFFFILE
		if not TIFFFILE:
			print('No files found.')
			sys.exit()
		else:
			pass

		# Ask which files to download all or what?
		print ('\n%i .tif files found...' % len(TIFFFILE))
		query = raw_input('\nDownload all .tif files?(Y/N): ')
		query=query.upper()

		if query != 'Y' and query != 'N':
			print '%s is not a correct entry. Please enter Y or N at prompt.' % query
			sys.exit()
		if query=='Y':
			print'Downloading all .tif files from Drive...'
			# Check all Landsat Codes from images to write folders for the B4 and B3 download
			Codes = []
			for afile in Images:
				BaseName = afile
				Split = BaseName.split('.')
				# Select only the base code for the image file
				LandsatCode = Split[0][0:-3]
				Codes.append(LandsatCode)
			# Filter out codes so only one exists for each image file (both B3 and B4)
			ImageCodes = collections.Counter(Codes).keys()

			# Write a folder for each image code. These codes inform the user which
			# satellite was used, the path and row, and date for the image. 
			for aCode in ImageCodes:
				dir = 'TIFImages/'+aCode
				if not os.path.exists(dir):
				    os.makedirs(dir)

			# Loop through available .tif files and download them into the LandsatImage
			# file folder.
			print ('Downloading all files...')
			for afile in Images:
				BaseName = afile
				Folder = afile[0:-7]
				# Filter file names to select item ID
				for item in items:
					if item['name']==BaseName:
						file_id = (item['id'])
				# print (file_id)
				# sys.exit()
				service = build('drive', 'v3', credentials=creds)
				request = service.files().get_media(fileId=file_id)

				fh = io.FileIO('TIFImages//'+Folder+'/'+BaseName, 'wb')
				downloader = MediaIoBaseDownload(fh, request)
				done = False
				while done is False:
					status, done=downloader.next_chunk()
					print ("Downloaded %s" % (BaseName))
		if query=='N':
			print 'Please select the image files your heart desires:'

			# Print the files and index values for selection.
			i = 1
			for aItem in Images:
				print ('%i) %s' % (i, aItem))
				i=i+1 
			query = raw_input('\nEnter index values of images separated by commas (or select single file):\n')
			query = query.replace(' ', '')
			query = query.split(',')

			# Select only files chosen in query
			selection = []
			for aItem in query:
				index = int(aItem)-1
				selection.append(Images[index])

			Codes = []
			for afile in selection:
				BaseName = afile
				Split = BaseName.split('.')
				# Select only the base code for the image file
				LandsatCode = Split[0][0:-3]
				Codes.append(LandsatCode)
			# Filter out codes so only one exists for each image file (both B3 and B4)
			ImageCodes = collections.Counter(Codes).keys()

			# Write a folder for each image code. These codes inform the user which
			# satellite was used, the path and row, and date for the image. 
			for aCode in ImageCodes:
				dir = 'TIFImages/'+aCode
				if not os.path.exists(dir):
				    os.makedirs(dir)

			# Loop through available .tif files and download them into the LandsatImage
			# file folder.
			print ('Downloading selected files...')
			for afile in selection:
				BaseName = afile
				Folder = afile[0:-7]
				# Filter file names to select item ID
				for item in items:
					if item['name']==BaseName:
						file_id = (item['id'])
				# print (file_id)
				# sys.exit()
				service = build('drive', 'v3', credentials=creds)
				request = service.files().get_media(fileId=file_id)
				# Modified
				# fh = io.BytesIO()
				fh = io.FileIO('TIFImages/'+Folder+'/'+BaseName, 'wb')
				downloader = MediaIoBaseDownload(fh, request)
				done = False
				while done is False:
					status, done=downloader.next_chunk()
					print ("Downloaded %s" % (BaseName))

##########################################################################################


def UPLOAD():
	creds = None
	# The file token.pickle stores the user's access and refresh tokens, and is
	# created automatically when the authorization flow completes for the first
	# time.
	if os.path.exists('token.pickle'):
		with open('token.pickle', 'rb') as token:
			# Add try and except to pass. If teh pickle file is empty,
			# it raises an EOFError and will not continue to write creds.
			try:
				creds = pickle.load(token)
			except:
				pass
	# If there are no (valid) credentials available, let the user log in.
	if not creds or not creds.valid:
		if creds and creds.expired and creds.refresh_token:
			creds.refresh(Request())
		else:
			flow = InstalledAppFlow.from_client_secrets_file(
				'credentials.json', SCOPESUP)
			creds = flow.run_local_server(port=0)
		# Save the credentials for the next run
		with open('token.pickle', 'wb') as token:
			pickle.dump(creds, token)

	service = build('drive', 'v3', credentials=creds)

	# Query for file information 
	query = raw_input('\nWhich file is it you would like to download?\nEnter File Path:')
	query
	File=str(query)
	# File type
	print 'Please select the file type:\n1) .zip\n2) .pdf\n3) .csv\n4) Not Listed'
	query = raw_input('\nEnter selection: ')
	query = int(query)
	# If a file type is not listed, it can be added into the prompt above and the query below.
	if query==1:
		dtype = 'application/x-7z-compressed'
	if query==2:
		dtype = 'application/pdf'
	if query==3:
		dtype = 'text/csv'
	if query==4:
		print '\nThe file format you need requires a specific mimetype code.\nPlease see the prompted link on for adding the data type to the program:\n\nhttps://www.freeformatter.com/mime-types-list.html'
		print '\nTravel Well Land-Strider...'
		sys.exit()
	# Define the file name (Based off file location, it will bear the same name 
	# as found in its parent directory) **FileN
	# There are 2 possible ways to enter file locations. If a copy paste is done,
	# the result will be a file separator of \ as opposed to /. If \ is the file
	# separator, the string will need to be split by '\\'. In which case trying to
	# split by / will result in a single string, hence the if lenght is equal to 1
	# check.
	Temp = File.split('/')
	if len(Temp)==1:
		Temp = File.split('\\')
		File = File.replace('\\', '/')
	FileN = Temp[-1]
	print '\nUploading File...'
	file_metadata = {'name': str(FileN)}
	media = MediaFileUpload(File,
	                        mimetype=dtype)
	file = service.files().create(body=file_metadata,
	                                    media_body=media,
	                                    fields='id').execute()
	print '\nUpload Completed:'
	print 'File ID: %s\nFile Name:%s' % (file.get('id'),FileN)

#######################################################################################

# Utilize code
if query==1:
	DOWNLOAD()
if query==2:
	UPLOAD()

