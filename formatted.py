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