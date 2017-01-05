from rest_framework.throttling import AnonRateThrottle


class BurstRateThrottle(AnonRateThrottle):
    rate = '100/min'


class SustainedRateThrottle(AnonRateThrottle):
    rate = '1000/day'
