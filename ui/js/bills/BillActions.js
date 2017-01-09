import $ from 'jquery';
import uri from 'urijs';

function setBills(bills) {
  return { type: 'SET_BILLS', bills };
}

// eslint-disable-next-line import/prefer-default-export
export const fetchBills = (topics = []) =>
  (dispatch) => {
    dispatch(setBills({ loading: true }));
    $.ajax({
      url: uri('laws/bills.json').search({ t: topics }),
      type: 'GET',
      success: bills => dispatch(setBills(bills)),
      error: () => dispatch(setBills({})),
    });
  };
