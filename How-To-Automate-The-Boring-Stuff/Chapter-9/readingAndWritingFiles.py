# CHAPTER 9: READING AND WRITING FILES

import shelve
from pathlib import Path
import os

# Variables are a fine way to store data while your program is running, but if you want
# your data to persist even after your program has finished, you need to save it to a file.
# A file's contect can be thought of as a single string value, potentially gigabytes in size.
# You will learn how to use Python to create, read, and save files on the hard drive.


# PART 1: FILES AND FILE PATHS


# A file has two key properties: a filename (usually written as one word) and a path. The path
# specifies the location of a file on the computer. For example, there is a file on my Windows
# laptop with the filename project.docx in the path C:\Users\Al\Documents. The part of the
# filename after the last period is called the file's extension and tells you a file's type.
# The filename project.docx is a Word document, and Users, Al, and Documents all refer to folders
# (also called directories). Folders can contain files and other folders. For example,
# project.docx is in the Documents folder, which is inside of the Al folder, which is inside
# the Users folder.

# The C:\ part of the path is the root folder, which contains all other folders. On Windows,
# the root folder is named C:\ and is also called the C: drive. On macOS and Linux, the root
# folder is /. In this book, I'll use the Windows-style root folder, C:\. If you are entering the
# the interactive shell examples on macOS or Linux, enter / instead.

# Additional volumes, such as DVD drive or USB flash drive, will appear differently on different
# operating systems. On Windows, they appear as new, lettered roots drives, such as D:\ or E:\.
# On macOS, they appear as new folders under the /Volumes folder. On Linux, they appear as new
# folders under the \mnt("mount") folder. Also note that while folder names and filenames are not
# case-sensitive on Windows and macOS, they are case-sensitive on Linux.

# NOTE: Since your system probably has different files and folders on it than mine, you won't
# be able to follow every example in this chapter exactly. Still, try to follow along using folders
# that exist on your computer


# BACKSLASH ON WINDOWS AND FORWARD SLASH ON MACOS AND LINUX:


# On Windows, paths are written using backslashes (\) as the separator between folder names.
# The macOS and Linux operating systems, however, use the forward slash (/) as their path
# separator. If you want your programs to work on all operating systems, you will have to write
# your Python scripts to handle both cases.

# Fortunately, this is simple to do with the Path() function in the pathlib module. If you pass
# it the string values of individual file and folder names in your path, Path() will return a string
# with a file path using the correct path separators.

''' from pathlib import Path '''
print(Path("spam", "bacon", "eggs"))

print(str(Path("spam", "bacon", "eggs")))

# Note that the convention for importing pathlib is to run from pathlib import Path, since
# otherwise we'd have to enter pathlib.Path everywhere Path shows up in our code. Not only is this
# extra typing redundant, but it's also redundant.

# If you want to get a simple text string of this path, you can pass it to the str() function,
# which in our example returns "spam\\bacon\\eggs". (Backslashes are doubles because each
# backslash needs to be escaped by another backslash character.) If I had called this function on,
# say, Linux, Path() would have returned a PosixPath object that, when passed to str(), would have
# returned "spam/bacon/eggs". (POSIX is a set of standards for Unix-like operating systems such as Linux.)

# These Path objects (really, WindowsPath or PosixPath objects, depending on your operating systems)
# will be passed to several of the file-related functions introduced in this chapter.
# For example, the following code joins names from a list of filenames to the end of a folder's name:

# from pathlib import Path
myFiles = ["accounts.txt", "details.csv", "invite.docx"]
for fileName in myFiles:
    print(Path(r"C:\Users\Al", fileName))

# On windows, the backslash separates directories, so you can't use it in filenames. However you can use
# backslashes in filenames on macOS and Linux. So while Path(r"spam\eggs") refers to two separate
# folders (or a file eggs in folder spam) on Windows, the same command would refer to a single folder
# (or file) named spam\eggs on macOS and Linux. For this reason, it's usually a good idea to always use
# forward slashes in your Python code (and I'll be doing so for the rest of this chapter).
# The pathlib module will ensure that it always works on all operating systems.


