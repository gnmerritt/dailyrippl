export const causes = (state = {}, action) => {
  switch (action.type) {
    case 'SET_CAUSES':
      return action.causes;
    default:
      return state;
  }
};

export const causeSearch = (state = '', action) => {
  switch (action.type) {
    case 'SET_CAUSE_SEARCH':
      return action.search;
    default:
      return state;
  }
};
