import React from 'react';
import { Provider } from 'react-redux';
import { render } from 'react-dom';

import createStore from './store';
import { loadState } from './LocalStorage';
import ThreePaneApp from './ThreePaneApp';

render(
  <Provider store={createStore(loadState())} >
    <ThreePaneApp />
  </Provider>,
  document.getElementById('rippl-app'),
);
