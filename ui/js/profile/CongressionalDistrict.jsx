import React, { PropTypes } from 'react';
import { connect } from 'react-redux';
import { Button } from 'react-bootstrap';

import { queryDistrict, fetchDistrict } from './ProfileActions';

/**
 * Either show the user their congressional district or a button to set it
 */
class CongressionalDistrict extends React.Component {
  componentDidMount() {
    const d = this.props.district;
    // fetch our district information using the saved district id
    if (d.id && !d.state) {
      this.props.fetchDistrict(d.id);
    }
  }

  render() {
    const d = this.props.district;
    if (!d.state) {
      const loading = d.loading;
      return (
        <Button
          onClick={loading ? null : this.props.queryDistrict}
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
  }
}

CongressionalDistrict.propTypes = {
  district: PropTypes.shape({
    state: PropTypes.shape({
      name: PropTypes.string.isRequired,
      abbr: PropTypes.string.isRequired,
    }),
    id: PropTypes.number,
    number: PropTypes.number,
  }).isRequired,
  fetchDistrict: PropTypes.func.isRequired,
  queryDistrict: PropTypes.func.isRequired,
};

const stateToProps = state => ({ district: state.district });
const dispatchToProps = dispatch => ({
  fetchDistrict: id => dispatch(fetchDistrict(id)),
  queryDistrict: () => dispatch(queryDistrict()),
});

const ConnectedCD = connect(
  stateToProps,
  dispatchToProps,
)(CongressionalDistrict);

export default ConnectedCD;
