import enum


class ItemType(enum.Enum):
    SKIN = 1
    GEM = 2
    COURIER = 3
    TAUNT = 4
    ITEMS_SET = 5
    TREASURE = 6
    TOOL = 7
    WARDS = 8
    COMMENTATORS = 9
    INTERFACE = 10


class Slot(enum.Enum):
    ABILITY_1 = "Ability 1"
    ABILITY_2 = "Ability 2"
    ABILITY_3 = "Ability 3"
    ABILITY_4 = "Ability 4"
    ACTION_ITEM = "Action Item"
    ANNOUNCER = "Announcer"
    ARMOR = "Armor"
    ARMS = "Arms"
    BACK = "Back"
    BELT = "Belt"
    BODY_HEAD = "Body - Head"
    COURIER = "Courier"
    CURSOR_PACK = "Cursor Pack"
    EMBLEM = "Emblem"
    GLOVES = "Gloves"
    HEAD = "Head"
    HEROIC_EFFIGY = "Heroic Effigy"
    HUB_SKIN = "HUD Skin"
    LEGS = "Legs"
    LOADING_SCREEN = "Loading Screen"
    MEGA_KILL_ANNOUNCER = "Mega-Kill Announcer"
    MISC = "Misc"
    MOUNT = "Mount"
    MULTI_KILL_BANNER = "Multikill Banner"
    MUSIC = "Music"
    N_FA = "N-FA"
    NECK = "Neck"
    OFF_HAND = "Off-Hand"
    Shapeshift = "Shapeshift"
    SHOULDER = "Shoulder"
    SUMMONED_UNIT = "Summoned Unit"
    TAIL = "Tail"
    TAUNT = "Taunt"
    TERRAIN = "Terrain"
    ULTIMATE = "Ultimate"
    VOICE = "Voice"
    WARD = "Ward"
    WEAPON = "Weapon"
    WEATHER = "Weather"
    NONE = None


class Quality(enum.Enum):
    STANDARD = "Standard"
    BASE = "Base"
    INSCRIBED = "Inscribed"
    AUSPICIOUS = "Auspicious"
    GENUINE = "Genuine"
    INFUSED = "Infused"
    EXALTED = "Exalted"
    UNUSUAL = "Unusual"
    ELDER = "Elder"
    FROZEN = "Frozen"
    HEROIC = "Heroic"


class Rarity(enum.Enum):
    COMMON = 1
    UNCOMMON = 2
    MYTHICAL = 3
    RARE = 4
    IMMORTAL = 5
    LEGENDARY = 6
    ARCANA = 7
