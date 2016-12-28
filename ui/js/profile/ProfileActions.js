import $ from 'jquery';
import uri from 'urijs';
import _ from 'underscore';

function setDistrict(district) {
  return { type: 'SET_DISTRICT', district };
}

// Called by the geolocation API once it gets the user's position
function positionHandler(dispatch, geoPosition) {
  const lat = geoPosition.coords.latitude;
  const lng = geoPosition.coords.longitude;
  $.ajax({
    url: uri('/legislature/district').query({ lat, lng }),
    type: 'GET',
    success: district => dispatch(setDistrict(district)),
    error: () => dispatch(setDistrict({})),
  });
}

// eslint-disable-next-line import/prefer-default-export
export const queryDistrict = () =>
  (dispatch) => {
    dispatch(setDistrict({ loading: true }));
    const afterPosition = _.partial(positionHandler, dispatch);
    // TODO: handle errors and stuff?
    navigator.geolocation.getCurrentPosition(afterPosition);
  };
