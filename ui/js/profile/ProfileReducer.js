export const district = (state = {}, action) => {
  switch (action.type) {
    case 'SET_DISTRICT':
      return action.district;
    default:
      return state;
  }
};

export const representatives = (state = {}, action) => {
  switch (action.type) {
    case 'SET_REPS':
      return action.reps;
    default:
      return state;
  }
};
