import { combineReducers } from 'redux';

import { district, representatives } from '../profile/ProfileReducer';

const ripplApp = combineReducers({
  district,
  representatives,
});

export default ripplApp;
