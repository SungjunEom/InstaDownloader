from cx_Freeze import setup, Executable

base = None    

executables = [Executable("InstaDownloader.py", base=base)]

packages = ["idna", "os", "time", "urllib.request","selenium"]
options = {
    'build_exe': {    
        'packages':packages,
    },    
}

setup(
    name = "downloader",
    options = options,
    version = "0.0.0.0",
    description = '',
    executables = executables
)