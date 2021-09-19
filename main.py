from distutils.dir_util import copy_tree
import formatted
import os, shutil

schemas_types = {'Integer': 'int', 'DateTime': 'datetime', 'Text': 'str', 'Date': 'date', 'Float': 'floar', 'Boolean': 'bool'}

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

def kebab_case_to_upper(text):
    words = text.split('-')
    result_text = ''

    for word in words:
        result_text += word.capitalize()
    return result_text

class FrontendApp:
    dependencies = [
        'react', 'react-dom', 'react-redux', 'react-router-dom', 'react-scripts',
        'redux-query', 'redux-query-interface-superagent', 'redux-query-react',
        '@material-ui/core', '@material-ui/icons', '@material-ui/core@next',
        '@testing-library/jest-dom', '@testing-library/react', '@testing-library/user-event',
        'web-vitals', '@mui/material', 'node-sass', 'sass', '@emotion/react', '@emotion/styled'
    ]

    title = 'App'
    theme = 'light'
    color = '#000'
    contrast_color = '#FFF'
    secondary_color = '#000'
    secondary_contrast_color = '#FFF'
    components = ['app']
    pages = []
    models = []
    folder_name = 'frontend' 

    def __init__(self, title: str, theme: str, color: str, secondary_color: str, secondary_contrast_color: str, contrast_color: str, components: list, pages: list, models: list):
        self.title = title
        self.theme = theme
        self.color = color
        self.contrast_color = contrast_color
        self.secondary_color = secondary_color
        self.secondary_contrast_color = secondary_contrast_color
        self.components += components
        self.pages = pages
        self.models = models

    def generate_file(self, path, template, *variables):
        with open('./result/{}/{}'.format(self.folder_name, path), 'w') as file:
            print(variables)
            text = template.format(*variables)
            print(text)
            file.write(text)

    def init(self):
        clear_dir('./result/{}'.format(self.folder_name))
        copy_tree('./frontend-template', './result/{}'.format(self.folder_name))

    def install_dependencies(self):
        dependencies = ' '.join(self.dependencies)
        os.system('cd ./result/{}; npm install {} --force'.format(self.folder_name, dependencies))

    def create_components_folders(self):
        for el in self.components:
            file_path = './result/{}/src/components/{}'.format(self.folder_name, el)
            os.system('mkdir {}'.format(file_path))

    def create_components_files(self):
        for el in self.components:
            component_name = kebab_case_to_upper(el)
            file_path = 'src/components/{}/{}.js'.format(el, el)

            self.generate_file(
                file_path, 
                formatted.component, 
                el, component_name, component_name
            )

            file_path = 'src/components/{}/{}.scss'.format(el, el)

            self.generate_file(
                file_path,
                ''
            )

            file_path = 'src/components/{}/index.js'.format(el)

            self.generate_file(
                file_path, 
                formatted.indexjs, 
                component_name, el, component_name
            )
    
    def create_pages(self):
        file_path = './result/{}/src/components/pages'.format(self.folder_name)
        os.system('mkdir {}'.format(file_path))

        file_path = 'src/components/pages/main-page.js'

        self.generate_file(
            file_path, 
            formatted.pages, 
        )

        file_path = 'src/components/pages/main-page.scss'

        self.generate_file(
            file_path,
            ''
        )

        file_path = 'src/components/pages/index.js'

        self.generate_file(
            file_path, 
            formatted.pagesindexjs, 
        )

    def create_app(self):
        file_path = './result/{}/src/components/app'.format(self.folder_name)
        os.system('mkdir {}'.format(file_path))

        file_path = 'src/components/app/app.js'

        self.generate_file(
            file_path, 
            formatted.app, 
        )

        file_path = 'src/components/app/app.scss'

        self.generate_file(
            file_path,
            ''
        )

        file_path = 'src/components/app/index.js'

        self.generate_file(
            file_path, 
            formatted.appindex, 
        )

    def generate_app(self):
        self.init()

        self.generate_file(
            'src/config.js', 
            formatted.configjs,
            self.theme, self.color, self.contrast_color, self.secondary_color, self.secondary_contrast_color
        )
        
        self.generate_file(
            'public/index.html',
            formatted.indexhtml,
            self.title
        )

        self.install_dependencies()

        self.create_components_folders()
        self.create_components_files()
        self.create_pages()
        self.create_app()

