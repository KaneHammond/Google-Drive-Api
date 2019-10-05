
import modules
from modules import *

####################################################################################
# Hello there!					                                                   #
# This short section of code will allow you to upload/download through a Google    #
# Drive account. The queries will request information when needed to accomodate    #
# the transfer. A single pickle file is needed to access your account. This will be#
# automatically created. If you wish to change the account being used, the pickle  #
# will need to be deleted and the script will make a new one. If placing this on a #
# remote device, api verification must be done on that device. This cannot be run  #
# remotely the first time. The writting of the pickle file must be approved via    #
# the web browser on each specific device the program will be used.				   #
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

# Define possible scopes for use, this single scope will give permission for both
# download and upload.

SCOPES = ['https://www.googleapis.com/auth/drive']


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
				'credentials.json', SCOPES)
			creds = flow.run_local_server(port=0)
		# Save the credentials for the next run
		with open('token.pickle', 'wb') as token:
			pickle.dump(creds, token)

	service = build('drive', 'v3', credentials=creds)

	# Call the Drive v3 API

	results = service.files().list(
		fields="nextPageToken, files(id, name)").execute()

	# collect raw file data form our google drive
	AllDriveFiles = results.get('files', [])

	# Filter items by type: We will use the csv to identify which file 
	# types are in the Google Drive.

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

	# Write Dictionary item to store each file type and list of files in.
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
	query = raw_input('Which type of file/s are you downloading?: ')

	# Verify query
	try:
		query=int(query)
	except:
		print '\nIncorrect entry format: %s' % type(query)
		print query
		pass

	if query<0 or query>i:
		print 'Value (%i) out of index range.' % query
		# Define query as number that will be out of range to ensure proper 
		# error message is delivered
		query = 99999999
		pass

	# Prepair list of items for download based upon query result and Options
	FileTypeForDown = Options[query-1]

	AvailableFiles = []
	for FileType, Items in AllData.items():
		if FileType==FileTypeForDown:
			AvailableFiles = Items

	# Has a download occured? Not yet so it is false. This is defined here 
	# as there is an alternative option for downloading .tif files which
	# is specific to image codes. If that option is chosen, then it must
	# be noted that a that download option was chosen and was successful.
	# If the image codes are not able to be parsed, it will return to the 
	# default download method.
	D = False

	##################################################################################
	#					SPECIAL TIF IMAGE FILE DOWNLOAD OPTION
	# Specify special format for .tif images. If the files are in an image 
	# collection format, this option will create folders specific to those 
	# codes. May help with organizing data. If the format of the image name 
	# is not supported, it will fail. Ex of image: LT05_033027_20080608_B3.tif
	if FileTypeForDown == 'Tagged Image File Format':
		print '\n'
		print '*'*67
		print '* Would you like to treat the image files as an image collection? *\n* Doing so will result in a special file format specific to image *\n* codes and "/" separators.                                       *'
		print '*'*67
		query = raw_input('\nEnter Y/N: ')

		query=query.upper()

		if query!='Y' and query!='N':
			print 'Incorrect entry: '
			print query
			sys.exit()
		if query=='N':
			print 'Will use tif_Files as output folder.'
		if query=='Y':
			dir = 'TIF_Code_Images'
			if not os.path.exists(dir):
			    os.makedirs(dir)
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
					# Validate query
					try:
						Number=int(Number)
					except:
						print '\nIncorrect entry format: %s' % type(Number)
						print Number
						sys.exit()
					if Number<0 or Number>len(query):
						print 'Value (%i) out of index range.' % Number
						sys.exit()
					FileOfInterest = AvailableFiles[Number-1]
					DownloadItems.append(FileOfInterest)
			if query == 'A':
				DownloadItems=AvailableFiles
			try:
				Codes = []
				for afile in DownloadItems:
					BaseName = afile
					Folder = afile[0:-7]
					Split = BaseName.split('.')
					# Select only the base code for the image file. There are 2
					LandsatCode = Split[0][0:-3]
					Codes.append(LandsatCode)
				# Filter out codes so only one exists for each image file (both B3 and B4)
				ImageCodes = collections.Counter(Codes).keys()

				# Write a folder for each image code. These codes inform the user which
				# satellite was used, the path and row, and date for the image. 
				for aCode in ImageCodes:
					dir = 'TIF_Code_Images/'+aCode
					if not os.path.exists(dir):
					    os.makedirs(dir)
					# Filter file names to select item ID
				for afile in DownloadItems:
					BaseName = afile
					for item in AllDriveFiles:
						if item['name']==BaseName:
							file_id = (item['id'])
							Folder = afile[0:-7]
					service = build('drive', 'v3', credentials=creds)
					request = service.files().get_media(fileId=file_id)

					fh = io.FileIO('TIF_Code_Images/'+Folder+'/'+BaseName, 'wb')
					downloader = MediaIoBaseDownload(fh, request)
					done = False
					while done is False:
						status, done=downloader.next_chunk()
						print ("Downloading %s" % (BaseName))
					print ("Downloaded %s" % (BaseName))
					D = True
			except:
				print '\nFailed to process image codes into folder structures.'
				print 'Will return to standard download method, please re-enter the selection.\n'

	##################################################################################

	# Unless tif images were already downloaded using a special file format, D will be false
	if D == False:
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
				# Validate query 
				try:
					Number=int(Number)
				except:
					print 'Incorrect entry format: %s' % type(Number)
					print Number
					return
				if Number<0 or Number>len(query):
					print 'Value (%i) out of index range.' % Number
					return
				FileOfInterest = AvailableFiles[Number-1]
				DownloadItems.append(FileOfInterest)
		if query == 'A':
			DownloadItems=AvailableFiles

		# Define the file ending from selected files. This will be used for our
		# folder the data will be placed into.
		FileEnding = DownloadItems[0].split('.')
		FileEnding= str(FileEnding[-1])

		# Write a file for downloading files. The name will reflect the file ending of the
		# file/files being downloaded.
		dir = FileEnding+'_Files'
		if not os.path.exists(dir):
			os.makedirs(dir)

		Out_Dir = FileEnding+'_Files/'

		# Loop through available files and download them 
		for afile in DownloadItems:
			BaseName = afile
			# Filter file names to select item ID
			for item in AllDriveFiles:
				if item['name']==BaseName:
					file_id = (item['id'])

			service = build('drive', 'v3', credentials=creds)
			request = service.files().get_media(fileId=file_id)

			fh = io.FileIO(Out_Dir+BaseName, 'wb')
			downloader = MediaIoBaseDownload(fh, request)
			done = False
			# This will return a downloading print until the file is finished.
			# If a small file, it will loop through quick.
			while done is False:
				status, done=downloader.next_chunk()
				print ("Downloading %s..." % (BaseName))
			print ("Downloaded %s" % (BaseName))


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
				'credentials.json', SCOPES)
			creds = flow.run_local_server(port=0)
		# Save the credentials for the next run
		with open('token.pickle', 'wb') as token:
			pickle.dump(creds, token)

	service = build('drive', 'v3', credentials=creds)

	# Query for file information 
	query = raw_input('\nWhich file is it you would like to download?\nEnter File Path:')
	query
	File=str(query)
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
	# Find the file format from ending of file name
	# Split the file based upon periods
	Split = FileN.split('.')
	# Select the final element of the split and re-insert 
	# a period to match a .FILETYPE format
	FileEnd = '.'+Split[-1]
	for aFormat in FileFormats:
		if FileEnd==aFormat[-1]:
			# Define the data type 
			dtype=aFormat[1]
	try:
		print '\nUploading File...'
		file_metadata = {'name': str(FileN)}
		media = MediaFileUpload(File,
		                        mimetype=dtype)
		file = service.files().create(body=file_metadata,
		                                    media_body=media,
		                                    fields='id').execute()
		print '\nUpload Completed:'
		print 'File ID: %s\nFile Name:%s' % (file.get('id'),FileN)
	except Exception as e:
		print e
		print '\nUpload Failed'
		pass


# Loop through the program 
while True:
	# Request which path is desired. Upload or download
	print '\nPlease choose a Google Drive request:\n1) File Download\n2) File Upload'
	query = raw_input('Selection (1 or 2): ')

	try:
		query = int(query)
		error = False
	except:
		print 'Incorrect query entry: '
		print query
		error = True
		pass

	if query<0 or query>2 and error==False:
		print 'Value (%i) out of index range.' % query
		pass

	if query==1:
		try:
			DOWNLOAD()
		except Exception as e:
			print e
			pass
	if query==2:
		try:
			UPLOAD()
		except Exception as e:
			print e
			pass

	query = raw_input('\nContinue with another request? (Y/N): ')

	query = query.upper()
	if query=='N':
		print '\n***EXIT***\n'
		sys.exit()