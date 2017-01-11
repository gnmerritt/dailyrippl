import React, { PropTypes } from 'react';
import { connect } from 'react-redux';
import { Button, Col } from 'react-bootstrap';

import { fetchBills } from './BillActions';
import RipplModal from '../rippl/RipplModal';

export const billShape = PropTypes.shape({
  sunlight_id: PropTypes.string.isRequired,
  official_title: PropTypes.string.isRequired,
});

/**
 * One row in the list of bills
 */
class Bill extends React.Component {
  constructor(props, context) {
    super(props, context);
    this.state = { open: false };
  }

  render() {
    const bill = this.props.bill;
    return (
      <div key={bill.sunlight_id}>
        <Col>{bill.official_title}</Col>
        <Col>
          <Button
            onClick={() => this.setState({ open: true })}
          >
            Rippl!
          </Button>
        </Col>
        <hr />
        <RipplModal
          bill={bill}
          open={this.state.open}
          onClose={() => this.setState({ open: false })}
        />
      </div>
    );
  }
}

Bill.propTypes = {
  bill: billShape.isRequired,
};

/**
 * The list of bills
 */
// eslint-disable-next-line react/no-multi-comp
class Bills extends React.Component {
  componentDidMount() {
    this.props.fetchBills();
  }

  render() {
    const bills = this.props.bills || [];
    return (
      <div>
        {bills.map(b => <Bill bill={b} key={b.id} />)}
      </div>
    );
  }
}

Bills.propTypes = {
  bills: PropTypes.arrayOf(billShape),
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
