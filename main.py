from distutils.dir_util import copy_tree
import formatted
import os, shutil

def clear_dir(path):
    for filename in os.listdir(path):
        file_path = os.path.join(path, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print('Failed to delete {}. Reason: {}'.format(file_path, e))

class FrontendApp:
    theme = 'light'
    color = '#000'
    contrast_color = '#FFF'
    secondary_color = '#000'
    secondary_contrast_color = '#FFF'
    components = []
    pages = []
    models = []
    folder_name = 'frontend' 

    def __init__(self, theme: str, color: str, secondary_color: str, secondary_contrast_color: str, contrast_color: str, components: list, pages: list, models: list):
        self.theme = theme
        self.color = color
        self.contrast_color = contrast_color
        self.secondary_color = secondary_color
        self.secondary_contrast_color = secondary_contrast_color
        self.components = components
        self.pages = pages
        self.models = models

    #def generate_file(*variables):


    def init(self):
        clear_dir('./result/{}'.format(self.folder_name))
        copy_tree('./frontend-template', './result/{}'.format(self.folder_name))

    def generate(self):
        self.init()

        with open('./result/{}/src/config.js'.format(self.folder_name), 'w') as file:
            print(self.theme, self.color, self.contrast_color, self.secondary_color, self.secondary_contrast_color)
            text = formatted.configjs.format(self.theme, self.color, self.contrast_color, self.secondary_color, self.secondary_contrast_color)
            file.write(text)
        
frontendApp = FrontendApp('light', '#2c3e50', '#FFF', '#bdc3c7', '#2c3e50', [], [], [])
frontendApp.generate()

#clear_dir('./result/backend')
#copy_tree("./backend-template", "./result/backend")