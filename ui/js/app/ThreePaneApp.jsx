import React from 'react';
import { Grid, Col } from 'react-bootstrap';

import CausesPane from '../causes/CausesPane';
import BillsPane from '../bills/BillsPane';
import ProfilePane from '../profile/ProfilePane';

const ThreePaneApp = () =>
  <Grid fluid>
    <Col md={2}>
      <CausesPane />
    </Col>
    <Col md={7}>
      <BillsPane />
    </Col>
    <Col md={3}>
      <ProfilePane />
    </Col>
  </Grid>
  ;

export default ThreePaneApp;
