import { combineReducers } from 'redux';

import { district, representatives } from '../profile/ProfileReducer';
import { causes } from '../causes/CauseReducer';

const ripplApp = combineReducers({
  causes,
  district,
  representatives,
});

export default ripplApp;
