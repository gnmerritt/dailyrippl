import React from 'react';
import { Grid, Row, Col } from 'react-bootstrap';

import CausesPane from '../causes/CausesPane';
import BillsPane from '../bills/BillsPane';
import ProfilePane from '../profile/ProfilePane';

const ThreePaneApp = () =>
  <Grid fluid>
    <Row>
      <Col md={12}>
        <ProfilePane />
      </Col>
    </Row>
    <Col md={4}>
      <CausesPane />
    </Col>
    <Col md={8}>
      <BillsPane />
    </Col>
  </Grid>
  ;

export default ThreePaneApp;
