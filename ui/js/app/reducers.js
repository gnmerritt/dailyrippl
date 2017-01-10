import { combineReducers } from 'redux';

import { district, representatives, userCauses } from '../profile/ProfileReducer';
import { causes } from '../causes/CauseReducer';
import { bills } from '../bills/BillsReducer';

const ripplApp = combineReducers({
  bills,
  causes,
  district,
  representatives,
  userCauses,
});

export default ripplApp;
