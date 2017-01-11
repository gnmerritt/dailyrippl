import React from 'react';
import { Row } from 'react-bootstrap';

import Bills from './Bills';

const BillsPane = () =>
  <div className="three-pane bills-pane">
    <Row>
      <h2>Upcoming legislation</h2>
    </Row>
    <Row>
      <Bills />
    </Row>
  </div>
  ;

export default BillsPane;