# USING THE / OPERATOR TO JOIN PATHS:


# We normally use the + operator to add two integer or floating-point numbers, such as in the expression
# 2 + 2, which evaluates to the integer value 4. But we can also use the + operator to concatenate two
# strings values, like the expression "Hello" + "World", which evaluates to the string value "HelloWorld".

# Similarly, the / operator that we normally use for division can also combine Path objects and strings.
# This is helpful for modifying a Path object after you've already created it with the Path() function.

# from pathlib import Path
print(Path("spam") / "bacon" / "eggs")
print(Path("spam") / Path("bacon/eggs"))
print(Path("spam") / Path("bacon", "eggs"))

# Using the \ operator with Path objects makes joining paths just as easy as string concatenation. It's also
# safe than using concatenation or the join() method, like we do in this example.

homeFolder = r"C:\Users\Al"
subFolder = "spam"
homeFolder + "\\" + subFolder
print("\\".join([homeFolder, subFolder]))

# A script that uses this code isn't safe; because its backslashes would only work on Windows. You could add an
# if statement that checks sys.platform (which contains a string describing the computer's operating system) to
# decide what kind of slash to use, but applying this custom code everywhere it's needed can be inconsistent
# and bug-prone.

# The pathlib module solves these problems by reusing the / math division operator to join paths correctly,
# no matter what operating system your code is running on. The following example uses this strategy to join
# the same paths as in the previous example:

homeFolder = Path("C:/Users/Al")
subFolder = Path("spam")
homeFolder / subFolder
print(str(homeFolder / subFolder))

# The only thing you need to keep in mind when using the / operator for joining paths is that one of the
# first two values must be a Path object. Python will give you an error if you try entering the following
# into the interactive shell.

''' "spam" / "bacon" / "eggs" '''
# NOTE: This will cause an error because we are not joining Path objects

# Python evaluates the / operator from left to right and evaluates to a Path object, so
# either the first or second leftmost value must be a Path object for the entire expression to
# evaluate to a Path object. Here's how the / operator and a Path object evaluate to the final Path object.

# If you see the TypeError: unsupported operand type(s) for /: "str" and "str" error message shown
# previously, you need to put a Path object on the left side of the expression.

# The / operator replaces the older os.path.join() function which you can learn more about from
# https://docs.python.org/3/library/os.path.html#os.path.join.


# THE CURRENT WORKING DIRECTORY:


# Every program that runs on your computer has a current working directory, or cwd. Any filenames or paths
# that do not begin with the root folder are assumed to be under the current working directory.

# NOTE: While folder is the more mordern name for directory, note that current working direcotry
# (or just working directory) is the standard term, no "current working folder"

# You can get the current working directory as a string value with the Path.cwd() function and change it using
# os.chdir(). Enter the following into the interactive shell:

# NOTE: type this in the interactive shell instead.
''' from pathlib import Path '''
''' import os '''

''' Path.cwd() '''
''' os.chdir("C:\\Windows\\System32") '''
''' Path.cwd() '''

# Here, the current working directory is set to C:\Users\Al\AppData\Local\Programs\Python\Python37.
# so the filename project.docx refers to C:\Users\Al\AppData\Local\Programs\Python\Python37\project.docx.
# When we change the current working directory to C:\Windows\System32, the filename project.docx is
# interpreted as C:\Windows\System32\project.docx.

# Python will display an error if you try to change to a directory that does not exist.

''' os.chdir("C:/ThisFolderDoesNotExist") '''
# NOTE: this will cause an error because the directory does not ThisFolderDoesNotExist

# There is no pathlib function for changing the working directory, because changing the current
# working directory while a program is running can often lead to subtle bugs.

# The os.getcwd() function is the older way of getting the current working directory as a string.


# THE HOME DIRECTORY:


# All users have a folder for their own files on the computer called the home directory or home folder.
# You can get a Path object of the home folder by calling Path.home():

