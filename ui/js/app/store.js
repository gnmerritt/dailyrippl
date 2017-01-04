import { createStore, applyMiddleware } from 'redux';
import ReduxThunk from 'redux-thunk';

import reducer from './reducers';

export default function buildStore(initialData) {
  return createStore(
    reducer,
    initialData,
    applyMiddleware(ReduxThunk),
  );
}
