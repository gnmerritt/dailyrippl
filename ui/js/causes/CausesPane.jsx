import React from 'react';
import { Row } from 'react-bootstrap';

import Causes from './Causes';

const CausesPane = () =>
  <div className="three-pane causes-pane">
    <Row>
      <h2>Causes</h2>
    </Row>
    <Row>
      <Causes />
    </Row>
  </div>
  ;

export default CausesPane;