print(Path.home())

# The home directories are located in a set place depending on your operating system:
# - On Windows, home directories are under C:\Users.
# - On Mac, home directories are under /Users.
# - On Linus, home directories are often under /home.

# Your scripts will almost certainly have permissions to read and write the files under your home directory,
# so it's an ideal place to put the files that your Python programs will work with.


# ABSOLUTE VS. RELATIVE PATHS:


# There are two ways to specify a file path:
# - An absolute path, which always begins with the root folder
# - A relative path, which is relative to the program's current working directory

# There are also the dot (.) and dot-dot (..) folders. There are not real folders but special names
# that can be used in a path. A single period ("dot") for a folder name is shorthand for "this directory."
# Two periods ("dot-dot") means "the parent folder"

# Figure 9-2 is an example of some folders and files. When the current working directory is set to C:\bacon,
# the relative paths for the other folders and files are set as they are in the figure.

# NOTE: LINE  UP THE THIS LINE HERE TO WHERE THE TOP OF THE LINTER ERROR MESSAGES / DISPLAY STARTS
# THEN USE LINE 180 AS A REFERENCE POINT TO SCROLL DOWN TO FIGURE 9-2 ONILNE.
# YOU WANT TO MATCH THE SCROLL BAR TO THE LEVEL OF 180!!

# The .\ at the start of a relative path is optional. For example, .\spam.txt and spam.txt refer to the
# same file.


# CREATING NEW FOLDERS USING THE OS.MAKEDIRS() FUNCTION:

# Your programs can create new folders (directories) with the os.makedirs() function. Enter
# the following into the interactive shell

''' import os '''
''' os.makedirs("C:\\delicious\\walnut\\waffles") '''

# This will create not just the C:\delicious folder but also a walnut folder inside C:\delicious and a
# waffles folder inside C:\delicious\walnut. That is, os.makedirs() will create any necessary intermediate
# folders in order to ensure that the full path exists.

# FIGURE 9-3 shows this hierachy of FOLDERS
# C:\
#   delicious
#       walnut
#           waffles

# To make a directory form a Path object, call the mkdir() method. For example, this code will create a
# spam folder under the home folder on my computer.

''' from pathlib import Path '''  # NOTE: below line needs to be added in as well
# Path(r"C:\Users\Al\spam").mkdir()


# HANDLING ABSOLUTE AND RELATIVE PATHS

# The pathlib module provides methods for checking whether a given path is an absolute path and
# returning the absolute path of a relative path.

# Calling the is_absolute() method on a Path object will return True if it represents an absolute path or False
# if it represents a relative path. For example, enter the following into the interactive shell, using your
# own files and folders instead of the exact ones listed here:

''' Path.cwd() '''
''' Path.cwd().isabsolute() '''
''' Path("spam/bacon/eggs").is_absolute() '''

# To get an absolute path from a relative path, you can put Path.cwd() / in front
# of the relative Path object. After all, when we say "relative path," we almost always mean
# a path that is relative to the current working directory.

# Enter the following into the interactive shell:

''' Path("my/relative/path") '''
''' Path.cwd() / Path("my/relative/path") '''

# If your relative path is relative to another path besides the current working directory, just
# replace Path.cwd() with that other path instead. The following example gets an absolute path using the
# home directory instead of the current working directory:

''' Path("my/relative/path") '''
''' Path.home() / Path("my/relative/path') '''

# the os.path module also has some useful functions related to absolute and relative paths:
# - Calling os.path.abspath(path) will return a string of the absolute path of the argument.
#   this is an easy way to convert a relative path into an absolute one.
# - Calling os.path.isabs(path) will return True if the argument is an absolute path and False if it is
# a relative path.
# - Calling os.path.relpath(path, start) will return a string of a relative path from the start path to path.
# If start is not provided, the current working directory is used as the start path.

# Try these functions in the interactive shell:

''' os.path.relpath("C:\\Windows", "C:\\") '''
''' os.path.relpath("C:\\Windows", "C:\\spam\\eggs") '''

