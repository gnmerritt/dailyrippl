// eslint-disable-next-line import/prefer-default-export
export const causes = (state = {}, action) => {
  switch (action.type) {
    case 'SET_CAUSES':
      return action.causes;
    default:
      return state;
  }
};
