import os
import sys
import shutil


class SmartTool:
    def makeDir(dirName):
        print(os.name, sys.platform)
        if sys.platform == 'darwin':
            desktop_path = os.path.expanduser('~/Desktop')
            folder_path = os.path.join(desktop_path, dirName)
            if os.path.exists(folder_path):
                shutil.rmtree(folder_path)
            os.mkdir(folder_path)
            return folder_path
        return ''

    def system(self):
        return sys.platform
