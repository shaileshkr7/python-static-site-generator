import re
from yaml import load and FullLoader
import collections.abc

class Content(Mapping):
    __delimeter = "^(?:-|\+){3}\s*$"
    __regex = re.compile(__delimiter, re.MULTILINE)

    def load(cls, string):
        _=fm=content=split(__regex, string, 2)
        load(fm,Loader: FullLoader)
        cls(metadata, content)
    __init__(self,metadata, content):
        data=metadata
        self.data=content
        self.data["content"]