# When the relative path is within the same parent folder as the path, but is
# within subfolders of a different path, such as "C:\\Windows" and "C:\\spam\\eggs", you can use the
# "dot-dot" notation to return to the parent folder.

# When the relative path is within the same parent folder as the path, but is within subfolders of a
# different path, such as "C:\\Windows" and "C:\\spam\\eggs", you can use the "dot-dot" notation to return
# to the parent folder.


# GETTING THE PARTS OF FILE PATH:


# Given a Path object, you can extrat the file path's different parts as strings using several Path object
# attributes. These can be useful for constructing new file paths based on existing ones. The attributes
# are diagrammed in Figure 9-4.

# The parts of a file path include the following:

# - The anchor: which is the root folder of the file system
# - The drive (on windows): which is the single letter that often denotes a phyical hard drive or other
# storage device
# - The parent, which is the folder that contains the file
# - The name of the file, made up of the stem (or base name) and the suffix (or extension)

# Note that Windows Path objects ahve a drive attibute, but macOS and Linux Path objects don't.
# The drive attribute doesn't include the first backslash.

# To extract each attribute from the file path, enter the following into the interactive shell:

p = Path("C:/Users/Al/spam.txt")
print(p.anchor)

print(p.parent)  # This is a Path object, not a string.

print(p.name)

print(p.stem)

print(p.suffix)

print(p.drive)

# NOTE: These attributes evaluate to simple string values, except for parent, which evaluates to another Path Object.
# The parentS attribute (which is different from the parenT attribute) evaluates to the ancestor folders of a
# Path object with an integer index:

print(Path.cwd())
print(Path.cwd().parents[0])
print(Path.cwd().parents[1])
# Path.cwd().parents[2]
# Path.cwd().parents[3]
# Path.cwd().parents[4]
# Path.cwd().parents[5]
# Path.cwd().parents[6]

# The older os.path module also has similar functions for getting the different parts of a path
# written in a string value. Calling os.path.dirname(path) will return a string of everything in a string
# value. Calling os.path.dirname(path) will return a string of everything that comes before the last slash in
# the path argument. Calling os.path.basename(path) will return a string of everything that comes after the last slash
# in the path argument. The directory (or dir) name and base name of a path are outlined in Figure 9-5.

# For example,

calcFilePath = "C:\\Windows\\System32\\calc.exe"
print(os.path.basename(calcFilePath))
print(os.path.dirname(calcFilePath))

# If you need a path's dir name and base name together, you can just call os.path.split() to get a tuple value
# with these two strings, like so:

calcFilePath = "C:\\Windows\\System32\\calc.exe"
print(os.path.split(calcFilePath))  # NOTE returns a TUPLE

# Notice that you could create the same tuple by calling os.path.dirname() and
# os.path.basename() and placing their return values in a tuple:

print((os.path.dirname(calcFilePath), os.path.basename(calcFilePath)))

# But os.path.split() is a nice shortcut if you need both values.
# Also, note that os.path.split() does not take a file path and return a list of strings of each folder. For that,
# use the split() method and split on the string in os.sep (Note that sep is in os, not os.path). The os.sep Variable
# is set to the correct folder-separating slash for the computer running the program, '\\' on Windows and '/' on
# macOS and Linux, and splitting on it will return a list of the individual folders.

print(calcFilePath.split(os.sep))  # NOTE: returns a list

# This returns all the parts of the path as strings.
# On macOS and Linux systems, the returned list of folders will begin with a blank string, like this:

"/usr/bin".split(os.sep)

# The split() string method will work to return a list of each part of the path.


# Finding File Sizes and Folder Contents


# Once you have ways of handling file paths, you can then start gathering informationa bout specific files
# and folders. The os.path module provides functions for finding the size of a file in bytes and the files and
# folders inside a given folder.

# - Calling os.path.getsize(path) will return the size in bytes of the file in the path argument
# - Calling os.listdir(path) will return a list of filename strings for each file in the path argument
# (NOTE: that his function is in the os module, not os.path.)

