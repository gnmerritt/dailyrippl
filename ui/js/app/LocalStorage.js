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
        userCauses: savedState.userCauses,
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
    userCauses: state.userCauses,
  };
  localStorage.setItem(STATE_KEY, JSON.stringify(essentialState));
}, 2 * 1000);

function StateSaverComponent(props) {
  setTimeout(() => saveState(props), 1);
  return props.children;
}

export const StateSaver = connect(
  state => state,
)(StateSaverComponent);
