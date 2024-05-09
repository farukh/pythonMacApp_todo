import FreeSimpleGUI as Sg
lblSelectFiles = Sg.Text("Select Files to Compress: ")
filesSelector = Sg.InputText()
btnFileChooser = Sg.FileBrowse()

lblSelectDestinationFolder = Sg.Text("Select Destination Folder: ")
destFolderInput = Sg.Input()
btnDestFolderSelector = Sg.FolderBrowse()

btnCompressNow = Sg.Button("Compress")
window = Sg.Window("Supper File Compression ", layout=[[lblSelectFiles,filesSelector,btnFileChooser],
                                             [lblSelectDestinationFolder,destFolderInput,btnDestFolderSelector],
                                             [btnCompressNow]])
window.read()

window.Close()