# Here's what I get when I try these functions in the interactive shell:

print(os.path.getsize("C:\\Windows\\System32\\calc.exe"))
print(os.listdir("C:\\Windows\\System32"))

# As you can see, the calc.exe program on my computer is 27,648 bytes in size, and I have a lot of files in
# C:\Windows\system32. If I want to find the total size of all the files in this directory, I can use os.path.getsize()
# and os.listdir() together.

totalSize = 0
for filename in os.listdir("C:\\Windows\\System32"):
    totalSize = totalSize + os.path.getsize(os.path.join("C:\\Windows\\System32", filename))
print(totalSize)

# As I loop over each filename in the C:\Windows\System32 folder, the totalSize variable is incremented by the size
# of each file. Notice how when I call os.path.getsize(), I use os.path.join() to join the folder name with the current
# filename. The integer that os.path.getsize() returns is added to the value of totalSize. After looping through all the files,
# I print totalSize to see the total size of the C:\Windows\System32 folder.


# Modifying a List of Files Using Glob Patterns


# If you want to work on speicific files, glob() is easier to use than listdir().
# Path objects have a glob() method for listing the contents of a folder according to a glob pattern.
# Glob patterns are like a simplified form of regex often used in command line arguments. The glob() method
# returns a generator object (which are beyond the scope of this book) that you'll need to pass to list() to easily
# view in the interactive shell:

p = Path("C:/Users/Al/Desktop")
p.glob("*")
print(list(p.glob("*")))

# NOTE: returns an empty list because no files exist in this path. Additionally there is no path name with those directories.
# Therefore it will not return anything

# The asterisk("*") stands for "multiple of any characters," so p.glob("*") returns a generator of all files in the path
# stored in p.
# Like with regexes, you can create complex expressions:

print(list(p.glob("*.txt")))

# The glob pattern "*.txt" will return files that start with any combination of characters as
# long as it ends with the string ".txt", which is the text file extension.
# In contrast with the asterisk, the question mark(?) stands for any single character:

list(p.glob("project?.docx"))

# The glob expression "project?.docx" will return "project1.docx" or "project5.docx", but it will
# not return "project10.docx", because ? only mathces to one character -- so it will not match to the
# two-character string "10".

# Finally, you can also combine the asterisk and question mark to create even more complex glob expressions, like this:
list(p.globe("*.?x?"))

# The glob expression "*?x?" will return files with any name and any three-character extension where the middle character is
# an "x". By picking out files with specific attributes, the glob() method lets you easily specify the files in a directory
# you want to perform some operation on. You can use a for loop to iterate over the generator that glob() returns:

p = Path("C:/Users/Al/Desktop")
for textFilePathObj in p.globe("*.txt"):
    print(textFilePathObj)  # Prints the Path object as a string.
    # Do something with the text file.

# If you want to perform some operation on every file in a directory, you can use either os.listdir(p) or p.glob("*").


# Checking Path Validity:


# Many Python functions will crash with an error if you supply them with a path that does not exist.
# Luckily, Path objects have methods to check wheter a given path exists and wheter it is a file or folder. Assuming that
# a variable p holds a Path object, you could expect the following:

# - Calling p.exists() returns True if the path exists or returns False if it doesn't exist.
# - Calling p.is_file() returns True if the path exists and is a file, or returns False otherwise.
# - Calling p.is_dir() returns True if the path exists and is a directory, or returns False otherwise.

# On his computer it looks like the following:

winDir = Path("C:/Windows")
notExistsDir = Path("C:/This/Folder/Does/Not/Exist")
calcFile = Path("C:/Windows/System32/calc.exe")
winDir.exists()
winDir.is_dir()
notExistsDir.exists()
calcFile.is_file()
calcFile.is_dir()

# You can determine whether there is a DVD or flash drive currently attached to the computer by checking for it with the
# exists() method. For instance, if I wanted to check for a flash drive with the volume name D:\ on my Windows computer, I
# could do that with the following:

