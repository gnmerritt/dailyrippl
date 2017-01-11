import React, { PropTypes } from 'react';
import { connect } from 'react-redux';

import { fetchCauses } from './CauseActions';
import { chooseCause } from '../profile/ProfileActions';
import { fetchBills } from '../bills/BillActions';

import CauseSearch from './CauseSearch';

const renderCause = (userCauses, chooser) =>
  (cause) => {
    const chosen = userCauses.indexOf(cause.id) > -1;
    const className = chosen ? 'chosen' : '';
    const onClick = () => chooser(cause.id, !chosen);
    return (
      // eslint-disable-next-line jsx-a11y/no-static-element-interactions
      <div key={cause.name} onClick={onClick} className={className}>
        {cause.name}
      </div>
    );
  }
  ;

class Causes extends React.Component {
  componentDidMount() {
    this.props.fetchCauses();
  }

  render() {
    const causes = this.props.causes || [];
    const userCauses = this.props.userCauses || [];
    return (
      <div className="causes">
        <CauseSearch />
        {causes.map(renderCause(userCauses, this.props.chooseCause))}
      </div>
    );
  }
}

Causes.propTypes = {
  causes: PropTypes.arrayOf(PropTypes.shape({
    id: PropTypes.number.isRequired,
    name: PropTypes.string.isRequired,
  })),
  userCauses: PropTypes.arrayOf(PropTypes.number),
  fetchCauses: PropTypes.func.isRequired,
  chooseCause: PropTypes.func.isRequired,
};

const stateToProps = state => ({
  causes: state.causes.results,
  userCauses: state.userCauses,
});
const dispatchToProps = dispatch => ({
  fetchCauses: () => dispatch(fetchCauses()),
  chooseCause: (cause, chosen) => {
    dispatch(chooseCause(cause, chosen));
    dispatch(fetchBills());
  },
});

const ConnectedCauses = connect(
  stateToProps,
  dispatchToProps,
)(Causes);

export default ConnectedCauses;
