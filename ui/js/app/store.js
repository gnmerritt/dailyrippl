import { createStore, applyMiddleware } from 'redux';
import ReduxThunk from 'redux-thunk';

import reducer from './reducers';

export default createStore(
  reducer,
  applyMiddleware(ReduxThunk),
);
