import React from 'react';
import { Grid, Col } from 'react-bootstrap';

import ProfilePane from '../profile/ProfilePane';

const ThreePaneApp = () =>
  <Grid fluid>
    <Col md={2}>
      Causes
    </Col>
    <Col md={7}>
      Bills
    </Col>
    <Col md={3}>
      <ProfilePane />
    </Col>
  </Grid>
  ;

export default ThreePaneApp;
