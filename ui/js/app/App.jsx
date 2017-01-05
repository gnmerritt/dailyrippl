import React from 'react';
import { Provider } from 'react-redux';
import { render } from 'react-dom';

import createStore from './store';
import { loadState, StateSaver } from './LocalStorage';
import ThreePaneApp from './ThreePaneApp';

render(
  <Provider store={createStore(loadState())} >
    <StateSaver>
      <ThreePaneApp />
    </StateSaver>
  </Provider>,
  document.getElementById('rippl-app'),
);
