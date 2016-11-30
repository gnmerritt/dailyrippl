# Bulk data

## Members of congress

https://github.com/unitedstates/congress-legislators

## Congressional districts

https://github.com/unitedstates/districts

# Sunlight foundation APIs

## Locate congressional district by lat/long

GET https://congress.api.sunlightfoundation.com/districts/locate?latitude=42.374870&longitude=-71.097069

```json
{
    "results": [
        {
            "state": "MA",
            "district": 7
        }
    ],
    "count": 1
}
```
