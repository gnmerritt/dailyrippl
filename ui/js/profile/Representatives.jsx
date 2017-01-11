import React, { PropTypes } from 'react';
import { connect } from 'react-redux';

const renderRep = rep =>
  <div key={rep.bioguide_id}>
    <div>{rep.first} {rep.last} ({rep.bioguide_id})</div>
    <div>TODO: phone #</div>
  </div>
  ;


const Representatives = props =>
  <div>
    <h3>House of Representatives</h3>
    {props.house && props.house.map(renderRep)}
    <h3>Senate</h3>
    {props.senate && props.senate.map(renderRep)}
  </div>
  ;

export const repShape = PropTypes.shape({
  bioguide_id: PropTypes.string.isRequired,
  first: PropTypes.string.isRequired,
  last: PropTypes.string.isRequired,
});

Representatives.propTypes = {
  senate: PropTypes.arrayOf(repShape),
  house: PropTypes.arrayOf(repShape),
};

const stateToProps = state => ({
  senate: state.representatives.SEN,
  house: state.representatives.HOR,
});

const ConnectedReps = connect(
  stateToProps,
)(Representatives);

export default ConnectedReps;
