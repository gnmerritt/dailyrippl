import React, { PropTypes } from 'react';
import { connect } from 'react-redux';

import { fetchBills } from './BillActions';

const renderBill = bill =>
  <div key={bill.sunlight_id}>
    {bill.official_title}
    <hr />
  </div>
  ;

class Bills extends React.Component {
  componentDidMount() {
    this.props.fetchBills();
  }

  render() {
    const bills = this.props.bills || [];
    return (
      <div>
        {bills.map(renderBill)}
      </div>
    );
  }
}

Bills.propTypes = {
  bills: PropTypes.arrayOf(PropTypes.shape({
    sunlight_id: PropTypes.string.isRequired,
    official_title: PropTypes.string.isRequired,
  })),
  fetchBills: PropTypes.func.isRequired,
};

const stateToProps = state => ({
  bills: state.bills.results,
});
const dispatchToProps = dispatch => ({
  fetchBills: causes => dispatch(fetchBills(causes)),
});

const ConnectedBills = connect(
  stateToProps,
  dispatchToProps,
)(Bills);

export default ConnectedBills;
