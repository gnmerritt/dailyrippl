import { combineReducers } from 'redux';

import { district } from '../profile/ProfileReducer';

const ripplApp = combineReducers({
  district,
});

export default ripplApp;
