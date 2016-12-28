// eslint-disable-next-line import/prefer-default-export
export const district = (state = {}, action) => {
  switch (action.type) {
    case 'SET_DISTRICT':
      return action.district;
    default:
      return state;
  }
};
