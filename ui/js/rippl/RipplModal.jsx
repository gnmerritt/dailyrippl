import React, { PropTypes } from 'react';
import { connect } from 'react-redux';
import { Modal } from 'react-bootstrap';

import Representatives from '../profile/Representatives';

/**
 * A modal window where we guide the user through making several calls to his/her
 * elected representatives to talk about a specific bill.
 */
const RipplModal = (props) => {
  const close = props.onClose;
  const bill = props.bill;
  return (
    <Modal bsSize="large" show={props.open} onHide={close}>
      <Modal.Header closeButton>
        <Modal.Title>{bill.sunlight_id} - {bill.official_title}</Modal.Title>
      </Modal.Header>
      <Modal.Body>
        <h3>Contact your reps</h3>
        <Representatives />
        <h3>For more info</h3>
        <a href={bill.url}>See the house floor listing</a>
      </Modal.Body>
    </Modal>
  );
};

RipplModal.propTypes = {
  bill: PropTypes.shape({
    official_title: PropTypes.string.isRequired,
    url: PropTypes.string.isRequired,
  }).isRequired,
  onClose: PropTypes.func.isRequired,
  open: PropTypes.bool.isRequired,
};

const stateToProps = state => ({
  senate: state.representatives.SEN,
  house: state.representatives.HOR,
});
const ConnectedRipplModal = connect(
  stateToProps,
)(RipplModal);

export default ConnectedRipplModal;
