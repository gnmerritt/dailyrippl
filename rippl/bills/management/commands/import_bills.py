import djclick as click
from funcy import first
import os
import requests

from bills.models import Bill
from questing.models import Topic
from legislature.models import Representative


BASE_URL = 'https://congress.api.sunlightfoundation.com/{}'
SUNLIGHT_API_KEY = os.getenv('SUNLIGHT_API_KEY')


def _paged_sunlight_request(url, filters):
    """Iterate through results from a Sunlight API endpoint"""
    headers = {'X-APIKEY': SUNLIGHT_API_KEY}
    filters.update({'page': 1, 'per_page': 20})
    page_count = 1
    while page_count > 0:
        resp = requests.get(url, headers=headers, params=filters)
        resp.raise_for_status()
        data = resp.json()
        for result in data['results']:
            yield result

        # update conditional and page filter
        page_count = data['page']['count']
        filters['page'] += 1


def _get_upcoming_bills(start_date):
    """Iterate through upcoming bills from Sunlight"""
    bills_url = BASE_URL.format('upcoming_bills')
    fields = ['bill_id',
              'chamber',
              'legislative_day',
              'range',
              'context',
              'url']
    filters = {'fields': ','.join(fields)}
    if start_date:
        filters['legislative_day__gte'] = start_date
    return _paged_sunlight_request(bills_url, filters)


def _get_bill_details(bill_id):
    """Get details about a bill"""
    url = BASE_URL.format('bills')
    fields = ['popular_title',
              'official_title',
              'summary',
              'keywords',
              'sponsor_id',
              'sponsor.state',
              'sponsor.last_name']
    filters = {'bill_id': bill_id, 'fields': ','.join(fields)}
    return first(_paged_sunlight_request(url, filters)) or {}


def _create_or_update_bill(bill_dict):
    """Create or update a Bill"""
    if 'bill_id' not in bill_dict:
        click.echo('Missing bill_id!')
        return

    # get details
    details = _get_bill_details(bill_dict['bill_id'])

    bill_chamber = bill_dict.get('chamber', '')
    if bill_chamber == 'senate':
        chamber = 'S'
    elif bill_chamber == 'house':
        chamber = 'H'
    else:
        chamber = ''

    defaults = {
        'official_title': details.get('official_title') or '',
        'popular_title': details.get('popular_title') or '',
        'summary': details.get('summary') or '',
        'url': bill_dict.get('url') or '',
        'chamber': chamber
    }

    bill, _ = Bill.objects.update_or_create(sunlight_id=bill_dict['bill_id'],
                                            defaults=defaults)

    # create/add topics from keywords
    keywords = details.get('keywords') or []
    for kw in keywords:
        name = kw if len(kw) <= 60 else kw[:57] + '...'
        topic_defaults = {'name': name, 'desc': kw}
        topic, _ = Topic.objects.get_or_create(name__iexact=name,
                                               defaults=topic_defaults)
        bill.topics.add(topic)

    # attach corresponding sponsor rep.
    bioguide_id = details.get('sponsor_id')
    if bioguide_id:
        try:
            sponsor = Representative.objects.get(bioguide_id=bioguide_id)
            bill.sponsor = sponsor
            bill.save()
        except Representative.DoesNotExist:
            pass


@click.command()
@click.option('--start_date', default=None)
def import_upcoming(start_date):
    """Get upcoming bills from the Sunlight API and update/insert models"""
    for bill_dict in _get_upcoming_bills(start_date):
        _create_or_update_bill(bill_dict)
