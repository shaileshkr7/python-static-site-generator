from typing import List
from pathlib import Path
import shutil

class Parser:
    extensions = []
    extensions: List[str]
def valid_exttension(extension):
    if extension in self.extensions:
        return true
    else:
        return false
def parse(path,source,dest):
    path: List[Path]
    source: List[Path]
    dest: List[Path]
    raise NotImplementedError
def read(path):
    with open(path, 'r') as file:
        return file
def write(path,dest,content,ext=".html"):
    full_path=self.dest/with_suffix.name
    with open(full_path, 'w') as file:
        file.write(content)
        file.close()
def copy(path,source,dest):
    copy2(path,dest/source)

class ResourceParser(Parser):
    extensions = [".jpg",".png",".gif",".css",".html"]
    def parse(path,source,dest):
        copy(path,source,dest)
