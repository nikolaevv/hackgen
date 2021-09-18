configjs = '''import {{createTheme}} from '@material-ui/core/styles';

const theme = createTheme({{
	palette: {{
		type: '{}',
        primary: {{
            main: '{}',
            contrastText: '{}',
        }},
        secondary: {{
            main: '{}',
            contrastText: '{}',
        }}
	}},
}});

export {{theme}};'''

indexhtml = '''<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="initial-scale=1, width=device-width" />
    <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Roboto:300,400,500,700&display=swap" />
    <link rel="icon" href="./favicon.png" />
    <title>{}</title>
  </head>
  <body>
    <div id="root"></div>
  </body>
</html>
'''

component = """import React from 'react';

import './{}.scss';

const {} = () => {{
    return (
        <div></div>
    );
}};

export default {};"""

indexjs = """import {} from './{}';

export default {};"""

pages = """import React from 'react';

import './main-page.scss';

const MainPage = () => {{
    return (
        <div>Hello world!</div>
    );
}};

export default MainPage;"""

pagesindexjs = """import MainPage from './main-page';

export {{MainPage}};"""

app = """import React from 'react';
import {{Route}}from 'react-router';
import {{MainPage}} from '../pages';

import './app.scss';

const App = () => {{
    return (
        <div>
            <Route path="/" exact component={{MainPage}}/>
        </div>
    );
}};

export default App;"""

appindex = """import App from './app';

export default App;"""