import re

pattern = re.compile(r"\[Video Playback\] Attempting to resolve URL '(?:[^']|'')*'", re.IGNORECASE)
fileLocation = ""
logText = ""

def GetLog():
    try:
        global fileLocation
        fileLocation = input("Enter File Path:\n")
        file = open(fileLocation, "rt", encoding="utf8")
        global logText
        logText = file.read()
        file.close()
    except:
        print("Error: Wrong Input! Please try again.")
        GetLog()

def AskIfClose():
    userInput = input("\nPress any key to exit:\n")

def AskIfSave():
    userInput = input("\nDo you want to save these into a file? (y/n)\n")
    if userInput == "y":
        SaveFile(True)
    elif userInput == "n":
        SaveFile(False)
        AskIfClose()
    else:
        print("Error: Incorrect input! Please try again.")
        AskIfSave()
    
def SaveFile(shouldSafe):
    if not shouldSafe: return
    # Get Output Log date / time
    time = fileLocation[:-4]
    time = time[-19:]
    fileName = f"VideoPlayerURLs_{time}.txt"

    # Format URLs
    formattedURLs = ""
    for url in urls:
        formattedURLs += f"{url}\n"

    # Create File
    try:
        file = open(fileName, "x")
        file.write(f"Video Player URL(s) from \"outputlog_{time}\":\n\n{formattedURLs}")
        file.close()
        print(f"Created file \"{fileName}\"!")
        AskIfClose()
    except:
        print("Error: could not save file!")
        AskIfClose()

# Get file from user
print("Hello! I can find Video / Stream URLs in VRChat output logs!\n")
GetLog()
print("\nLooking for URls, this might take a while!\n")

# Find URLs
urls = re.findall(pattern, logText)

# Remove Duplicates
urls = list(dict.fromkeys(urls))

# Remove Prefix / Suffix
for i in range(len(urls)):
    urls[i] = urls[i][44:]
    urls[i] = urls[i][:-1]

# Print URL
if len(urls) > 0:
    print(f"Found {len(urls)} Url(s):")
    for url in urls:
        print(url)
    AskIfSave()
else:
    print("No URLs found!")
    AskIfClose()