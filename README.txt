****	Google Api File Transfer ****

Python 2.7.15
pip 19.2.3

INTRODUCTION:
This script was written to download and upload files from a users Google Drive account.
For my personal use I only needed to upload .zip, .csv, and .pdf files. For downloads,
I only required to download .tif and .zip files. The program works well under these 
conditions. In order to upload or download any other type of files, the code would 
need to be adjusted. This can be used on the device you are using, or on a remote 
device.

INSTALLATION:

1) Enable Google Api -
You can follow the instructions given here: [ https://developers.google.com/drive/api/
v3/quickstart/python ] for enabling your Google Drive API. This is required to ensure 
you are able to access your drive. The Drive.py code will require a credentials file 
which must be downloaded from Google, it will be an option after you enable your 
Google API via the given link. This file may have a long crazy name, you must rename 
it: credentials.json and save it to the GoogleDrive folder. 

2) Run Drive.py-
The modules.py section provided in the folder should provide you with all the files 
required to install this in python 2.7. Simply run the Drive.py file and it will 
import the required dependencies via modules.py. modules.py was written while using 
pip-19.2.3. This is important to note as the subprocess calls used in the event of a 
failed import may not be compatible with earlier versions (different syntax). After 
running Drive.py for the first time (Providing you have downloaded and renamed the 
credentials.json file) it will prompt a login link in the command prompt, as well as a 
pop up webpage on the device the code is running from. You can use the pop up to login 
to your Google account, or if accessing this code from a remote device, copy and paste 
the link provided in the prompt. Once you login, a pickle file will be created. 
Afterwhich you will not have to login again; as long as you plan on accessing the same 
Drive.

USEAGE:
Run the Drive.py file from your command prompt. Remember to change your directory to 
where the file is located. After the imports have been collected, you will be asked 
which function you are wanting to do. The options will be to download or upload files. 

If downloading files, you will be given the option to download all files with the .tif 
or .zip ending, or list them to select them individually. Regardless of your download, 
the files will be saved to the same directory as Drive.py. A folder will be created 
for .zip files, this folder will be named ZipFiles. If downloading .tif files, the 
script is specific to Landsat codes. Downloading them will result in a master 
directory file called TIFImages, within this folder subfolders will be written unique 
to the image code. Which consists of the path, row, and date of image collection. This 
was designed for downloading separate bands of imagery, keeping all image collections 
together. 

If uploading files, the first prompt will ask where the file is located. This is the
file directory ending with the name of the file. For example: 
C:\Users\Boop\le\snoot.zip where the file is snoot.zip. You can copy and paste
the file location or enter it manually, the script will process both \ and / file 
separators. After you have entered the location of the file the program will ask which
file type is being uploaded. This script will only work with .csv, .zip, and .pdf for 
file upload. A fourth option is listed which is 'Not Listed', this will simply provide 
you with a link to mimetype information (see here: https://www.freeformatter.com/
mime-types-list.html). The way the api defines the file type is based upon its 
mimetype. So other codes will have to be added if you with to upload different file 
types. This could actually be passed easily as an automated part, I just didn't do 
that.

THE END:

It isn't the best script, but it works for me. Hope you enjoy it!

Cheers!

								\m/ (>_<) \m/


