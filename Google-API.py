5
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

####################################################################################
# Lets pull in some useful information. Our FileTypes.csv contains all supported file
# types for the Google API (excluding Andrew Toolkit). *NO ANDREW TOOLKIT SUPPORT*
# The list file formats will contain [File common name, mime type, file ending]

FileFormats = []
with open('FileTypes.csv') as TheCsv:
	for aItem in TheCsv:
		aItem = aItem.replace('\n', '')
		# Split the csv data by comma
		aItem = aItem.split(',')
		# Select info we want, all but the last element which consists of '\n'
		FileFormats.append(aItem)




# Request which path is desired. Upload or download
# print '\nPlease choose a Google Drive request:\n1) File Download\n2) File Upload'
# query = raw_input('Selection (1 or 2): ')

# try:
# 	query = int(query)
# except:
# 	print 'Incorrect query entry: '
# 	print query
# 	sys.exit()

# if query<0 or query>2:
# 	print 'Incorrect query entry: '
# 	print query
# 	sys.exit()


# Define possible scopes for use
# If modifying these scopes, delete the file token.pickle. These are here for 
# choosing the permission for the api connection. Each one will allow different 
# options in drive. We use SCOPESRO for listing files for download and SCOPESUP for
# the download section. SCOPES is the general one provided in a tutorial which I left
# as an option, but would have to be edited in the code.
SCOPESRO = ['https://www.googleapis.com/auth/drive.readonly']
# Upload
SCOPESUP = ['https://www.googleapis.com/auth/drive']


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

	# collect raw file data
	AllDriveFiles = results.get('files', [])

	# Filter items by type: We will use the csv to identify which file types are in the
	# Google Drive.

	FileEndings = []
	for File in AllDriveFiles:
		FileName = str(File['name'])
		# Split our file name by a period
		FileName = FileName.split('.')
		# Regarless of name, the final element from our split
		# should be the file ending. Here we add a string item
		# to re-insert a period to complete a file end item.
		# Depending on file format, this list may be incorrect.
		# This will be fixed when we cross reference the list with our csv.
		FileEndItem = '.'+FileName[-1]
		# Now we will filter out the trash! Only keep items which are actual file
		# endings, and are supported.
		for Supported in FileFormats:
			# Final element in Suported is our file ending.
			if Supported[-1]==FileEndItem:
				FileEndings.append(FileEndItem)
	# Drop doubles in FileEndings list using .keys from collections import
	FileEndings = collections.Counter(FileEndings)
	FileEndings = FileEndings.keys()

	# Write List to store each file type in.
	AllData = {}
	i = 0
	# Loop through the accepted file formats listed and write a dictionary item
	# Containing file type and list of files within each category.
	while i < len(FileEndings):
		templist = []
		for File in AllDriveFiles:
			FileNameI = str(File['name'])
			# Split our file name by a period
			FileName = FileNameI.split('.')
			# Regarless of name, the final element from our split
			# should be the file ending. Here we add a string item
			# to re-insert a period to complete a file end item.
			# Depending on file format, this list may be incorrect.
			# This will be fixed when we cross reference the list with our csv.
			FileEndItem = '.'+FileName[-1]
			if FileEndItem ==FileEndings[i]:
				templist.append(FileNameI)
		for Item in FileFormats:
			if Item[-1]==FileEndings[i]:
				Name = Item[0]
				AllData[Name]=templist
		i = i+1

	# Start our query for downloading the items.
	print '\n'
	i = 1
	# Write list of options from the print statement to match query request
	Options = []
	for FileType, Items in AllData.items():
		print '%i) File Type: %s (%i Files found)' % (i, FileType, len(Items))
		Options.append(FileType)
		i = i+1
	# Query for input
	print '\nEnter integer value below.'
	query = raw_input('Which type of file are you downloading?: ')

	# Test query
	try:
		query=int(query)
	except:
		print 'Incorrect entry format:'
		print query
		sys.exit()

	if query<0 or query>i:
		print 'Value (%i) out of index range.' % query
		sys.exit()

	# Prepair list of items for download based upon query result and Options
	FileTypeForDown = Options[query-1]

	AvailableFiles = []
	for FileType, Items in AllData.items():
		if FileType==FileTypeForDown:
			AvailableFiles = Items

	print '\nAvailable Files for Download:\n'
	i = 1
	for File in AvailableFiles:
		print '%i) %s' % (i, File)
		i = i+1
	print '\nSeparate values by commas or type A to download all files.'
	query = raw_input('Please select item/s for download:')

	# Filter the query response
	query=str(query)
	DownloadItems = []
	if query!='A':
		query = query.split(',')
		for Number in query:
			Number=int(Number)
			FileOfInterest = AvailableFiles[Number-1]
			DownloadItems.append(FileOfInterest)
	if query == 'A':
		DownloadItems=AvailableFiles

	# Define the file ending from selected files. This will be used for our
	# folder the data will be placed into.
	FileEnding = DownloadItems[0].split('.')

	dir = FileEnding+'_Files'
	if not os.path.exists(dir):
		os.makedirs(dir)

	Out_Dir = FileEnding+'_Files/'
	# WORK ON DOWNLoad
	# Loop through available files and download them 
	print ('Downloading selected files...')
	for afile in AllDriveFiles:
		BaseName = afile['name']
		print BaseName
		sys.exit()
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
	if query==3:
		# Write list of all .tif files on the drive for download.
		# Will download all files ending with .tif
		if not CredFiles:
			print('No files found.')
			sys.exit()
		else:
			pass
		# Ask to download all
		print ('\n%i .json files found...' % len(CredFiles))
		query = raw_input('\nDownload all .json files?(Y/N): ')
		query=query.upper()

		# Check validity of query 
		if query != 'Y' and query != 'N':
			print '%s is not a correct entry. Please enter Y or N at prompt.' % query
			sys.exit()
		# Download all
		if query=='Y':
			# if only one file is present, and download all is selected, it will still
			# be placed in the collection folder. This could potentially keep it separated
			# from the one in use.
			dir = 'Collection_JSON'
			if not os.path.exists(dir):
			    os.makedirs(dir)
			# Filter through .json files for download
			for afile in CredFiles:
				BaseName = afile
				for item in items:
					if item['name']==BaseName:
						file_id = (item['id'])

				service = build('drive', 'v3', credentials=creds)
				request = service.files().get_media(fileId=file_id)

				print'Downloading all files...'
				fh = io.FileIO('Collection_JSON/'+BaseName, 'wb')
				downloader = MediaIoBaseDownload(fh, request)
				done = False
				while done is False:
					status, done=downloader.next_chunk()
					print ("Downloaded %s" % (BaseName))
		### WORKING ON SECTION
		# if query=='N':
		# 	# Filter through .json files for selection
		# 	for afile in CredFiles:
		# 		BaseName = afile
		# 		for item in items:
		# 			if item['name']==BaseName:
		# 				file_id = (item['id'])

		# 		service = build('drive', 'v3', credentials=creds)
		# 		request = service.files().get_media(fileId=file_id)

		# 		print'Downloading all files...'
		# 		fh = io.FileIO(BaseName, 'wb')
		# 		downloader = MediaIoBaseDownload(fh, request)
		# 		done = False
		# 		while done is False:
		# 			status, done=downloader.next_chunk()
		# 			print ("Downloaded %s" % (BaseName))

DOWNLOAD()

