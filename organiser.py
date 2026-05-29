import os
import shutil
from pathlib import Path
file_types={"docs":['.docx','.xlsx','.txt','.pptx','.doc','.pdf','.csv'],
            "images":['.jpg','.jpeg','.png','.gif','.webp','.avif','.svg','.tiff','.tif'],
            "videos":['.mp4','.mov','.mkv','.avi','webm','.m4v'],
            "audios":['.mp3','.m4a','.aac','.ogg','.wav','.aiff','.aif','.flac','.alac'],
            "code":['.py','.js','.cpp','.cc','.java','.c'],
            "others":[]}
def get_category(extension):
    for category,type in file_types.items():
        if extension in type:
            return category
    return "others"


def organise_folder(folder):
    folder_path=Path(folder)
    skipped,moved=0,0
    if folder_path.exists()==False:
        print(f"Folder not found on {folder}")
        return
    for file in folder_path.iterdir():
        if file.is_dir() or file.name.startswith('.'):
            skipped=skipped+1
        else:
            category=get_category(file.suffix)
            new_path=folder_path/category
            new_path.mkdir(exist_ok=True)
            shutil.move(str(file),str(new_path))
            moved=moved+1
            print(f"moved {file.suffix} to /{category} folder")
    print(f"{moved} files moved  and {skipped} files skipped")

if __name__=="__main__":
    target_folder=input("Enter the path of folder which you want to organise: ")
    organise_folder(target_folder)