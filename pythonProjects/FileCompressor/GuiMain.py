import FreeSimpleGUI as Sg
from zip_creator import make_archive
lblSelectFiles = Sg.Text("Select Files to Compress: ")
filesSelector = Sg.InputText(key="FilesPath")
btnFileChooser = Sg.FilesBrowse()

lblSelectDestinationFolder = Sg.Text("Select Destination Folder: ")
destFolderInput = Sg.Input(key='DestFolder')
btnDestFolderSelector = Sg.FolderBrowse()

lblOutput = Sg.Text(key="lblOutput", text_color='Blue')
btnCompressNow = Sg.Button("Compress")
window = Sg.Window("Supper File Compression ", layout=[[lblSelectFiles,filesSelector,btnFileChooser],
                                             [lblSelectDestinationFolder,destFolderInput,btnDestFolderSelector],
                                             [btnCompressNow,lblOutput]], font=('Arial',20))
while True:
    event, values = window.read()
    filePath = values['FilesPath'].split(';')
    destFolder = values['DestFolder']
    print(filePath)
    print(destFolder)
    make_archive(filesPaths=filePath,destFolder=destFolder,zipFileName="compressedNew")
    window['lblOutput'].update("Compression Completed.")

window.Close()

