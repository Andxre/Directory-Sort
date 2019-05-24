import os
import shutil
import datetime


#Constant vars
program = "newSort.py"

def getDirectory():
	currentDir = os.getcwd()
	print("Current Directory: {}".format(currentDir))
	return currentDir
	
def view(currentDir):
	files = os.listdir(currentDir)
	for f in files:
		if (f[0] == '.'):
			files.remove(f)
	for f in files:
		if (f != program):
			time = os.path.getmtime(f)
			time = datetime.datetime.fromtimestamp(time).strftime('%Y-%m-%d')
			print("\033[32m{} \033[33mwas last modified on {}".format(f, time))
	return files

def newDir(files):
	for f in files:
		time = os.path.getmtime(f)
		time = datetime.datetime.fromtimestamp(time).strftime('%Y-%m-%d')	
		if (not os.path.isdir(time)):
			os.makedirs(time)
			print("Folder " + "\033[32m" + str(time) + "\033[0m" + " was created!")

def sort(files, destination):
	for f in files:
		if (f != program):
			time = os.path.getmtime(f)
			time = datetime.datetime.fromtimestamp(time).strftime('%Y-%m-%d')
			folder = str(destination) + '/' + time
			shutil.move(f, folder)

def main():
	print("Directory Sort")
	print("Version 1.0")
	print("By: Andxre")
	currentDir = getDirectory()
	files = view(currentDir)
	newDir(files)
	sort(files, currentDir)

if __name__ == "__main__":
	main()
