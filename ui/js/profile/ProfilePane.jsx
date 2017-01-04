import React from 'react';
import { Row } from 'react-bootstrap';

import CongressionalDistrict from './CongressionalDistrict';

const ProfilePane = () =>
  <div>
    <Row>
      <CongressionalDistrict />
    </Row>
    <Row>
      Your representatives are TODO HERE
    </Row>
  </div>
  ;

export default ProfilePane;