class BackendApp:
    models = []
    folder_name = 'backend' 
    
    def __init__(self, models):
        self.models = models

    def init(self):
        clear_dir('./result/{}'.format(self.folder_name))
        copy_tree('./backend-template', './result/{}'.format(self.folder_name))

    def create_enum(self, name, choices):
        self.add_to_file('app/choices.py', 'class {}(enum.Enum):\n'.format(name.capitalize()))
        for choice in choices:
            self.add_to_file('app/choices.py', '    {} = "{}"\n'.format(choice.upper(), choice.upper()))

    def add_to_file(self, path: str, text: str):
        with open('./result/{}/{}'.format(self.folder_name, path), 'a') as file:
            file.write(text)

    def read_file(self, path: str) -> str:
        with open('./result/{}/{}'.format(self.folder_name, path), 'r') as file:
            return file.read()

    def insert_to_file(self, path: str, text: str):
        prev_text = self.read_file(path)
        recent_text = text + prev_text

        with open('./result/{}/{}'.format(self.folder_name, path), 'w') as file:
            file.write(text)

    def create_models(self):
        for model in self.models:
            self.add_to_file('app/models.py', text = formatted.model.format(model['title'], model['title'].lower() + 's'))

            for rel in model["relations"]:
                self.add_to_file('app/models.py', '    {}s = relationship({})\n'.format(rel.lower(), rel))

            for column in model["columns"]:
                if column['type'] in ('Integer', 'DateTime', 'Text', 'Date', 'Float', 'Boolean'):
                    self.add_to_file('app/models.py', '    {} = Column({}'.format(column['name'], column['type']))
                elif column['type'] == 'enum':
                    self.create_enum(column['name'], column['choices'])
                    self.add_to_file('app/models.py', "    {} = Column(Enum({})".format(column['name'], column['name'].capitalize()))
                elif column['type'] == 'relation':
                    self.add_to_file('app/models.py', "    {}_id = Column(Integer, ForeignKey('{}.id')".format(column['name'], column['name']))

                if column.get('default') != None:
                    self.add_to_file('app/models.py', ',default={}'.format(column['default']))
                if column.get('nullable') != None:
                    self.add_to_file('app/models.py', ',nullable={}'.format(column['nullable']))

                self.add_to_file('app/models.py', ')\n')

    def create_schemas(self):
        for model in self.models:
            self.add_to_file('app/schemas.py', 'class {}(BaseModel):\n'.format(model['title']))
            for column in model["columns"]:
                if column['type'] in ('Integer', 'DateTime', 'Text', 'Date', 'Float', 'Boolean'):
                    self.add_to_file('app/schemas.py', '    {}: {}\n'.format(column['name'], schemas_types[column['type']]))
                elif column['type'] == 'enum':
                    self.add_to_file('app/schemas.py', '    {}: {}\n'.format(column['name'], column['name'].capitalize()))
                elif column['type'] == 'relation':
                    self.add_to_file('app/schemas.py', "    {}_id: int\n".format(column['name']))

            self.add_to_file('app/schemas.py', '\n    class Config:\n        orm_mode = True\n\n')

    def create_CRUD(self):
        for model in self.models:
            lowed_model_title = model['title'].lower()
            self.add_to_file('app/crud.py', formatted.read_all.format(lowed_model_title, model['title'].capitalize()))
            self.add_to_file('app/crud.py', formatted.read_by_id.format(lowed_model_title, lowed_model_title, model['title'].capitalize(), model['title'].capitalize(), lowed_model_title, lowed_model_title))
            
            columns = [c['name'] for c in model["columns"] if c.get('default') == None and c.get('nullable') == None]
            specified_columns = [c['name'] + '=' + c['name'] for c in model["columns"] if c.get('default') == None and c.get('nullable') == None]
            self.add_to_file('app/crud.py', formatted.create.format(lowed_model_title, ', '.join(columns), model['title'].capitalize(), ', '.join(specified_columns)))
    
    def create_API(self):
        for model in self.models:
            lowed_model_title = model['title'].lower()

            self.add_to_file('main.py', formatted.method.format(
                'get', 
                '{}s'.format(lowed_model_title), 
                'List[schemas.{}]'.format(model['title']),
                'get_{}s'.format(lowed_model_title),
                'get_{}s'.format(lowed_model_title)
            ))

            self.add_to_file('main.py', formatted.method_with_id.format(
                'get', 
                '{}s'.format(lowed_model_title),
                '{id}',
                'schemas.{}'.format(model['title']),
                'get_{}'.format(lowed_model_title),
                'id',
                'get_{}_by_id'.format(lowed_model_title),
                'id'
            ))

            self.add_to_file('main.py', formatted.method.format(
                'post', 
                '{}'.format(lowed_model_title), 
                'None',
                'create_{}'.format(lowed_model_title),
                'create_{}'.format(lowed_model_title)
            ))

            

    def build_requirements(self):
        os.system('cd ./result/{}; pipreqs ./'.format(self.folder_name))

    def create_database(self):
        pass

    def generate_app(self):
        self.init()
        self.create_models()
        self.create_schemas()
        self.create_CRUD()
        self.create_API()
        self.build_requirements()

if __name__ == '__main__':
    #frontendApp = FrontendApp('Some App', 'light', '#2c3e50', '#FFF', '#bdc3c7', '#2c3e50', [], [], [])
    #frontendApp.generate_app()

    models = [{"title": "User", "columns": [
        {"type": "Integer", "name": "age", "default": 1, "nullable": True}, 
        {"type": "Text", "name": "name"},
        {"type": "enum", "name": "role", "choices": ['AIRPORT', 'BUSINESS']},
        {"type": "relation", "name": "cart", "nullable": True},
        ], "relations": ['Message']}]
    backendApp = BackendApp(models)
    backendApp.generate_app()

#clear_dir('./result/backend')
#copy_tree("./backend-template", "./result/backend")