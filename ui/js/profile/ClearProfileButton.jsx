import React from 'react';
import { Button, Modal } from 'react-bootstrap';

import { destroyState } from '../app/LocalStorage';

/**
 * A button with a confirmation modal for clearing all local data
 */
class ClearProfileButton extends React.Component {
  constructor(props, context) {
    super(props, context);
    this.state = { confirming: false };
  }

  setConfirming(confirming) {
    this.setState({ confirming });
  }

  renderConfirmation() {
    const close = () => this.setConfirming(false);
    return (
      <Modal show={this.state.confirming} onHide={close}>
        <Modal.Header closeButton>
          <Modal.Title>Clear your profile?</Modal.Title>
        </Modal.Header>
        <Modal.Body>
          <p>
            This action <b>cannot be undone</b>. We do not store any of your information
            on our servers and so we cannot restore it if you clear it now.
          </p>
        </Modal.Body>
        <Modal.Footer>
          <Button onClick={destroyState} bsStyle="danger">Clear profile</Button>
          <Button onClick={close}>Cancel</Button>
        </Modal.Footer>
      </Modal>
    );
  }

  render() {
    return (
      <div>
        <Button onClick={() => this.setConfirming(true)}>
          Clear my profile
        </Button>
        {this.renderConfirmation()}
      </div>
    );
  }
}

export default ClearProfileButton;
