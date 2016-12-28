import React, { PropTypes } from 'react';
import { connect } from 'react-redux';
import { Button } from 'react-bootstrap';

import { queryDistrict } from './ProfileActions';

/**
 * Either show the user their congressional district or a button to set it
 */
const CongressionalDistrict = (props) => {
  const d = props.district;
  if (!d.district) {
    const loading = d.loading;
    return (
      <Button
        onClick={loading ? null : props.queryDistrict}
        disabled={loading}
      >
        {loading ? 'Loading...' : 'Find my congressional district'}
      </Button>
    );
  }
  return (
    <div>
      Your congressional district is {d.state_name} {d.district}
    </div>
  );
};

CongressionalDistrict.propTypes = {
  district: PropTypes.shape({
    state: PropTypes.string,
    state_name: PropTypes.string,
    district: PropTypes.number,
    str: PropTypes.string,
  }).isRequired,
  queryDistrict: PropTypes.func.isRequired,
};

const stateToProps = state => ({ district: state.district });
const dispatchToProps = dispatch => ({
  queryDistrict: () => dispatch(queryDistrict()),
});

const ConnectedCD = connect(
  stateToProps,
  dispatchToProps,
)(CongressionalDistrict);

export default ConnectedCD;
