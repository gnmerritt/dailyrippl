import { connect } from 'react-redux';
import _ from 'underscore';

const STATE_KEY = 'rippl_v1';

/**
 * Load saved state from local storage
 */
export function loadState() {
  try {
    const savedState = JSON.parse(localStorage.getItem(STATE_KEY));
    if (savedState) {
      return {
        district: { id: savedState.district },
      };
    }
  } catch (e) {} // eslint-disable-line no-empty

  return {};
}

/**
 * Save essential pieces of the current state to local storage
 */
const saveState = _.debounce((state) => {
  const essentialState = {
    district: state.district.id,
  };
  localStorage.setItem(STATE_KEY, JSON.stringify(essentialState));
}, 5 * 1000, true);

function StateSaverComponent(props) {
  setTimeout(() => saveState(props), 1);
  return props.children;
}

export const StateSaver = connect(
  state => state,
)(StateSaverComponent);
