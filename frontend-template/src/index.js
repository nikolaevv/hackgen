import React from 'react';
import ReactDOM from 'react-dom';
import { Provider } from 'react-redux';
import {theme} from './config';
import { Provider as ReduxQueryProvider } from 'redux-query-react';
import store, {getQueries} from './store';
import App from './components/app';
import {ThemeProvider} from '@material-ui/core';
import {BrowserRouter as Router, Switch} from 'react-router-dom';

ReactDOM.render(
    <React.StrictMode>
        <Provider store={store}>
            <ReduxQueryProvider queriesSelector={getQueries}>
                <ThemeProvider theme={theme}>
                    <Router>
                        <Switch>
                            <App/>
                        </Switch>
                    </Router>
                </ThemeProvider>
            </ReduxQueryProvider>
        </Provider>
    </React.StrictMode>,
  document.getElementById('root')
);