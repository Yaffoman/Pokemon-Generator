import numpy as np
from random import random

names1 = ["Dra", "Drago", "Chame", "Alba", "Alli", "Alliga", "Ante", "Arma", "Barra", "Ba", "Bea", "Bi", "Buffa",
          "Cate", "Chimpa", "Coyo", "Cro", "Croco", "Dino", "Ele", "Ela", "Falco", "Fla", "Flami", "Gaze", "Gira",
          "Gori", "Hippo", "Hye", "Jagua", "Kanga", "Koa", "Leo", "Mana", "Octo", "Peli", "Pigeo", "Porcu", "Rhino",
          "Sala", "Salama", "Scorpi", "Sha", "Swa", "Toa", "Walla", "Wolve"]
names2 = ["bite", "buff", "byss", "ceon", "coon", "cross", "ctric", "dily", "dos", "drill", "free", "lax", "lite",
          "lix", "loon", "lord", "low", "ly", "mire", "mish", "mite", "nite", "nium", "nub", "nyte", "pet", "phy",
          "pip", "pix", "plume", "pod", "rak", "reon", "ron", "ros", "saur", "sion", "sire", "slash", "star", "tar",
          "tic", "tine", "tle", "ton", "tone", "tric", "tuff", "zar", "zel"]
names3 = ["Allig", "Albatr", "Armad", "Donk", "Badg", "Barrac", "Bis", "Buff", "Caterp", "Chick", "Chimpanz", "Chimp",
          "Cobr", "Croc", "Crocod", "Dinos", "Dolph", "Drag", "Drac", "Eleph", "Falc", "Flam", "Gaz", "Pand", "Hamst",
          "Hippop", "Hyen", "Jag", "Kangar", "Koal", "Komod", "Leop", "Lem", "Lobst", "Mant", "Mosq", "Octop", "Ostr",
          "Oyst", "Panth", "Parr", "Pelic", "Peng", "Salam", "Rhin", "Rhinoc", "Pand", "Scorp", "Spid", "Term", "Tig",
          "Turt", "Vult", "Vultur", "Weas", "Wolv"]
names4 = ["aid", "air", "airy", "ama", "aring", "ash", "ath", "aza", "eaf", "eat", "ee", "eler", "ena", "eo", "eon",
          "epi", "ette", "evoir", "ia", "ig", "ion", "ire", "ita", "itar", "ite", "ith", "ithe", "ius", "ix", "oal",
          "oke", "ola", "oom", "ops", "ora", "ord", "ory", "oss", "oth", "otic", "otto", "ou", "ow", "una", "ung",
          "uno", "uzz", "ygon", "yle", "yss"]
names5 = ["Iro", "Gole", "Magma", "Blast", "Veno", "Gro", "Electri", "Ele", "Magi", "Spi", "Qui", "Gladia", "Fie",
          "Glaci", "Skele", "Flu", "Aqua", "Hype", "Kine", "Speci", "Chime", "Terro", "Horro", "Gho", "Bone", "Craze",
          "Flame", "Steel", "War", "Char", "Doom", "Slow", "Quick", "Elec", "Spin", "Quil", "Ash", "Shel", "Chill",
          "Fier", "Volt", "Star", "Ram", "Whirl", "Stun"]
names6 = ["bat", "bil", "boon", "bug", "dine", "fly", "meleon", "guin", "hawk", "hog", "hopper", "key", "king", "ling",
          "madillo", "mingo", "mite", "nea", "pecker", "phant", "phin", "pie", "pion", "quito", "raffe", "ray", "rilla",
          "roach", "ron", "sel", "ster", "tile", "topus", "vark", "whale", "wing", "zelle"]
names7 = ["Aquat", "Ash", "Bell", "Blast", "Bon", "Burn", "Carn", "Char", "Chill", "Chim", "Dem", "Dew", "Doom", "Drop",
          "Earth", "Elec", "Electr", "Fier", "Fluff", "Glac", "Glad", "Glas", "Gold", "Goth", "Grow", "Herb", "Hunt",
          "Hyp", "Iron", "Kinet", "Kyn", "Magic", "Magm", "Marsh", "Meg", "Melt", "Molt", "Mount", "Ninj", "Odd",
          "Quick", "Quil", "Ram", "Ramp", "Rock", "Sand", "Shel", "Silver", "Skel", "Slow", "Spec", "Spin", "Star",
          "Steel", "Stun", "Terr", "Venom", "Volt", "War", "Whirl", "Wint"]
names8 = ["abura", "aby", "acle", "acuda", "adger", "adillo", "alo", "amander", "amel", "ander", "anzee", "api", "arak",
          "aroo", "aros", "atee", "atross", "ecta", "een", "ela", "elope", "ena", "eon", "ephant", "erine", "erpillar",
          "eton", "ey", "ibia", "ibou", "ican", "ida", "igator", "illa", "ing", "ingale", "ingo", "ish", "itar",
          "eleon", "ypus", "ite", "ium", "oceros", "oda", "odile", "odo", "onite", "oon", "oose", "opotamus", "opus",
          "ora", "orb", "os", "osaur", "ossum", "oth", "owary", "oyote", "uar", "uin", "uito", "upine", "utor", "ybara",
          "yte"]
