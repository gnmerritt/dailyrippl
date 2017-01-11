import { combineReducers } from 'redux';

import { district, representatives, userCauses } from '../profile/ProfileReducer';
import { causes, causeSearch } from '../causes/CauseReducer';
import { bills } from '../bills/BillsReducer';

const ripplApp = combineReducers({
  bills,
  causes,
  causeSearch,
  district,
  representatives,
  userCauses,
});

export default ripplApp;
