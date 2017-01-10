// eslint-disable-next-line import/prefer-default-export
export const bills = (state = {}, action) => {
  switch (action.type) {
    case 'SET_BILLS':
      return action.bills;
    default:
      return state;
  }
};
