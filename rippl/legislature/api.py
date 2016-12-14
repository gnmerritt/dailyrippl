from django.http import JsonResponse

from legislature.sunlight.district import DistrictMatcher


def find_district(request):
    latitude = request.GET['lat']
    longitude = request.GET['lng']
    matcher = DistrictMatcher()
    district = matcher.find_district(latitude, longitude)
    return JsonResponse({
        'state': district.state.abbr,
        'state_name': district.state.name,
        'district': district.number,
        'str': str(district)
    })
