import zipfile
import pathlib
def make_archive(filesPaths,destFolder,zipFileName):
    dest_path = pathlib.Path(destFolder,f'{zipFileName}.zip')
    with zipfile.ZipFile(dest_path,'w') as archive:
        for filePath in filesPaths:
            filePath = pathlib.Path(filePath)
            archive.write(filePath, arcname=filePath.name)

# following lines are for testing purpose only. Will execute when we run "THIS" file only
if __name__ == '__main__':
    make_archive(filesPaths=['testSpace/test1.txt','testSpace/test2.txt'], destFolder="testSpace")

