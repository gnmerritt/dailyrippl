from django.http import JsonResponse, HttpResponseBadRequest
from django.shortcuts import get_object_or_404


from legislature.sunlight.district import DistrictMatcher
from legislature.google_civics import get_reps_for_address
from legislature.queries.representatives import RepresentativeFetcher
from legislature.queries.districts import DistrictSerializer
from legislature.models import District


def find_district(request):
    """Returns the congressional district for a given user's location"""
    try:
        latitude = request.GET['lat']
        longitude = request.GET['lng']
    except KeyError:
        return HttpResponseBadRequest('Need both "lat" and "lng" query params')
    matcher = DistrictMatcher()
    district = matcher.find_district(latitude, longitude)
    return JsonResponse(DistrictSerializer(district).data)


def fetch_district(request, district_id):
    district = get_object_or_404(District, pk=district_id)
    return JsonResponse(DistrictSerializer(district).data)


def fetch_representative(request, district_id):
    """Returns a map of chambers of congress to reps for a district"""
    reps = RepresentativeFetcher()
    return JsonResponse(reps.fetch(district_id))


def fetch_address_reps(request):
    """Return a list with contact info for representatives of an address"""
    address = request.GET.get('address')
    if not address:
        return HttpResponseBadRequest('Need "address" query param')

    contacts = get_reps_for_address(address)
    if not contacts:
        return HttpResponseBadRequest(
            'Could not fetch representatives for address "{}"'.format(address))
    return JsonResponse(contacts)
