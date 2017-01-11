import React, { PropTypes } from 'react';
import { connect } from 'react-redux';
import { FormControl } from 'react-bootstrap';

import { setSearch } from './CauseActions';

const CauseSearch = props =>
  <FormControl
    type="text"
    value={props.searchString}
    placeholder="Search causes"
    onChange={props.setSearch}
  />
  ;

CauseSearch.propTypes = {
  searchString: PropTypes.string.isRequired,
  setSearch: PropTypes.func.isRequired,
};

const ConnectedCauseSearch = connect(
  state => ({ searchString: state.causeSearch }),
  dispatch => ({ setSearch: e => dispatch(setSearch(e.target.value)) }),
)(CauseSearch);

export default ConnectedCauseSearch;
