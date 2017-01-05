import $ from 'jquery';
import uri from 'urijs';

function setCauses(causes) {
  return { type: 'SET_CAUSES', causes };
}

// eslint-disable-next-line import/prefer-default-export
export const fetchCauses = () =>
  (dispatch) => {
    dispatch(setCauses({ loading: true }));
    $.ajax({
      url: uri('rippl/topics.json'),
      type: 'GET',
      success: causes => dispatch(setCauses(causes)),
      error: () => dispatch(setCauses({})),
    });
  };
