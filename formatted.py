configjs = '''
import {{createTheme}} from '@material-ui/core/styles';

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