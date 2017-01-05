"""Use Google Civics API to get all the details about """
import logging
import os

import requests

logger = logging.getLogger(__name__)

GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')
base_url = 'https://www.googleapis.com/civicinfo/v2/representatives'


def get_reps_for_address(address):
    """Get representatives for an address (any string)

    Args:
        address: str - an address (lat/long works)

    Returns:
        list of contact info | None (if error)
    """
    if not GOOGLE_API_KEY:
        raise AssertionError('Missing GOOGLE_API_KEY from env')

    # https://developers.google.com/civic-information/docs/v2/representatives
    params = {
        'key': GOOGLE_API_KEY,
        'includeOffices': True,
        'address': address
    }
    resp = requests.get(base_url, params=params)
    if not resp.ok:
        # TODO(carolyn): differentiate btwn malformed address, rate limits, etc
        return

    data = resp.json()
    if 'offices' not in data or 'officials' not in data:
        logger.error('Missing required key from Google response')
        return

    offices = data['offices']
    officials = data['officials']

    # TODO(carolyn): format this like the other api endpoint?
    # for now, just add the office name to the officials
    for office in offices:
        office_name = office['name']
        for i in office['officialIndices']:
            officials[i]['office_name'] = office_name

    return officials
