import React from 'react';
import { Row } from 'react-bootstrap';

import ClearProfileButton from './ClearProfileButton';
import CongressionalDistrict from './CongressionalDistrict';
import Representatives from './Representatives';

const ProfilePane = () =>
  <div>
    <Row>
      <h2>You</h2>
    </Row>
    <Row>
      <CongressionalDistrict />
    </Row>
    <Row>
      <Representatives />
    </Row>
    <Row>
      <ClearProfileButton />
    </Row>
  </div>
  ;

export default ProfilePane;
