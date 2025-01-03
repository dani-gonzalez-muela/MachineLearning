name_dict = {
    1: "Bulbasaur",
    2: "Ivysaur",
    3: "Venusaur",
    4: "Charmander",
    5: "Charmeleon",
    6: "Charizard",
    7: "Squirtle",
    8: "Wartortle",
    9: "Blastoise",
    10: "Caterpie",
    11: "Metapod",
    12: "Butterfree",
    13: "Weedle",
    14: "Kakuna",
    15: "Beedrill",
    16: "Pidgey",
    17: "Pidgeotto",
    18: "Pidgeot",
    19: "Rattata",
    20: "Raticate",
    21: "Spearow",
    22: "Fearow",
    23: "Ekans",
    24: "Arbok",
    25: "Pikachu",
    26: "Raichu",
    27: "Sandshrew",
    28: "Sandslash",
    29: "Nidoran F",
    30: "Nidorina",
    31: "Nidoqueen",
    32: "Nidoran M",
    33: "Nidorino",
    34: "Nidoking",
    35: "Clefairy",
    36: "Clefable",
    37: "Vulpix",
    38: "Ninetales",
    39: "Jigglypuff",
    40: "Wigglytuff",
    41: "Zubat",
    42: "Golbat",
    43: "Oddish",
    44: "Gloom",
    45: "Vileplume",
    46: "Paras",
    47: "Parasect",
    48: "Venonat",
    49: "Venomoth",
    50: "Diglett",
    51: "Dugtrio",
    52: "Meowth",
    53: "Persian",
    54: "Psyduck",
    55: "Golduck",
    56: "Mankey",
    57: "Primeape",
    58: "Growlithe",
    59: "Arcanine",
    60: "Poliwag",
    61: "Poliwhirl",
    62: "Poliwrath",
    63: "Abra",
    64: "Kadabra",
    65: "Alakazam",
    66: "Machop",
    67: "Machoke",
    68: "Machamp",
    69: "Bellsprout",
    70: "Weepinbell",
    71: "Victreebel",
    72: "Tentacool",
    73: "Tentacruel",
    74: "Geodude",
    75: "Graveler",
    76: "Golem",
    77: "Ponyta",
    78: "Rapidash",
    79: "Slowpoke",
    80: "Slowbro",
    81: "Magnemite",
    82: "Magneton",
    83: "Farfetch'd",
    84: "Doduo",
    85: "Dodrio",
    86: "Seel",
    87: "Dewgong",
    88: "Grimer",
    89: "Muk",
    90: "Shellder",
    91: "Cloyster",
    92: "Gastly",
    93: "Haunter",
    94: "Gengar",
    95: "Onix",
    96: "Drowzee",
    97: "Hypno",
    98: "Krabby",
    99: "Kingler",
    100: "Voltorb",
    101: "Electrode",
    102: "Exeggcute",
    103: "Exeggutor",
    104: "Cubone",
    105: "Marowak",
    106: "Hitmonlee",
    107: "Hitmonchan",
    108: "Lickitung",
    109: "Koffing",
    110: "Weezing",
    111: "Rhyhorn",
    112: "Rhydon",
    113: "Chansey",
    114: "Tangela",
    115: "Kangaskhan",
    116: "Horsea",
    117: "Seadra",
    118: "Goldeen",
    119: "Seaking",
    120: "Staryu",
    121: "Starmie",
    122: "Mr. Mime",
    123: "Scyther",
    124: "Jynx",
    125: "Electabuzz",
    126: "Magmar",
    127: "Pinsir",
    128: "Tauros",
    129: "Magikarp",
    130: "Gyarados",
    131: "Lapras",
    132: "Ditto",
    133: "Eevee",
    134: "Vaporeon",
    135: "Jolteon",
    136: "Flareon",
    137: "Porygon",
    138: "Omanyte",
    139: "Omastar",
    140: "Kabuto",
    141: "Kabutops",
    142: "Aerodactyl",
    143: "Snorlax",
    144: "Articuno",
    145: "Zapdos",
    146: "Moltres",
    147: "Dratini",
    148: "Dragonair",
    149: "Dragonite",
    150: "Mewtwo",
    "Bulbasaur": 1,
    "Ivysaur": 2,
    "Venusaur": 3,
    "Charmander": 4,
    "Charmeleon": 5,
    "Charizard": 6,
    "Squirtle": 7,
    "Wartortle": 8,
    "Blastoise": 9,
    "Caterpie": 10,
    "Metapod": 11,
    "Butterfree": 12,
    "Weedle": 13,
    "Kakuna": 14,
    "Beedrill": 15,
    "Pidgey": 16,
    "Pidgeotto": 17,
    "Pidgeot": 18,
    "Rattata": 19,
    "Raticate": 20,
    "Spearow": 21,
    "Fearow": 22,
    "Ekans": 23,
    "Arbok": 24,
    "Pikachu": 25,
    "Raichu": 26,
    "Sandshrew": 27,
    "Sandslash": 28,
    "Nidoran F": 29,
    "Nidorina": 30,
    "Nidoqueen": 31,
    "Nidoran M": 32,
    "Nidorino": 33,
    "Nidoking": 34,
    "Clefairy": 35,
    "Clefable": 36,
    "Vulpix": 37,
    "Ninetales": 38,
    "Jigglypuff": 39,
    "Wigglytuff": 40,
    "Zubat": 41,
    "Golbat": 42,
    "Oddish": 43,
    "Gloom": 44,
    "Vileplume": 45,
    "Paras": 46,
    "Parasect": 47,
    "Venonat": 48,
    "Venomoth": 49,
    "Diglett": 50,
    "Dugtrio": 51,
    "Meowth": 52,
    "Persian": 53,
    "Psyduck": 54,
    "Golduck": 55,
    "Mankey": 56,
    "Primeape": 57,
    "Growlithe": 58,
    "Arcanine": 59,
    "Poliwag": 60,
    "Poliwhirl": 61,
    "Poliwrath": 62,
    "Abra": 63,
    "Kadabra": 64,
    "Alakazam": 65,
    "Machop": 66,
    "Machoke": 67,
    "Machamp": 68,
    "Bellsprout": 69,
    "Weepinbell": 70,
    "Victreebel": 71,
    "Tentacool": 72,
    "Tentacruel": 73,
    "Geodude": 74,
    "Graveler": 75,
    "Golem": 76,
    "Ponyta": 77,
    "Rapidash": 78,
    "Slowpoke": 79,
    "Slowbro": 80,
    "Magnemite": 81,
    "Magneton": 82,
    "Farfetch'd": 83,
    "Doduo": 84,
    "Dodrio": 85,
    "Seel": 86,
    "Dewgong": 87,
    "Grimer": 88,
    "Muk": 89,
    "Shellder": 90,
    "Cloyster": 91,
    "Gastly": 92,
    "Haunter": 93,
    "Gengar": 94,
    "Onix": 95,
    "Drowzee": 96,
    "Hypno": 97,
    "Krabby": 98,
    "Kingler": 99,
    "Voltorb": 100,
    "Electrode": 101,
    "Exeggcute": 102,
    "Exeggutor": 103,
    "Cubone": 104,
    "Marowak": 105,
    "Hitmonlee": 106,
    "Hitmonchan": 107,
    "Lickitung": 108,
    "Koffing": 109,
    "Weezing": 110,
    "Rhyhorn": 111,
    "Rhydon": 112,
    "Chansey": 113,
    "Tangela": 114,
    "Kangaskhan": 115,
    "Horsea": 116,
    "Seadra": 117,
    "Goldeen": 118,
    "Seaking": 119,
    "Staryu": 120,
    "Starmie": 121,
    "Mr. Mime": 122,
    "Scyther": 123,
    "Jynx": 124,
    "Electabuzz": 125,
    "Magmar": 126,
    "Pinsir": 127,
    "Tauros": 128,
    "Magikarp": 129,
    "Gyarados": 130,
    "Lapras": 131,
    "Ditto": 132,
    "Eevee": 133,
    "Vaporeon": 134,
    "Jolteon": 135,
    "Flareon": 136,
    "Porygon": 137,
    "Omanyte": 138,
    "Omastar": 139,
    "Kabuto": 140,
    "Kabutops": 141,
    "Aerodactyl": 142,
    "Snorlax": 143,
    "Articuno": 144,
    "Zapdos": 145,
    "Moltres": 146,
    "Dratini": 147,
    "Dragonair": 148,
    "Dragonite": 149,
    "Mewtwo": 150,
}