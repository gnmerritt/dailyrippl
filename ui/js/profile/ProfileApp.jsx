import React from 'react';
import { Provider } from 'react-redux';
import { render } from 'react-dom';

import store from '../app/store';

import CongressionalDistrict from './CongressionalDistrict';

function ProfileApp() {
  return (
    <div>
      <CongressionalDistrict />
    </div>
  );
}

// TODO: abstract this store nonsense out somewhere
render(
  <Provider store={store} >
    <ProfileApp />
  </Provider>,
  document.getElementById('profile-app'),
);