dDrive = Path("D:/")
dDrive.exists()

# Oops! It looks like I forgot to plug in my flash drive.
# The older os.path module can accomplish the same task with the os.path.exists(path),
# os.path.isfile(path), and os.path.isdir(path) functions, which act just like thier Path function counterparts.
# As of Python 3.6, these functions can accept Path objects as well as strings.


# THE FILE READING/WRITING PROCESS:


# Once you are comfortable working with folders and relative paths, you'll be able to specify the location of files to read
# and write. The functions covered in the next few sections will apply to plaintext files. Plaintext files contain only basic
# text characters and do not include font, size, or color information. Text files with the .txt extension or Python script files
# with the .py extension are examples of plaintext files. These can be opened with Window's Notepad or macOS's TextEdit applicaiton.
# Your programs can easliy read the contents of plaintext files and treat them as an ordinary string value.

# Binary files are all other file types, such as word processing documents, PDFs, images, spreadsheets, and executable programs. If you
# open a binary file in Notepad or TextEdit, it will look like scrambled nonsense.

# Since every different type of binary file must be handled in its own way, this book will not go into reading and writing raw binary
# files directly. Fortunately, many modules make working with binary files easier -- you will explore one of them, the shelve module,
# late in this chapter. The pathlib module's read_text() method returns a string of the full contents of a text file. It's write_text()
# method creates a new text file (or overwrites an existing one) with the string passed to it.

''' from pathlib import Path '''
p = Path("spam.txt")
p.write_text("Hello, world!")
p.read_text()

# These method calls create a spam.txt file with the content "Hello, world!". The 13 that write_text() returns indicates that
# 13 characters were written to the file. (You can often disregard this information.) The read_text() call reads and returns the contents
# of our new file as a string: "Hello, world!".

# Keep in mind that these Path object methods only provide basic interactions with the files. The more common way of writing to a file
# involves using the open() function and file objects. These are three steps to reading and writing files in Python.

# 1. Call the open() function to return a File object.
# 2. Call the read() or write() method on the File object.
# 3. Close the file by calling the close() method on the File object.

# We'll go over these steps in the following sections.


# PART 2: OPENING FILES WITH THE OPEN() FUNCTION


# To open a file with the open() function, you pass it a string path indicating the file you want to open; it can be either an absolute
# or relative path. The open() function returns a File object.

# Try it by creating a text file name hello.txt using Notepad or TextEdit. Type Hello, world! as the content of this text file and save it
# in your user home folder. The enter the following into the interative shell.

helloFile = open(Path.home() / "hello.txt")
# NOTE: this creates a file object that can now be used to read or write.
# The open() function can also accept strings. If you're using Windows, enter the following into the interactive shell:

helloFile = open("C:\\Users\\your_home_folder\\hello.txt")

# If you're using macOS, enter the following into the interactive shell instead:

helloFile = open("/Users/your_home_folder/hello.txt")

# Make sure to replace your_home_folder with your computer username. For example, my usersname is AL, so I'd enter
# "C:\\Users\\Al\\hello.txt" on Windows. Note that the open() function only accepts Path objects as of Python 3.6. In previous
# versions, you always need to pass a string to open().

# Both test commands will open the file in "reading plaintext" mode, or read mode for short. When a file is opened in read mode,
# Python lets you only read data from the file; you can't write or modify it in any way. Read mode is the default mode for files you open
# in Python. But if you don't want to rely on Python's defaults, you can explicitly specify the mode passing the string value "r" as a
# second argument to open(). So open("/Users/Al/hello.txt", "r") and open("/Users/Al/hello.txt") do the same thing.

# The call to open() returns a File object. A file object represents a file on your computer; it is simply another type of value in Python,
# much like the lists and dictionaries you're already familiar with. In the previous example, you stored the File object in the variable
# helloFile. Now, whenever you want to read from or write to the file, you can do so by calling methods on the File object in helloFile.


# READING THE CONTENTS OF FILES


