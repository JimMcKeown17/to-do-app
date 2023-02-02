import zipfile
import pathlib

a = pathlib.Path("dest", "compressed.zip")

def make_archive(filepaths, dest_dir):
    with zipfile.ZipFile(a, "w") as archive:
        for filepath in filepaths:
            archive.write(filepath)

if __name__ == "__main__":
    make_archive(filepaths=["ideas.txt", "projects.txt"], dest_dir="dest")
