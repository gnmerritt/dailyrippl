import $ from 'jquery';
import uri from 'urijs';

function setCauses(causes) {
  return { type: 'SET_CAUSES', causes };
}

export const fetchCauses = () =>
  (dispatch, getState) => {
    dispatch(setCauses({ loading: true }));
    const state = getState();
    const searchString = state.causeSearch;
    $.ajax({
      url: uri('rippl/topics.json').search({ q: searchString }),
      type: 'GET',
      success: causes => dispatch(setCauses(causes)),
      error: () => dispatch(setCauses({})),
    });
  };

export const setSearch = search =>
  (dispatch, getState) => {
    dispatch({ type: 'SET_CAUSE_SEARCH', search });
    // TODO: debounce this so it doesn't murder the server
    fetchCauses()(dispatch, getState);
  };
