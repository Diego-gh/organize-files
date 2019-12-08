import shutil, os

# [Folder, .extension, .extension, . . . ]
# Must be a list of lists
ORDER = [["Images", ".jpg", ".png", ".tif"],
	["Videos", ".mp4", ".MOV"],
	["Documents", ".doc",".docx", ".pdf"],
	["Music", ".mp3", ".wav", ".aac"]]

# Get the location of this script
CURRENT_DIR = os.path.dirname(os.path.realpath(__file__))

# Return folder associated with the file extension
def getFolder(file):
	for x in ORDER:
		for ext in x[1:]:
			if file.endswith(ext):
				# Extension match
				return x[0]
	# Extension not found
	return 0

# Checks if file exists before moving
def move(file, folder):
	filePath = os.path.join(CURRENT_DIR, file)
	folderPath = os.path.join(CURRENT_DIR, folder)
	tPath = os.path.join(folderPath, file)
	if os.path.exists(tPath):
		# If file exi
		print(file + " already exists in " + folder)
		return False
	else:
		shutil.move(filePath, folderPath)
		return True

# Create folders
for f in ORDER:
	fPath = os.path.join(CURRENT_DIR, f[0])
	# If the folder doesn't exist, create one
	if not os.path.exists(fPath):
		os.makedirs(fPath)

count = 0

# Iterate through all files in the directory
for file in os.listdir(CURRENT_DIR):
	# Get folder associated with file extension
	folder = getFolder(file)
	# If a match was found
	if folder != 0:
		#print(file + " - " + folder)
		if move(file, folder):
			count += 1

print(str(count) + " files moved")