# Now that you have a File object, you can start reading from it. If you want to read the entire contents of a file as a string value, use the
# File object's read() method. Let's continue with the hello.txt File object you stored in helloFile. Enter the following into the interactive shell:

helloContent = helloFile.read()
helloContent

# read() returns the string that is stored in the file. You can think of a file's contents as a single large string value.

# You can also use readlines() to get a LIST of string values form the file, one string for each line of text. For example, create a file name
# sonnet29.txt in the same directory as hello.txt and write the following text in it:

''' When, in disgrace with fortune and men's eyes,
 I all alone beweep my outcast state,
 And trouble deaf heaven with my bootless cries,
 And look upon myself and curse my fate, '''

# Make sure to separate the four lines with line breaks. Then enter the following into the interactive shell:

sonnetFile = open(Path.home() / "sonnet29.txt")
sonnetFile.readlines()

# NOTE: that, except for the last line of the file, each of the string values ends with a newline character \n. A list of strings is often
# easier to work with than a single large string value.


#  WRITING TO FILES


# In order to write to a file you must open it in "write plaintext" or "append plaintext" mode (write or append mode).
# NOTE: You can't write to a file that is has been opened in read mode.

# Write mode overwrites the existing file and starts from scratch. Pass "w" as the second argument to open() to
# open the file in write mode.

# Append mode will add text to the end of the existing file.

# If the filename does not exist, write and append mode will create a new, blank file.
# After reading or writing a file, call the close() method before opening the file again.

baconFile = open("bacon.txt", "w")
baconFile.write("Hello, world!\n")
baconFile.close()

baconFile.open("bacon.txt", "a")
baconFile.write("Bacon is not a vegetable.")
baconFile.close()

baconFile = open("bacon.txt")
content = baconFile.read()
baconFile.close()
print(content)

# First, we open bacon.txt in write mode. A new file called bacon.txt is created since there isn't a
# bacon.txt yet.
# Calling write() on the opened file and passing write() the string "Hello, world!\n" writes the string to the
# file and returns the number of characters written, including the newline. Then we close the file.

# Use append mode to add text, instead of overwriting the whole file. So we open the file in append mode,
# write "Bacon is not a vegetable." to the file, and clost it.

# To print the file contents to the screen, open the file in its default read mode, call read(), store
# the resulting File object in content, close the file, and print content.

# NOTE: write() does not add a newline character to the end of a string like print(). You must add it yourself.


# PART 3: SAVING VARIABLES WITH THE SHELVE MODULE


# Saving variables to binary shelf files using the shelve module, allows you to restore data to
# varaiables from the hard drive. The shelve module allows you to use Save and Open features.

shelfFile = shelve.open("mydata")
cats = ["Zophie", "Pooka", "Simon"]

shelfFile["cats"] = cats
shelfFile.close()

# To read and write using the shelve module, you first import shelve. Call shelve.open() and pass it a filename,
# and then store the returned shelf value in a variable.
# NOTE: You can make changes to the shelf value as if it were a dictionary. When you're done,
# call close() on the shelf value. Here, our shelf value is stored in shelfFile. We create a list
# cats and write shelfFile["cats"] = cats to store the list in shelfFile as a value associated with the key "cats"
# Then we call close() on shelfFile. NOTE: Python 3.7+ you can't pass a Path object, the filenames must be strings.

# mydata.bak, mydata.dat, and mydata.dir will be created in the current working directory. These binary files contain the data
# you stored in your shelf. Your programs can use the shelve module to later reopen and retrieve the data from these
# shelf files. Shelf values don't have to be opened in read or write mode -- they can do both once opened.

shelfFile = shelve.open("mydata")
type(shelfFile)
shelfFile["cats"]
shelfFile.close()

# Here, we open the shelf files to check that our data was stored correctly. Entering shelfFile["cats"] returns the same list
# that we stored earlier, so we know that the list is correctly stored, and we call close().

# Just like dictionaries, shelf values have keys() and values() methods that will return list-like values of the keys and values in
# the shelf. Since these methods return list-like values instead of true lists, you should pass them to the list() function to get them in list form.

