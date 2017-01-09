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

export const userCauses = (state = [], action) => {
  switch (action.type) {
    case 'CHOOSE_CAUSE':
      if (action.chosen) {
        return state.concat(action.causeId);
      }
      return state.filter(c => c !== action.causeId);
    default:
      return state;
  }
};