names9 = ["Alpaking", "Alphatross", "Antelobster", "Antethereal", "Apricode", "Aquail", "Arachnibble", "Arachnite",
          "Autoad", "Baboom", "Badgerbil", "Bambinosaur", "Bamboa", "Bamboozle", "Barracupid", "Beauty-Rex",
          "Beavermin", "Berriot", "Bisong", "Blazebra", "Boaris", "Brasselle", "Brasshopper", "Brawlphin", "Brawnkey",
          "Bumble Beetle", "Bunnibs", "Butterflux", "Cabarrage", "Caesardine", "Camoose", "Camosquito", "Camouse",
          "Caterpixie", "Celestiger", "Charachnid", "Cheeturbo", "Chickombo", "Chimpanther", "Clovertex", "Cobrawl",
          "Cocobra", "Cottonic", "Cowl", "Crabbit", "Crocodoom", "Demongoose", "Demonkey", "Dinoscythe", "Discorpion",
          "Dolphire", "Donkhi", "Dragonightmare", "Drummingbird", "Eaglide", "Echound", "Elandroid", "Elephantom",
          "Falcondor", "Fearkat", "Flamimic", "Flyte", "Frogre", "Frostrich", "Fuseal", "Fuzebra", "Geishark",
          "Gerbile", "Ghostrich", "Giraffle", "Globster", "Gnuke", "Goath", "Groundog", "Hamstorm", "Hamstun",
          "Harlequill", "Hawkward", "Hedgehawk", "Hippong", "Hippony", "Hippounce", "Hitmantis", "Hornettle", "Hypony",
          "Ingotter", "Jackalfa", "Jaguava", "Jellyfists", "Jestingray", "Jollygator", "Kangaroar", "Kangarookie",
          "Kingray", "Knightingale", "Koalamb", "Koalasso", "Koalava", "Komodough", "Komodozer", "Laserpent",
          "Lemonster", "Leopanther", "Leopaws", "Lionic", "Llamagic", "Lobsteroid", "Magmeleon", "Magnettle", "Magpine",
          "Manateeth", "Mascotton", "Mermantis", "Mockroach", "Mohawk", "Monkeye", "Neopard", "Numbat", "Octopine",
          "Octopuds", "Octopup", "Orcabbage", "Ottermite", "Oysterminate", "Pandaisy", "Pandame", "Pandamonium",
          "Pandarkness", "Pandata", "Pandaw", "Pandaze", "Panthug", "Papayak", "Parriot", "Parsnipe", "Pelicanine",
          "Penguage", "Penguine", "Penguinite", "Pigeode", "Pigeoid", "Pigeonite", "Pigloo", "Ponymph", "Porcupid",
          "Porcupike", "Porpoison", "Potatoad", "Proctopus", "Propelican", "Psychound", "Pyrose", "Quackal", "Quailava",
          "Quaileaf", "Quailynx", "Rabbite", "Rabbyte", "Raccoconut", "Raccocoon", "Recyclops", "Repelican", "Rhinome",
          "Rhinosaur", "Rhinova", "Riotter", "Salamaniac", "Salamantis", "Salmonk", "Sardeeno", "Scarabyte", "Scorpike",
          "Scorpine", "Scorpish", "Sharcade", "Sharctic", "Snailment", "Soyak", "Soyster", "Squidle", "Squidol",
          "Stingrage", "Sumouse", "Swanna", "Termime", "Termitis", "Thortoise", "Tomatoad", "Tortoros", "Troutlaw",
          "Tsardine", "Tucanine", "Turtoro", "Turtoy", "Turtusk", "Tuturkey", "Twilightingale", "Ursign", "Ursire",
          "Vanillama", "Vaporc", "Vilemon", "Viperil", "Viperk", "Vultune", "Wallabyte", "Walruse", "Walrust",
          "Warachnid", "Warthawk", "Weaseal", "Whaleaf", "Wispider", "Wolfix", "Wombattle", "Woolf", "Wrathhog",
          "Yetiger", "Zapple", "Zebrawl"]


def nameGen():
    names = ""
    i = np.random.randint(0, 10)

    if i < 2:
        rnd0 = np.random.randint(0, len(names1))
        rnd1 = np.random.randint(0, len(names2))
        names = names1[rnd0] + names2[rnd1]
    elif i < 4:
        rnd0 = np.random.randint(0, len(names3))
        rnd1 = np.random.randint(0, len(names4))
        names = names3[rnd0] + names4[rnd1]
    elif i < 6:
        rnd0 = np.random.randint(0, len(names5))
        rnd1 = np.random.randint(0, len(names6))
        names = names5[rnd0] + names6[rnd1]
    elif i < 8:
        rnd0 = np.random.randint(0, len(names7))
        rnd1 = np.random.randint(0, len(names8))
        names = names7[rnd0] + names8[rnd1]
    else:
        rnd0 = np.random.randint(0, len(names9))
        names = names9[rnd0]
    return names


nombres = []

for i in range(100000):
    nombres.append(nameGen())

print(nombres)
