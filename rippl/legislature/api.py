from django.http import JsonResponse, HttpResponseBadRequest

from legislature.sunlight.district import DistrictMatcher


def find_district(request):
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