shelfFile = shelve.open("mydata")
list(shelfFile.keys())
list(shelfFile.values())

# Plaintext is useful for creating files that you'll read in a text editor such as Notepad or TextEdit, but if you want to save
# data from your Phython programs, use the shelve module.


# PART 4: SAVING VARIABLES WITH THE PPRINT.PFORMAAT() FUNCTION


# Recall: pprint.pprint() will "pretty print" the contents of a list or dictionary to the screen, while pprint.pformat() function
# will return this same text as a string instead of printing it. NOTE: This string is syntactically correct Python code.

# Say you have a dictionary stored in a variable and you want to save this variable and its contents for future use.
# Using pprint.pformat() will give you a string that you can write to a .py file.
# This file will be your very own module that you can import whenever you want to use the variable stored in it.

''' import pprint '''
cats = [{"name": "Zophie", "desc": "chubby"}, {"name": "Pooka", "desc": "fluffy"}]
pprint.pformat(cats)
fileObj = open("myCats.py", "w")
fileObj.write("cats = " + pprint.pformat(cats) + "\n")
fileObj.close()

# Here, we import pprint to let us use pprint.pformat(). We have a list of dictionaries, stored in
# a variable cats. To keep the list in cats available even after we close the shell, we use
# pprint.pformat() to return it as a string. Once we have the data in cats as a string, it's easy to
# write the string to a file, which we'll cal myCats.py

# The modules that an import statement imports are themselves just Python scripts.
# When the string pprint.pformat() is saved to a .pyfile, the file is a module that can be imported
# just like any other.

# And since Python scripts are themselves just text files with .py file extension, your Python programs can even
# generate other Python programs.

''' import myCats '''
myCats.cats
myCats.cats[0]
myCats.cats[0]["name"]

# The benefit of creating a .py file (as opposed to saving variables with the shelve module) is that because it is a text file,
# the contents of the file can be read and modified by anyone with a simple text editor. For most applications, however, saving data using
# the shelve module is preferred way to save variables to a file. Only basic data types such as integers, floats, strings, lists, and
# dictionaries can be written to a file as simple text. File objects, for example, cannot be encoded as text.

# NOTE: Look at randomQuizGenerator.py and mcb.pyw for the projects.


# SUMMARY:


# Files are organized into folders (also called directories), a path describes the location of the file.
# Every program running on your computer has a current working directory, this lets you specify file paths
# relative to the current location instead of always typing the absolute path. pathlib and os.path have modules
# for manipulating file paths.

# Programs can also directly interact with contents of text files. The open() function can open these files to read
# in their contents as one large string (with the read() method) or as a list of strings (with the readlines() method).
# The open() function can open files in write or append mode to create new text files or add existing text files, respectively.


# PRACTICE QUESTIONS:

# 1. What is a relative path relative to?
# The current working directory.

# 2. What does an absolute path start with?
# The root folder, / or C:\

# 3. What does Path("C:/Users') / Al' evaluate to on Windows?
# "C:/Users/Al"

# 4. What does 'C:/Users' / 'Al' evaluate to on Windows?
# Error message. None of them are path objects

# 5. What do the os.getcwd() and os.chdir() functions do?
# Get ths current working directory and changes the directory.

# 6. What are the . and .. folders?
# The . the current folder and .. is the parent directory

# 7. In C:\bacon\eggs\spam.txt, which part is the dir name, and which part is the base name?
# dir name is C:\bacon\eggs, base name is spam.txt

# 8. What are the three “mode” arguments that can be passed to the open() function?
# "r" - read mode, "w" - write mode "a" - append mode

# 9. What happens if an existing file is opened in write mode?
# All of its content gets overwritten

# 10. What is the difference between the read() and readlines() methods?
# read returns the entire content as a single string. readlines() returns a list of strings.

# 11. What data structure does a shelf value resemble?
# a shelf value resembles a dictionary value; it has keys and values, along with keys() and values() methods
# that work similarly to the dictionary methods of the same names.
