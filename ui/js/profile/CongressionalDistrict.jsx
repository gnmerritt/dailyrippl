import React, { PropTypes } from 'react';
import { connect } from 'react-redux';
import { Button } from 'react-bootstrap';

import { queryDistrict } from './ProfileActions';

/**
 * Either show the user their congressional district or a button to set it
 */
const CongressionalDistrict = (props) => {
  const d = props.district;
  if (!d.id) {
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
      Your congressional district is {d.state.name} {d.number}
    </div>
  );
};

CongressionalDistrict.propTypes = {
  district: PropTypes.shape({
    state: PropTypes.shape({
      name: PropTypes.string.isRequired,
      abbr: PropTypes.string.isRequired,
    }),
    id: PropTypes.number,
    number: PropTypes.number,
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
