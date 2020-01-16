import os

def run(**args):
    print "[*!] In dir lister module."
    files = os.listdir(".")
    return str(files)
