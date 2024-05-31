from django.conf import settings
# LoL Constants
TIER_WEIGHTS = {
    "UNRANKED": 0,
    "IRON": 0,
    "BRONZE": 1,
    "SILVER": 2,
    "GOLD": 3,
    "PLATINUM": 4,
    "EMERALD": 5,
    "DIAMOND": 6,
    "MASTER": 7,
    "GRANDMASTER": 7,
    "CHALLENGER": 7,
}

RANK_WEIGHTS = {
    "IV": 0,
    "III": 1,
    "II": 2,
    "I": 3,
    "NONE": 0, 
}


# Model choices
PLATFORM_CHOICES = [
    ("euw1", "EUW"),
    ("na1", "NA"),
    ("br1", "BR"),
    ("eun1", "EUNE"),
    ("jp1", "JP"),
    ("kr", "KR"),
    ("la1", "LAN"),
    ("la2", "LAS"),
    ("oc1", "OCE"),
    ("ru", "RU"),
    ("tr1", "TR"),
]

REGION_CHOICES = [
    ("europe", "europe"),
    ("americas", "americas"),
    ("asia", "asia"),
]

TIER_CHOICES = [
    ("UNRANKED", "UNRANKED"),
    ("IRON", "IRON"),
    ("BRONZE", "BRONZE"),
    ("SILVER", "SILVER"),
    ("GOLD", "GOLD"),
    ("PLATINUM", "PLATINUM"),
    ("EMERALD", "EMERALD")
    ("DIAMOND", "DIAMOND"),
    ("MASTER", "MASTER"),
    ("GRANDMASTER", "GRANDMASTER"),
    ("CHALLENGER", "CHALLENGER"),
]
RANK_CHOICES = [("I", "I"), ("II", "II"), ("III", "III"), ("IV", "IV"), ("NONE", "NONE")]


PLATFORM_TO_REGION = { # taken from here until pulsefire implements it: https://github.com/iann838/pyot/blob/master/pyot/models/lol/base.py#l12
        "br1": "americas",
        "eun1": "europe",
        "euw1": "europe",
        "jp1": "asia",
        "kr": "asia",
        "la1": "americas",
        "la2": "americas",
        "na1": "americas",
        "oc1": "sea",
        "tr1": "europe",
        "ru": "europe",
        "ph2": "sea",
        "sg2": "sea",
        "th2": "sea",
        "tw2": "sea",
        "vn2": "sea",
    }


# Pulsefire
API_CLIENT_ARGS = {"X-Riot-Token": settings.RIOT_API_KEY}
# Riot API Stuff
SOLOQ = "RANKED_SOLO_5x5" 
FLEXQ = "RANKED_TEAM_5x5"
# https://static.developer.riotgames.com/docs/lol/queues.json
SOLOQ_INT = 420
FLEXQ_INT = 440