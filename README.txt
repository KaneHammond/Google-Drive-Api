****	Google Api File Transfer ****
			 \m/ (>_<) \m/

Python 2.7.15
pip 19.2.3

***************************************************************************************
INTRODUCTION:
This script was written to download and upload files from a users Google Drive account.
All file formats (listed here: https://www.freeformatter.com/mime-types-list.html) are
accepted for upload and download by Google. These are mimetype codes that tell the 
server what file format is being used. They are primarily for data upload and are 
not required for the data download. You may still be able to download other file
types through the API server, but this program only sticks to 689 of 690 file formats 
provided through the freeformatter site. This ensures that the files uploaded through
the API will also be able to be downloaded. Since there are a tremendous number of 
file formats, I should mention they have not all been tested with this program.

# NOTE: Andrew Toolkit file format not supported *NO ANDREW TOOLKIT SUPPORT*
# NOTE: If dealing with unsupported files, you can place them in a .zip folder

***************************************************************************************
INSTALLATION:
1) Enable Google Api -
You can follow the instructions given here: [ https://developers.google.com/drive/api/
v3/quickstart/python ] for enabling your Google Drive API. This is required to ensure 
you are able to access your drive. The Google-API.py code will require a credentials file which must be downloaded from Google, it will be an option after you enable your 
Google API via the given link. This file may have a long crazy name, you must rename 
it: credentials.json and save it to the GoogleDrive folder.

# NOTE: When installing this on a remote device, the pick file is unique to that device
so you must physically be at the location to interact with the program before it can
be used from a remote setting.

2) Run Drive.py-
The modules.py section provided in the folder should provide you with all the files 
required to install this in python 2.7. Simply run the Google-API.py file and it will 
import the required dependencies via modules.py. modules.py was written while using 
pip-19.2.3. This is important to note as the subprocess calls used in the event of a 
failed import may not be compatible with earlier versions (different syntax). After 
running Drive.py for the first time (Providing you have downloaded and renamed the 
credentials.json file) it will prompt a login link in the command prompt, as well as a 
pop up webpage on the device the code is running from. You can use the pop up to login 
to your Google account, or if accessing this code from a remote device, copy and paste 
the link provided in the prompt. Once you login, a pickle file will be created. 
Afterwhich you will not have to login again; as long as you plan on accessing the same 
Drive Account.

***************************************************************************************
USEAGE:
Run the Google-API.py file from your command prompt (Remember to change your directory 
to where the file is located). After the imports have been collected, you will be 
asked which function you are wanting to do. The options will be to download or upload 
files. 

If downloading files, you will be given a list of file formats recognized on your
Google Drive. They will each be followed by how many files of that format are 
discovered. You will be prompted to select a file format to see the individual 
files. They will be listed and you will then be asked to enter which ones you
wish to download (All files (A) is an option). The result will be an output folder
containing the files you chose to download. The file name will be unique to the 
file format you downloaded. For example, downloading a .zip file/s will result it 
to be place in a file/directory called zip_Files. These folders and directories
will be created by the script and will be located in the working directory of 
the Google-API.py file.

# NOTE: When downloading .tif/.tiff files you will given the option to download them 
as an image collection. This will format the output folders by standard landsat image
codes. This will prevent all bands of separate images from being stored in the same
place. If it fails, the program will defualt and place them all into a tif_Files
folder.

If uploading files, the first prompt will ask where the file is located. This is the
file directory ending with the name of the file. For example: 
C:\Users\Boop\le\snoot.zip, where the file is snoot.zip. The script will process the 
file/directory name provided and find the appropriate mimetype code to allow for 
upload. All the file type codes are included in the FileTypes.csv. Additional codes
may be entered and the script should be able to process them. 

The functions/defs are written into a loop. This means after you upload or download
a file, it will not automatically exit. You will be asked if you'd like to continue
with another request. If you answer N for no, it will exit.

***************************************************************************************
END: 
That is the gyst of what this can do. Not all file formats have been tested.
The file formats that are supported through this API are listed below for reference.
Other information for them can be found here: 
https://www.freeformatter.com/mime-types-list.html
Or by opening the FileType.csv in the downloaded package. Best of luck!


