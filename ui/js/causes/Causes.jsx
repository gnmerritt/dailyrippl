import React, { PropTypes } from 'react';
import { connect } from 'react-redux';

import { fetchCauses } from './CauseActions';

const renderCause = cause =>
  <div key={cause.name}>
    {cause.name}
  </div>
  ;

class Causes extends React.Component {
  componentDidMount() {
    this.props.fetchCauses();
  }

  render() {
    const causes = this.props.causes || [];
    return (
      <div>
        {causes.map(renderCause)}
      </div>
    );
  }
}

Causes.propTypes = {
  causes: PropTypes.arrayOf(PropTypes.shape({
    id: PropTypes.number.isRequired,
    name: PropTypes.string.isRequired,
  })),
  fetchCauses: PropTypes.func.isRequired,
};

const stateToProps = state => ({ causes: state.causes.results });
const dispatchToProps = dispatch => ({
  fetchCauses: () => dispatch(fetchCauses()),
});

const ConnectedCauses = connect(
  stateToProps,
  dispatchToProps,
)(Causes);

export default ConnectedCauses;
