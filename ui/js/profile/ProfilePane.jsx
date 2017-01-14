import React from 'react';
import { Button, Panel, Row, Col, Glyphicon } from 'react-bootstrap';

import ClearProfileButton from './ClearProfileButton';
import CongressionalDistrict from './CongressionalDistrict';
import Representatives from './Representatives';

class ProfilePane extends React.Component {
  constructor(props, context) {
    super(props, context);
    this.state = { open: true };
  }

  renderHeader() {
    const icon = this.state.open ? 'minus' : 'plus';
    return (
      <Row>
        <Col md={11}>
          <h2>Your Profile</h2>
        </Col>
        <Col md={1}>
          <Button
            bsSize="small"
            onClick={() => this.setState({ open: !this.state.open })}
          >
            <Glyphicon glyph={icon} />
          </Button>
        </Col>
      </Row>
    );
  }

  render() {
    return (
      <Panel header={this.renderHeader()} collapsible expanded={this.state.open}>
        <Col md={4}>
          <CongressionalDistrict />
        </Col>
        <Col md={4}>
          <Representatives />
        </Col>
        <Col md={4}>
          <div>TODO: causes here</div>
          <ClearProfileButton />
        </Col>
      </Panel>
    );
  }
}

export default ProfilePane;
