from django.http import JsonResponse, HttpResponseBadRequest

from legislature.sunlight.district import DistrictMatcher
from legislature.queries.representatives import RepresentativeFetcher


def find_district(request):
    """Returns the congressional district for a given user's location"""
    try:
        latitude = request.GET['lat']
        longitude = request.GET['lng']
    except KeyError:
        return HttpResponseBadRequest('Need both "lat" and "lng" query params')
    matcher = DistrictMatcher()
    district = matcher.find_district(latitude, longitude)
    return JsonResponse({
        'state': district.state.abbr,
        'state_name': district.state.name,
        'district': district.number,
        'district_id': district.id,
        'str': str(district)
    })


def fetch_representative(request, district_id):
    """Returns a map of chambers of congress to reps for a district"""
    reps = RepresentativeFetcher()
    return JsonResponse(reps.fetch(district_id))