############################################################
SUPPORTED FILE FORMATS (Allegedly, not all have been tested):

ZVUE Media Manager
Z.U.L. Geometry
Zip Archive
Zzazz Deck
YIN (YANG - XML)
YANG Data Modeling Language
YAML Ain't Markup Language / Yet Another Markup Language
XYZ File Format
X Window Dump
XUL - XML User Interface Language
XSPF - XML Shareable Playlist Format
SyncML
XML Transformations
Intercon FormNet
Microsoft XML Paper Specification
Express by Infoseek
X PixMap
XPInstall - Mozilla
XML-Binary Optimized Packaging
Sugar Linux Application Bundle
XML - Extensible Markup Language
Microsoft Office - OOXML - Spreadsheet Template
Microsoft Excel - Macro-Enabled Template File
Microsoft Office - OOXML - Spreadsheet
Microsoft Excel - Macro-Enabled Workbook
Microsoft Excel - Binary Workbook
Microsoft Excel
Microsoft Excel - Add-In File
eXtended Image File Format (XIFF)
XHTML - The Extensible HyperText Markup Language
Extensible Forms Description Language
Adobe XML Forms Data Format
XML Patch Framework
XML Encryption Syntax and Processing
Fujitsu - Xerox DocuWorks
Data Structure for the Security Suitability of Cryptographic Algorithms
Adobe XML Data Package
SyncML - Device Management
XML Configuration Access Protocol - XCAP Diff
X BitMap
Fujitsu - Xerox DocuWorks Binder
Microsoft XAML Browser Application
CorelXARA
Microsoft Silverlight
3D Crossword Plugin
Microsoft Windows Media Video Playlist
WebTurbo
Web Services Policy
WSDL - Web Services Description Language
Virtual Reality Modeling Language
Microsoft Wordpad
SundaHus WQ
Microsoft Works
Microsoft Windows Media Player Playlist
Wordperfect
Web Open Font Format
Microsoft Windows Media Player Skin Package
Microsoft Windows Media Audio/Video Playlist
Microsoft Windows Media Video
WMLScript
Wireless Markup Language Script (WMLScript)
Compiled Wireless Markup Language (WMLC)
Wireless Markup Language (WML)
Microsoft Windows Metafile
Microsoft Windows Media Player Download Package
Microsoft Windows Media Audio
Microsoft Windows Media
Widget Packaging and XML Configuration
Qualcomm's Plaza Mobile Internet
WebP Image
Open Web Media Project - Video
Open Web Media Project - Audio
WAP Binary XML (WBXML)
Critical Tools - PERT Chart EXPERT
WAP Bitamp (WBMP)
Microsoft Windows Media Audio Redirector
Waveform Audio File Format (WAV)
Doom Video Game
VoiceXML
Virtue VTU
Viewport+
Microsoft Visio 2013
Microsoft Visio
Vivo
Visionary
VirtualCatalog
vCalendar
Groove - Vcard
vCard
Video CD
DECE Video
DECE MP4
DECE SD Video
DECE PD Video
DECE Mobile Video
DECE Graphic
DECE High Definition Video
DECE Audio
UUEncode
User Interface Quartz - Theme (Symbian)
Ustar (Uniform Standard Tape Archive)
URI Resolution Services
Unique Object Markup Language
Unity 3d
UMAJIN
Universal Forms Description Language
Text File
Mobius Management Systems - Topic Index File
Genomatix Tuxedo Framework
SimTech MindMapper
Turtle (Terse RDF Triple Language)
TrueType Font
Tab Seperated Values
Time Stamped Data Envelope
Microsoft Windows Terminal Services
True BASIC
TRI Systems Config
Groove - Tool Template
BitTorrent
MobileTV
Tagged Image File Format
Tagged Image File Format
Microsoft Office System Release Theme
TeX Font Metric
Sharing Transaction Fraud Data
GNU Texinfo Document
TeX
Text Encoding and Interchange
SMART Technologies Apps
Tcl Script
3rd Generation Partnership Project - Transaction Capabilities Application Part
Tar File (Tape Archive)
Tao Intent
troff
OpenOffice - Writer (Text - HTML)
OpenOffice - Math (Formula)
OpenOffice - Impress (Presentation)
OpenOffice - Writer (Text - HTML)
OpenOffice - Draw (Graphics)
OpenOffice - Calc (Spreadsheet)
Arista Networks Software Image
Adobe Flash
Scalable Vector Graphics (SVG)
SourceView Document
Digital Video Broadcasting
System V Release 4 CPIO Checksum Data
System V Release 4 CPIO Archive
ScheduleUs
Close Captioning - Subtitle
OpenOffice - Writer Template (Text - HTML)
Proprietary P&G Standard Reporting System
Microsoft Trust UI Provider - Certificate Trust Link
Hyperstudio
OpenOffice - Impress Template (Presentation)
Worldtalk
OpenOffice - Draw Template (Graphics)
OpenOffice - Calc Template (Spreadsheet)
SailingTracker
Speech Synthesis Markup Language
QUASS Stream Player
Kodak Storyshare
SPARQL - Results
Search/Retrieve via URL Response Format
WAIS Source
Server-Based Certificate Validation Protocol - Validation Policies - Request
Server-Based Certificate Validation Protocol - Validation Policies - Response
In3D - 3DML
FutureSplash Animator
SMAF Phrase
Server Normal Format
Synchronized Multimedia Integration Language
StarOffice - Math
StepMania
SimpleAnimeLite Player
Microsoft Office - OOXML - Presentation (Slide)
Microsoft PowerPoint - Macro-Enabled Open XML Slide
SSEYO Koan Play File
Stuffit Archive
Stuffit Archive
Symbian Install Package
S Hexdump Format
Shell Archive
Bourne Shell Script
Standard Generalized Markup Language (SGML)
StarOffice - Writer (Global)
TIBCO Spotfire
Hydrostatix Master Suite
Secure Electronic Transaction - Registration
Secure Electronic Transaction - Payment
Java Serialized Object
Secured eMail
Secured eMail
Secured eMail
Digital Siesmograph Networks - SEED Datafiles
SeeMail
StarOffice - Writer
Session Description Protocol
SudokuMagic
StarOffice - Impress
StarOffice - Calc
StarOffice - Draw
Curl - Source Code
Server-Based Certificate Validation Protocol - Validation Response
Server-Based Certificate Validation Protocol - Validation Request
Lotus Screencam
Microsoft Schedule+
IBM Electronic Media Management System - Secure Container
Systems Biology Markup Language
SMAF Audio
Assembler Source File
Rich Text Format (RTF)
Rich Text Format
RSS - Really Simple Syndication
Really Simple Discovery
XML Resource Lists
SPARQL - Query
Nokia Radio Application - Preset
Nokia Radio Application - Preset
RetroPlatform Player
Relax NG Compact Syntax
Mobile Information Device Profile
Real Audio Sound
RealMedia
XML Resource Lists Diff
EDMICS 2000
XML Resource Lists
Hit'n'Mix
IMS Networks
Silicon Graphics RGB Bitmap
Digital Talking Book - Resource File
BusinessObjects
RemoteDocs R-Viewer
Resource Description Framework
IP Unplugged Roaming Client
CMU Image
RAR Archive
Real Audio Sound
QuarkXpress
Quicktime Video
PubliShare Objects
Quicken
Open Financial Exchange
QuickAnime Player
Microsoft PlayReady Ecosystem Video
Microsoft PlayReady Ecosystem
3M Post It Notes
3rd Generation Partnership Project - Pic Var
Microsoft Publisher
Princeton Video Image
Portable Symmetric Key Container
PSF Fonts
Photoshop Document
3rd Generation Partnership Project - Pic Small
PICSRules
Lotus Freelance
Mobipocket
Microsoft Office - OOXML - Presentation
Microsoft PowerPoint - Macro-Enabled Presentation File
Microsoft PowerPoint
Microsoft Office - OOXML - Presentation (Slideshow)
Microsoft PowerPoint - Macro-Enabled Slide Show File
Portable Pixmap Format
Adobe PostScript Printer Description File Format
Microsoft PowerPoint - Add-in file
Microsoft Office - OOXML - Presentation Template
Microsoft PowerPoint - Macro-Enabled Template File
MacPorts Port System
Portable Anymap Image
Portable Network Graphics (PNG)
Portable Network Graphics (PNG) (x-token)
Portable Network Graphics (PNG) (Citrix client)
PosML
Pronunciation Lexicon Specification
PocketLearn Viewers
Mobius Management Systems - Policy Definition Language File
3rd Generation Partnership Project - Pic Large
Internet Public Key Infrastructure - Certification Path
Internet Public Key Infrastructure - Certificate Management Protocole
JPEG Image (Progressive)
PICT Image
Pretty Good Privacy
Pretty Good Privacy - Signature
Portable Game Notation (Chess Games)
Portable Graymap Format
Portable Font Resource
PostScript Fonts
Adobe Portable Document Format
PalmOS Data
PCX Image
CURL Applet
PCL 6 Enhanced (Formely PCL XL)
HP Printer Command Language
Portable Compiled Format
Portable Bitmap Format
PowerBuilder
PawaaFILE
BAS Partitur Format
PKCS #8 - Private-Key Information Syntax Standard
PKCS #7 - Cryptographic Message Syntax Standard
PKCS #7 - Cryptographic Message Syntax Standard (Certificate Request Response)
PKCS #7 - Cryptographic Message Syntax Standard
PKCS #7 - Cryptographic Message Syntax Standard (Certificates)
PKCS #12 - Personal Information Exchange Syntax Standard
PKCS #10 - Certification Request Standard
Pascal Source File
Open Office Extension
OpenDocument Text Template
OpenDocument Spreadsheet Template
OpenDocument Presentation Template
OpenDocument Image Template
Open Document Text Web
OpenDocument Graphics Template
OpenType Font File
OpenDocument Chart Template
OSFPVG
Open Score Format
Lotus Organizer
Open eBook Publication Structure
Microsoft OneNote
Ogg
Ogg Video
Ogg Audio
OpenDocument Text
OpenDocument Spreadsheet
OpenDocument Presentation
OpenDocument Text Master
OpenDocument Image
OpenDocument Graphics
OpenDocument Formula Template
OpenDocument Formula
OpenDocument Chart
OpenDocument Database
Office Document Architecture
Microsoft Office Binder
Fujitsu Oasys
Fujitsu Oasys
Fujitsu Oasys
Lotus Notes
FlashPix
NobleNet Web
NobleNet Sealer
NobleNet Directory
Enliven Viewer
neuroLanguage
N-Gage Game Data
Navigation Control file for XML (for ePub)
Network Common Data Form (NetCDF)
Mathematica Notebook Player
Notation3
N-Gage Game Installer
MPEG Url
Triscape Map Explorer
MXML
Recordare Applications
Material Exchange Format
Medical Waveform Encoding Format
Microsoft MediaView
Recordare Applications
MUsical Score Interpreted Code Invented for the ASCII designation of Notation
Virtue MTS
Muvee Automatic Video Editing
Mobius Management Systems - Script Language
Mesh Data Type
QUASS Stream Player
3GPP MSEQ File
Media Server Control Markup Language
MARC21 XML Schema
MARC Formats
Mobius Management Systems - Query File
MiniPay
Microsoft Project
Mophun VM
Blueice Research Multipass
Apple Installer Package
MPEG Audio
MPEG Video
Mophun Certificate
MPEG-4 Audio
MPEG4
MPEG-4 Video
SGI Movie
Metadata Object Description Schema
Microsoft Money
EDMICS 2000
SMAF File
Karaoke on Chipnuts Chipsets
Dolby Meridian Lossless Packing
Motion JPEG 2000
FrameMaker Interchange Format
MIDI - Musical Instrument Digital Interface
EFI Proteus
MapGuide DBXML
Melody Format for Mobile Platform
Metadata Encoding and Transmission Standard
Metalink
Microsoft Document Imaging Format
Microsoft Access
Curl - Manifest File
Micro CADAM Helix D&D
MedCalc
Mbox database files
Mobius Management Systems - Basket file
Mathematical Markup Language
EcoWin Chart
Metadata Authority Description Schema
Mathematica Notebooks
M4v
Multimedia Playlist Unicode
M3U (Multimedia Playlist)
MPEG-21
Lotus Wordpro
Lucent Voice
Frogans Player
Microsoft Learning Resource Module
ROUTE 66 Location Based Services
Archipelago Lesson Player
Life Balance - Exchange Format
Life Balance - Desktop Edition
LaTeX
Laser App Enterprise
KDE KOffice Office Suite - Kword
Kahootz
OpenGL Textures (KTX)
KDE KOffice Office Suite - Kspread
KDE KOffice Office Suite - Kpresenter
KDE KOffice Office Suite - Kontour
Kinar Applications
Google Earth - Zipped KML
Google Earth - KML
Kidspiration
KDE KOffice Office Suite - Kformula
KDE KOffice Office Suite - Karbon
JavaScript Object Notation (JSON)
JavaScript
JPEG 2000 Compound Image File Format
JPGVideo
JPEG Image
JPEG Image (Citrix client)
Joda Archive
Java Network Launching Protocol
HP Indigo Digital Press - Job Layout Languate
RhymBox
Java Source File
Java Archive
Lightspeed Audio Lab
J2ME App Descriptor
ImmerVision PURE Players
ImmerVision PURE Players
Shana Informed Filler
iRepository / Lucidoc Editor
IBM DB2 Rights Manager
Shana Informed Filler
Internet Protocol Flow Information Export
Microsoft Class Server
Simply Accounting - Data Import
Shana Informed Filler
Micrografx iGrafx Professional
Initial Graphics Exchange Specification (IGES)
IOCOM Visimeet
igLoader
Shana Informed Filler
Image Exchange Format
iCalendar
Icon Image
CoolTalk
ICC profile
Interactive Geometry Software
HV Script
HV Voice Parameter
HV Voice Dictionary
HyperText Markup Language (HTML)
Kenamea App
Macintosh BinHex 4.0
Hewlett-Packard's WebPrintSmart
Hewlett Packard Instant Delivery
HP-GL/2 and HP RTL
WinHelp
Hierarchical Data Format
Homebanking Computer Interface (HBCI)
Hypertext Application Language
H.264
H.263
H.261
GEONExT and JSXGraph
Graphviz
Gen-Trix Studio
Groove - Tool Message
GNU Tar Files
Ghostscript Font
Speech Recognition Grammar Specification - XML
Groove - Injector
Speech Recognition Grammar Specification
GrafEq
NpGraphIt
Gnumeric
GameMaker ActiveX
Groove - Identity Message
Graphics Interchange Format
Groove - Help
GeoGebra
GeoGebra
GeoMetry Explorer
DynaGeo
Geometric Description Language (GDL)
Groove - Account
GeospacW
G3 Fax Image
GeoplanW
FuzzySheet
Adobe Flex Project
FAST Search & Transfer ASA
ANSER-WEB Terminal Client - Web Funds Transfer
FluxTime Clip
FAST Search & Transfer ASA
Friendly Software Corporation
FlashPix
Frogans Player
FrameMaker Normal Format
mod_fly / fly.cgi
FLEXSTOR
KDE KOffice Office Suite - Kivio
Flash Video
Micrografx
FLI/FLC Animation Format
Xfig
FreeHand MX
Fujitsu Oasys
FCS Express Layout Link
Forms Data Format
International Society for Advancement of Cytometry
FastBid Sheet
Flash Video
Fortran Source File
EZPix Secure Photo Album
EZPix Secure Photo Album
Novadigm's RADIA and EDM products
Efficient XML Interchange
Microsoft Application
Setext
QUASS Stream Player
MICROSEC e-Szign¢
ECMAScript
Electronic Publication
Microsoft Embedded OpenType
Digital Winds Music
Extensible MultiModal Annotation
Email Message
Proprietary P&G Standard Reporting System
Pcsel eFIF File
Novadigm's RADIA and EDM products
Novadigm's RADIA and EDM products
Nuera ECELP 9600
Nuera ECELP 7470
Nuera ECELP 4800
TIBCO Spotfire
AutoCAD DXF
DWG Drawing
Autodesk Design Web Format (DWF)
Device Independent File Format (DVI)
DTS High Definition Audio
DTS Audio
Document Type Definition
Digital Talking Book
Data Structure for the Security Suitability of Cryptographic Algorithms
PRS Lines Tag
DRA Audio
DPGraph
OSGi Deployment Package
Microsoft Office - OOXML - Word Document Template
Microsoft Word - Macro-Enabled Template
Microsoft Office - OOXML - Word Document
Microsoft Word - Macro-Enabled Document
Microsoft Word
New Moon Liftoff/DNA
Apple Disk Image
DjVu
Mobius Management Systems - Distribution Database
Adobe Shockwave Player
DreamFactory
X.509 Certificate
Debian Package
Fujitsu - Xerox 2D CAD Data
OMA Download Agents
Curl - Detached Applet
Web Distributed Authoring and Versioning
Mobius Management Systems - UniversalArchive
COLLADA
CU-Writer
Curl - Applet
CU-SeeMe
Comma-Seperated Values
Cascading Style Sheets (CSS)
Sixth Floor Media - CommonSpace
Chemical Style Markup Language
C Shell Script
CryptoNote
Internet Public Key Infrastructure - Certificate Revocation Lists
Microsoft Information Card
Compact Pro
CPIO Archive
Blackberry COD File
Corel Metafile Exchange (CMX)
CustomMenu
Chemical Markup Language
CrystalMaker Data Format
CosmoCaller
Microsoft Clipboard Clip
CrickSoftware - Clicker
CrickSoftware - Clicker - Wordbank
CrickSoftware - Clicker - Template
CrickSoftware - Clicker - Palette
CrickSoftware - Clicker - Keyboard
Java Bytecode File
Claymore Data Files
Microsoft Artgalry
ANSER-WEB Terminal Client - Certificate Issue
Crystallographic Interchange Format
KDE KOffice Office Suite - KChart
Microsoft Html Help File
pIRCh
Computer Graphics Metafile
Internet Public Key Infrastructure - Certificate
Interactive Geometry Software Cinderella
CambridgeSoft Chem Draw
ChemDraw eXchange file
Cloud Data Management Interface (CDMI) - Queue
Cloud Data Management Interface (CDMI) - Object
Cloud Data Management Interface (CDMI) - Domain
Cloud Data Management Interface (CDMI) - Contaimer
Cloud Data Management Interface (CDMI) - Capability
MediaRemote
CIM Database
Voice Browser Call Control
Microsoft Trust UI Provider - Security Catalog
CURL Applet
Microsoft Cabinet File
Clonk Game
ClueTrust CartoMobile - Config Package
ClueTrust CartoMobile - Config
C Source File
Bzip2 Archive
Bzip Archive
BTIF
Preview Systems ZipLock/VBox
Bitmap Image File
BMI Drawing Data Interchange
Binary Data
Fujitsu Oasys
RealVNC
SyncML - Device Management
Glyph Bitmap Distribution Format
Binary CPIO Archive
Amazon Kindle eBook format
AirZip FileSECURE
AirZip FileSECURE
Applixware
Audio Video Interleave (AVI)
Sun Audio - Au file format
Antix Game Player
Atom Publishing Protocol Service Document
Atom Publishing Protocol
Atom Syndication Format
ACU Cobol
Simply Accounting
Microsoft Advanced Systems Format (ASF)
Lotus Approach
Microsoft ClickOnce
Android Package Archive
AmigaDE
Digital Video Broadcasting
Adobe AIR Application
Audio Interchange File Format
PostScript
Ahead AIR Application
MO:DCA-P
Audiograph
Adaptive differential pulse-code modulation
ACU Cobol
Ace Archive
Active Content Compression
Attribute Certificate
AbiWord
Adobe (Macropedia) Authorware - Segment File
Adobe (Macropedia) Authorware - Map
Advanced Audio Coding (AAC)
Adobe (Macropedia) Authorware - Binary File
7-Zip
3GP
3GP2
In3D - 3DML
Lotus 1-2-3




