import sys
import os
import shutil
import argparse
import json

def Main(pluginName:str,):
    print(f"{pluginName}")

    CopyTemplate()
    SetupTemplate(pluginName)
    UpdateFiles(pluginName)

def CopyTemplate():
    path = os.getcwd()
    templatePath = path + "\\Template"

    print(templatePath, path)
    shutil.copytree(templatePath, path, dirs_exist_ok=True)

def SetupTemplate(pluginName: str):
    directory = os.getcwd()
    templatePath = directory + "\\Template"
    isRename = False

    for subdir, dirs, files in os.walk(directory):
        if subdir.startswith(templatePath):
            continue

        for filename in files:
            if RenameFile(pluginName, filename, subdir, directory):
                isRename = True

        for dir in dirs:
            if RenameFile(pluginName, dir, subdir, directory):
                isRename = True
    if isRename:
        return SetupTemplate(pluginName)
    return

def RenameFile(pluginName, filename, subdir, directory):
    if filename.find('Your_Plugin_Name') >= 0:
        newFilename = filename.replace("Your_Plugin_Name", pluginName) # replace only in filename
        subDirectoryPath = os.path.relpath(subdir, directory) # path to subdirectory
        filePath = os.path.join(subDirectoryPath, filename) # path to file
        newSubDirectoryPath = subDirectoryPath.replace("Your_Plugin_Name", pluginName)
        newFilePath = os.path.join(newSubDirectoryPath, newFilename) # new path
        os.rename(filePath, newFilePath) # rename

        return True
    
    return False

def UpdateFiles(pluginName):
    path = os.getcwd()
    templatePath = path + "\\Template"
    enginePath = path + "\\EngineContent"

    envJson = open('env.json')
    envData = json.load(envJson)

    for subdir, dirs, files in os.walk(path):
        if subdir.startswith(templatePath) or subdir.startswith(enginePath):
            continue
        for file in files:
            if file == os.path.basename(sys.argv[0]) or file == "env.json" or file.find("InitEnv") >= 0 or file == "readme.md":
                continue
            filePath = subdir + f"\\{file}"
            print(filePath)
            with open(filePath, "r+") as filehandle:
                content = filehandle.read()
                content = content.replace("Your_Plugin_Name", pluginName)
                content = content.replace("Your_PressureCooker_Path", f"{path}")
                content = content.replace("Your_Editor_Path", envData["EditorDir"])
                content = content.replace("Your_Game_Path", envData["GameDir"])
                filehandle.seek(0)
                filehandle.write(content)
                filehandle.truncate()

def CleanupEnvironment():
    path = os.getcwd()

    dirList = os.listdir()
    for dir in dirList:
        if dir == "Template" or dir == "EngineContent" or dir.find("InitEnv") >= 0 or dir == "env.json" or dir == "readme.md":
            continue
        file = path + f"\\{dir}"
        if (os.path.isfile(file)):
            os.remove(file)
        else:
            shutil.rmtree(file)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
                    prog='InitEnvironment',
                    description='Prepares the environment for cooking TSW4 pak files',
                    epilog='developed by Nony')
 
    parser.add_argument("-p", "--Plugin", help = "The Plugin Name")
    parser.add_argument("-c", "--Cleanup", help = "Cleans Up the directory", action='store_true')
    
    args = parser.parse_args()
    
    if args.Cleanup:
        CleanupEnvironment()

    if args.Plugin:
        pluginName = args.Plugin
        Main(pluginName)
    elif args.Cleanup:
        print("Cleanup Successful")
    else:
        print("""Arguments missing Plugin/GameDir.
              Run the script with the following arguements -p <PluginName>
              ex: py InitEnvironment.py -p <PluginName>
              Run -h to get more info""")