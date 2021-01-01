"""This module defines the marker class, representing markers to deter intrusion at a nuclear waste
isolation site, and defines the various markers available in the game"""

from dataclasses import dataclass

NOT_PURCHASABLE = "non-purchasable"
GLOBAL = "global"
SYNERGY_PARTNERSHIP_PREFIX = "synergy_partnership_"
SPOOKY = "spooky"
PRO_EDUCATIONAL = "pro-educational"
EDUCATIONAL = "educational"
TERRAFORMING = "terraforming"
MONOLITH = "monolith"

@dataclass
class Marker: #pylint: disable=too-many-instance-attributes,too-few-public-methods
    """A data-only class representing a marker effecting the waste isolation site"""
    name: str
    base_cost: int
    description: str
    icon_coords: tuple
    icon_image: int
    visibility_init: tuple
    visibility_decay: str
    understandability_init: tuple
    understandability_decay: str
    respectability_init: tuple
    respectability_decay: str
    likability_init: tuple
    likability_decay: str
    usability_init: tuple
    usability_decay: str
    tags: list

    def is_global(self):
        """Returns true if the marker has the global tag"""
        return GLOBAL in self.tags

    def is_purchasable(self):
        """Returns true if the marker lacks the non-purchasable tag"""
        return NOT_PURCHASABLE not in self.tags

    def has_synergy_partnership(self):
        """Returns true if the marker has a synergy_partnership_* tag"""
        for tag in self.tags:
            if tag.startswith(SYNERGY_PARTNERSHIP_PREFIX):
                return True
        return False

    def get_synergy_partnerships(self):
        """Returns the postfixes of all the marker's synergy_partnership_* tags"""
        partnerships = []
        for tag in self.tags:
            if tag.startswith(SYNERGY_PARTNERSHIP_PREFIX):
                partnerships.append(tag[len(SYNERGY_PARTNERSHIP_PREFIX):])
        return partnerships

    def is_spooky(self):
        """Returns true if the marker has the spooky tag"""
        return SPOOKY in self.tags

    def is_pro_educational(self):
        """Returns true if the marker has the pro-educational tag"""
        return PRO_EDUCATIONAL in self.tags

    def is_educational(self):
        """Returns true if the marker has the educational tag"""
        return EDUCATIONAL in self.tags

    def is_terraforming(self):
        """Returns true if the marker has the terraforming tag"""
        return TERRAFORMING in self.tags

    def is_monolith(self):
        """Returns true if the marker has the monolith tag"""
        return MONOLITH in self.tags

markers = {
    "granite-monolith": Marker(
        name="Granite Monolith",
        description="A 5 meter monolith carved from a single piece of granite.\nHighly durable",
        icon_coords=(240,0),
        icon_image = 0,
        base_cost=100000,
        usability_init = (0,0,0),
        usability_decay = "constant",
        visibility_init = (6,6,6),
        visibility_decay = "slow_lin_0",
        respectability_init = (6,6,6),
        respectability_decay = "slow_lin_inc_8",
        likability_init = (0,0,0),
        likability_decay = "constant",
        understandability_init = (9,9,9),
        understandability_decay = "exp_0" ,
        tags=["surface", "structure", "language-dependent", "low-tech", "monolith"]
    ),
    "ruined-granite-monolith": Marker(
        name="Ruined Monolith (Granite)",
        description="This used to be a granite monolith",
        icon_coords=(224,48),
        icon_image = 0,
        base_cost=0,
        usability_init = (0,0,0),
        usability_decay = "constant",
        visibility_init = (2,2,2),
        visibility_decay = "constant",
        respectability_init = (4,4,4),
        respectability_decay = "slow_lin_inc_8",
        likability_init = (0,0,0),
        likability_decay = "constant",
        understandability_init = (2,2,2),
        understandability_decay = "exp_0" ,
        tags=["non-purchasable","surface", "structure", "spooky",
              "language-dependent", "low-tech", "monolith"]
    ),
    "atomic-flower": Marker(
        name="Atomic Flowers",
        description="Flowers with information on the dangers of the site\nencoded into their DNA. \
Self-propagating, but only\neffective against high-tech societies",
        icon_coords=(128,0),
        icon_image = 0,
        base_cost=500000,
        usability_init = (0,0,0),
        usability_decay = "constant",
        visibility_init = (1,1,1),
        visibility_decay = "constant",
        respectability_init = (0,0,0),
        respectability_decay = "constant",
        likability_init = (3,3,3),
        likability_decay = "constant",
        understandability_init = (0,2,8),
        understandability_decay = "constant",
        tags=["surface", "biological", "high-tech", "beautiful"]
    ),
    "ruined-atomic-flower": Marker(
        name="Ruined Atomic Flowers",
        description="These were pretty, once",
        icon_coords=(128,32),
        icon_image = 0,
        base_cost=500000,
        usability_init = (0,0,0),
        usability_decay = "constant",
        visibility_init = (1,1,1),
        visibility_decay = "constant",
        respectability_init = (0,0,0),
        respectability_decay = "constant",
        likability_init = (-3,-3,-3),
        likability_decay = "constant",
        understandability_init = (0,2,8),
        understandability_decay = "constant",
        tags=["non-purchasable","surface", "biological", "high-tech", "spooky"]
    ),
    "good-cult": Marker(
        name="Established Cult",
        description="A highly organized priesthood dedicated to preserving\nthe message that \
this site is dangerous.\nVulnerable to religious turmoil",
        icon_coords=(176,16),
        icon_image = 0,
        base_cost=2000000,
        usability_init = (0,0,0),
        usability_decay = "constant",
        visibility_init = (7,7,7),
        visibility_decay = "constant",
        respectability_init = (7,7,7),
        respectability_decay = "constant",
        likability_init = (5,5,5),
        likability_decay = "constant",
        understandability_init = (10,10,10),
        understandability_decay = "lin_0",
        tags=["active", "biological", "culture-linked", "low-tech", "religious", "global"]
    ),
    "ray-cats": Marker(
        name="Ray Cats",
        description="Cats genetically engineered to glow in the presence\nof radiation, \
accompanied by efforts to pass into\nlegend the message 'avoid places where the cats glow'",
        icon_coords=(112, 0),
        icon_image = 0,
        base_cost=1000000,
        usability_init = (0,0,0),
        usability_decay = "constant",
        visibility_init = (5,5,5),
        visibility_decay = "constant",
        respectability_init = (3,3,3),
        respectability_decay = "constant",
        likability_init = (-2,-2,-2),
        likability_decay = "constant",
        understandability_init = (5,5,5),
        understandability_decay = "constant",
        tags=["biological", "low-tech", "folklore-linked", "global"]
    ),
    "buried-messages": Marker(
        name="Buried Messages",
        description="Warning messages inscribed in ceramics,\nburied at various depths across the \
site.\nMore effective upon cultures with industrial\ndigging technology",
        icon_coords=(64,16),
        icon_image = 0,
        base_cost=100000,
        usability_init = (0,0,0),
        usability_decay = "constant",
        visibility_init = (0,0,0),
        visibility_decay = "constant",
        respectability_init = (3,3,3),
        respectability_decay = "tech_curve",
        likability_init = (-2,-2,-2),
        likability_decay = "lin_0",
        understandability_init = (9,9,9),
        understandability_decay = "exp_0",
        tags=["buried", "low-tech", "linguistic"]
    ),
    "danger-sign": Marker(
        name="Danger Sign",
        description="A sign reading \"danger\" and bearing a radiation\nsymbol",
        icon_coords=(160,16),
        icon_image = 0,
        base_cost=1000,
        usability_init = (0,0,0),
        usability_decay = "constant",
        visibility_init = (1,1,1),
        visibility_decay = "lin_0",
        respectability_init = (7,7,7),
        respectability_decay = "lin_0",
        likability_init = (-2,-2,-2),
        likability_decay = "lin_0",
        understandability_init = (5,5,5),
        understandability_decay = "lin_0",
        tags=["synergy_partnership_1", "linguistic", "pictoral"]
    ),
    "disgust-faces": Marker(
        name="Disgusted Faces",
        description="Depictions of faces in sickness in pain, etched into\nstone",
        icon_coords=(144,16),
        icon_image = 0,
        base_cost=10000,
        usability_init = (0,0,0),
        usability_decay = "constant",
        visibility_init = (2,2,2),
        visibility_decay = "slow_lin_0",
        respectability_init = (0,0,0),
        respectability_decay = "constant",
        likability_init = (-3,-3,-3),
        likability_decay = "constant",
        understandability_init = (3,3,3),
        understandability_decay = "slow_lin_0",
        tags=["synergy_partnership_1", "spooky", "pictoral"]
    ),
    "periodic-table": Marker(
        name="Periodic Table",
        description="A depiction of the periodic table, with the elements\nburied here circled \
and arrows pointing down",
        icon_coords=(192,0),
        icon_image = 0,
        base_cost=10000,
        usability_init = (0,0,0),
        usability_decay = "constant",
        visibility_init = (1,1,1),
        visibility_decay = "lin_0",
        respectability_init = (0,0,0),
        respectability_decay = "constant",
        likability_init = (0,0,0),
        likability_decay = "constant",
        understandability_init = (0,5,5),
        understandability_decay = "constant",
        tags=["educational", "pictoral"]
    ),
    "walk-on-map": Marker(
        name="Walk On Map",
        description="A map of all known waste sites inscribed in the ground",
        icon_coords=(80,16),
        icon_image = 0,
        base_cost=10000,
        usability_init = (0,0,0),
        usability_decay = "constant",
        visibility_init = (8,8,8),
        visibility_decay = "lin_0",
        respectability_init = (1,1,1),
        respectability_decay = "constant",
        likability_init = (2,2,2),
        likability_decay = "constant",
        understandability_init = (0,7,7),
        understandability_decay = "constant",
        tags=["educational", "pictoral"]
    ),
    "star-map": Marker(
        name="Star Map",
        description="A map of the stars showing their position when the\nsite was created and when \
the site will be safe.\nCould be used to calculate age",
        icon_coords=(128,16),
        icon_image = 0,
        base_cost=1000,
        usability_init = (0,0,0),
        usability_decay = "constant",
        visibility_init = (2,2,2),
        visibility_decay = "constant",
        respectability_init = (0,5,5),
        respectability_decay = "constant",
        likability_init = (1,1,1),
        likability_decay = "constant",
        understandability_init = (0,0,0),
        understandability_decay = "constant",
        tags=["educational", "pictoral"]
    ),
    "rubble-field": Marker(
        name="Rubble Field",
        description="Fill the site with random rubble, making access\ndifficult",
        icon_coords=(192,16),
        icon_image = 0,
        base_cost=10000,
        usability_init = (-10,-6,-6),
        usability_decay = "constant",
        visibility_init = (9,9,9),
        visibility_decay = "slow_lin_0",
        respectability_init = (0,0,0),
        respectability_decay = "slow_lin_inc_3",
        likability_init = (-3,-3,-3),
        likability_decay = "lin_0",
        understandability_init = (0,0,0),
        understandability_decay = "constant",
        tags=["terraforming"]
    ),
    "spike-field": Marker(
        name="Spike Field",
        description="Fill the site with dangerous and scary spikes",
        icon_coords=(144,0),
        icon_image = 0,
        base_cost=10000,
        usability_init = (-10,-5,-5),
        usability_decay = "constant",
        visibility_init = (10,10,10),
        visibility_decay = "lin_0",
        respectability_init = (9,9,9),
        respectability_decay = "constant",
        likability_init = (-7,-7,-7),
        likability_decay = "constant",
        understandability_init = (0,0,0),
        understandability_decay = "constant",
        tags=["terraforming", "spooky"]
    ),
    "attractive-monument": Marker(
        name="Beautiful Monument",
        description="A pretty building for your site. Maybe people will\nwant to maintain it?",
        icon_coords=(112,16),
        icon_image = 0,
        base_cost=100000,
        usability_init = (4,4,4),
        usability_decay = "constant",
        visibility_init = (8,8,8),
        visibility_decay = "lin_0",
        respectability_init = (7,7,7),
        respectability_decay = "constant",
        likability_init = (9,9,9),
        likability_decay = "constant",
        understandability_init = (0,0,0),
        understandability_decay = "constant",
        tags=["beautiful","surface"]
    ),
    "ruined-attractive-monument": Marker(
        name="Ruined Attractive Monument",
        description="This used to be a pretty building",
        icon_coords=(112,32),
        icon_image = 0,
        base_cost=10,
        usability_init = (0,0,0),
        usability_decay = "constant",
        visibility_init = (2,2,2),
        visibility_decay = "constant",
        respectability_init = (3,3,3),
        respectability_decay = "constant",
        likability_init = (-2,-2,-2),
        likability_decay = "constant",
        understandability_init = (0,0,0),
        understandability_decay = "constant",
        tags=["non-purchasable", "spooky", "beautiful","surface"]
    ),
    "bad-cult": Marker(
        name="Cult",
        description="A cult of dubious quality",
        icon_coords=(176,0),
        icon_image = 0,
        base_cost=1000,
        usability_init = (0,0,0),
        usability_decay = "constant",
        visibility_init = (7,7,7),
        visibility_decay = "constant",
        respectability_init = (-3,-3,-3),
        respectability_decay = "constant",
        likability_init = (-5,-5,-5),
        likability_decay = "constant",
        understandability_init = (9,9,9),
        understandability_decay = "exp_neg_10",
        tags=["global"]
    ),
    "visitor-center": Marker(
        name="Visitor Center",
        description="Build a visitor center for the site",
        icon_coords=(208,16),
        icon_image = 0,
        base_cost=30000,
        usability_init = (0,0,0),
        usability_decay = "constant",
        visibility_init = (4,4,4),
        visibility_decay = "lin_0",
        respectability_init = (1,1,1),
        respectability_decay = "constant",
        likability_init = (3,3,3),
        likability_decay = "constant",
        understandability_init = (10,10,10),
        understandability_decay = "exp_0",
        tags=["pro-educational", "beatutiful","surface"]
    ),
    "ruined-visitor-center": Marker(
        name="Ruined Visitor Center",
        description="This used to be a visitor center",
        icon_coords=(208,32),
        icon_image = 0,
        base_cost=30000,
        usability_init = (0,0,0),
        usability_decay = "constant",
        visibility_init = (1,1,1),
        visibility_decay = "constant",
        respectability_init = (0,0,0),
        respectability_decay = "constant",
        likability_init = (-1,-1,-1),
        likability_decay = "constant",
        understandability_init = (3,3,3),
        understandability_decay = "exp_0",
        tags=["pro-educational", "non-purchasable", "spooky","surface"]
    ),
    "cemetery": Marker(
        name="Cemetery",
        description="Build a cemetery on the site - maybe people will\nleave it alone",
        icon_coords=(160,0),
        icon_image = 0,
        base_cost=10000,
        usability_init = (-3,-3,-3),
        usability_decay = "constant",
        visibility_init = (7,7,7),
        visibility_decay = "lin_0",
        respectability_init = (10,10,10),
        respectability_decay = "constant",
        likability_init = (-4,-4,-4),
        likability_decay = "constant",
        understandability_init = (-1,-1,-1),
        understandability_decay = "constant",
        tags=["spooky"]
    ),
    "wooden-monolith": Marker(
        name="Wooden Monolith",
        description="A monolith made of wood",
        icon_coords=(224,16),
        icon_image = 0,
        base_cost=1000,
        usability_init = (0,0,0),
        usability_decay = "constant",
        visibility_init = (6,6,6),
        visibility_decay = "fast_lin_0",
        respectability_init = (4,4,4),
        respectability_decay = "constant",
        likability_init = (0,0,0),
        likability_decay = "constant",
        understandability_init = (9,9,9),
        understandability_decay = "exp_0",
        tags=["surface","monolith"]
    ),
    "ruined-wooden-monolith": Marker(
        name="Ruined Wooden Monolith",
        description="This used to be a monolith made of wood",
        icon_coords=(224,32),
        icon_image = 0,
        base_cost=1000,
        usability_init = (0,0,0),
        usability_decay = "constant",
        visibility_init = (1,1,1),
        visibility_decay = "constant",
        respectability_init = (3,3,3),
        respectability_decay = "constant",
        likability_init = (0,0,0),
        likability_decay = "constant",
        understandability_init = (2,2,2),
        understandability_decay = "exp_0",
        tags=["non-purchasable","spooky","surface","monolith"]
    ),
    "metal-monolith": Marker(
        name="Metal Monolith",
        description="A monolith made of metal",
        icon_coords=(240,16),
        icon_image = 0,
        base_cost=10000,
        usability_init = (2,2,2),
        usability_decay = "constant",
        visibility_init = (6,6,6),
        visibility_decay = "lin_0",
        respectability_init = (5,5,5),
        respectability_decay = "constant",
        likability_init = (0,0,0),
        likability_decay = "constant",
        understandability_init = (9,9,9),
        understandability_decay = "exp_0",
        tags=["surface","monolith"]
    ),
    "ruined-metal-monolith": Marker(
        name="Ruined Metal Monolith",
        description="This used to be a monolith made of metal",
        icon_coords=(240,48),
        icon_image = 0,
        base_cost=100,
        usability_init = (1,1,1),
        usability_decay = "constant",
        visibility_init = (2,2,2),
        visibility_decay = "constant",
        respectability_init = (2,2,2),
        respectability_decay = "constant",
        likability_init = (0,0,0),
        likability_decay = "constant",
        understandability_init = (2,2,2),
        understandability_decay = "exp_0",
        tags=["non-purchasable","spooky","surface","monolith"]
    ),
    "death-sculpture": Marker(
        name="Death Sculpture",
        description="Scary!",
        icon_coords=(224,0),
        icon_image = 0,
        base_cost=10000,
        usability_init = (0,0,0),
        usability_decay = "constant",
        visibility_init = (8,8,8),
        visibility_decay = "lin_0",
        respectability_init = (7,7,7),
        respectability_decay = "constant",
        likability_init = (-2,-2,-2),
        likability_decay = "constant",
        understandability_init = (1,1,1),
        understandability_decay = "constant",
        tags=["spooky", "pictoral","surface"]
    ),
    "black-hole": Marker(
        name="Black Hole",
        description="A giant void in the ground. Don't fall in!",
        icon_coords=(208,0),
        icon_image = 0,
        base_cost=10000,
        usability_init = (-10,-7,-7),
        usability_decay = "constant",
        visibility_init = (10,10,10),
        visibility_decay = "slow_lin_0",
        respectability_init = (6,6,6),
        respectability_decay = "constant",
        likability_init = (-6,-6,-6),
        likability_decay = "constant",
        understandability_init = (0,0,0),
        understandability_decay = "constant",
        tags=["terraforming"]
    ),
    #NOTE: THE TERRAINS ARE IN IMAGE 1
    "sand": Marker(
        name="Sand",
        description="It's pretty sandy sand.",
        icon_coords=(16,0),
        icon_image = 1,
        base_cost=0,
        usability_init = (0,0,0),
        usability_decay = "constant",
        visibility_init = (0,0,0),
        visibility_decay = "constant",
        respectability_init = (0,0,0),
        respectability_decay = "constant",
        likability_init = (0,0,0),
        likability_decay = "constant",
        understandability_init = (0,0,0),
        understandability_decay = "constant",
        tags=["non-purchasable"]
    ),
    "grass": Marker(
        name="Grass",
        description="A patch of lush grass.",
        icon_coords=(32,0),
        icon_image = 1,
        base_cost=0,
        usability_init = (0,0,0),
        usability_decay = "constant",
        visibility_init = (0,0,0),
        visibility_decay = "constant",
        respectability_init = (0,0,0),
        respectability_decay = "constant",
        likability_init = (0,0,0),
        likability_decay = "constant",
        understandability_init = (0,0,0),
        understandability_decay = "constant",
        tags=["non-purchasable"]
    ),
    "shadow": Marker(
        name="Shadow",
        description="A nice, shady spot.",
        icon_coords=(0,32),
        icon_image = 1,
        base_cost=0,
        usability_init = (0,0,0),
        usability_decay = "constant",
        visibility_init = (0,0,0),
        visibility_decay = "constant",
        respectability_init = (0,0,0),
        respectability_decay = "constant",
        likability_init = (0,0,0),
        likability_decay = "constant",
        understandability_init = (0,0,0),
        understandability_decay = "constant",
        tags=["non-purchasable"]
    ),
    "marbled-smoke": Marker(
        name="Marbled Smoke",
        description="A plume of marbled smoke.",
        icon_coords=(48,32),
        icon_image = 1,
        base_cost=0,
        usability_init = (0,0,0),
        usability_decay = "constant",
        visibility_init = (0,0,0),
        visibility_decay = "constant",
        respectability_init = (0,0,0),
        respectability_decay = "constant",
        likability_init = (0,0,0),
        likability_decay = "constant",
        understandability_init = (0,0,0),
        understandability_decay = "constant",
        tags=["non-purchasable"]
    ),
    "fire": Marker(
        name="Fire",
        description="Beware the fire here.",
        icon_coords=(16,16),
        icon_image = 1,
        base_cost=0,
        usability_init = (0,0,0),
        usability_decay = "constant",
        visibility_init = (0,0,0),
        visibility_decay = "constant",
        respectability_init = (0,0,0),
        respectability_decay = "constant",
        likability_init = (0,0,0),
        likability_decay = "constant",
        understandability_init = (0,0,0),
        understandability_decay = "constant",
        tags=["non-purchasable"]
    ),
    "pink-candles": Marker(
        name="Pink Candles",
        description="They're pretty.",
        icon_coords=(16,32),
        icon_image = 1,
        base_cost=0,
        usability_init = (0,0,0),
        usability_decay = "constant",
        visibility_init = (0,0,0),
        visibility_decay = "constant",
        respectability_init = (0,0,0),
        respectability_decay = "constant",
        likability_init = (0,0,0),
        likability_decay = "constant",
        understandability_init = (0,0,0),
        understandability_decay = "constant",
        tags=["non-purchasable"]
    ),
    "colorful-stone": Marker(
        name="Colorful Stone",
        description="What an interesting shade of stone.",
        icon_coords=(48,16),
        icon_image = 1,
        base_cost=0,
        usability_init = (0,0,0),
        usability_decay = "constant",
        visibility_init = (0,0,0),
        visibility_decay = "constant",
        respectability_init = (0,0,0),
        respectability_decay = "constant",
        likability_init = (0,0,0),
        likability_decay = "constant",
        understandability_init = (0,0,0),
        understandability_decay = "constant",
        tags=["non-purchasable"]
    ),
    "concrete": Marker(
        name="Concrete",
        description="Good ol' slab of concrete.",
        icon_coords=(0,0),
        icon_image = 1,
        base_cost=0,
        usability_init = (0,0,0),
        usability_decay = "constant",
        visibility_init = (0,0,0),
        visibility_decay = "constant",
        respectability_init = (0,0,0),
        respectability_decay = "constant",
        likability_init = (0,0,0),
        likability_decay = "constant",
        understandability_init = (0,0,0),
        understandability_decay = "constant",
        tags=["non-purchasable"]
    ),
    "yellow-candles": Marker(
        name="Yellow Candles",
        description="These are nice candles.",
        icon_coords=(24,32),
        icon_image = 1,
        base_cost=0,
        usability_init = (0,0,0),
        usability_decay = "constant",
        visibility_init = (0,0,0),
        visibility_decay = "constant",
        respectability_init = (0,0,0),
        respectability_decay = "constant",
        likability_init = (0,0,0),
        likability_decay = "constant",
        understandability_init = (0,0,0),
        understandability_decay = "constant",
        tags=["non-purchasable"]
    ),
    "marbled-tile": Marker(
        name="Marbled Tile",
        description="Regular tile with a marbled design.",
        icon_coords=(32,16),
        icon_image = 1,
        base_cost=0,
        usability_init = (0,0,0),
        usability_decay = "constant",
        visibility_init = (0,0,0),
        visibility_decay = "constant",
        respectability_init = (0,0,0),
        respectability_decay = "constant",
        likability_init = (0,0,0),
        likability_decay = "constant",
        understandability_init = (0,0,0),
        understandability_decay = "constant",
        tags=["non-purchasable"]
    ),
    "dark-sand": Marker(
        name="Dark Sand",
        description="This is some dense sand.",
        icon_coords=(48,48),
        icon_image = 1,
        base_cost=0,
        usability_init = (0,0,0),
        usability_decay = "constant",
        visibility_init = (0,0,0),
        visibility_decay = "constant",
        respectability_init = (0,0,0),
        respectability_decay = "constant",
        likability_init = (0,0,0),
        likability_decay = "constant",
        understandability_init = (0,0,0),
        understandability_decay = "constant",
        tags=["non-purchasable"]
    ),
    "light-sand": Marker(
        name="Light Sand",
        description="Loosely packed white sand",
        icon_coords=(32,48),
        icon_image = 1,
        base_cost=0,
        usability_init = (0,0,0),
        usability_decay = "constant",
        visibility_init = (0,0,0),
        visibility_decay = "constant",
        respectability_init = (0,0,0),
        respectability_decay = "constant",
        likability_init = (0,0,0),
        likability_decay = "constant",
        understandability_init = (0,0,0),
        understandability_decay = "constant",
        tags=["non-purchasable"]
    ),
    "blue-candles": Marker(
        name="Blue Candles",
        description="Very ominous looking candles.",
        icon_coords=(48,0),
        icon_image = 1,
        base_cost=0,
        usability_init = (0,0,0),
        usability_decay = "constant",
        visibility_init = (0,0,0),
        visibility_decay = "constant",
        respectability_init = (0,0,0),
        respectability_decay = "constant",
        likability_init = (0,0,0),
        likability_decay = "constant",
        understandability_init = (0,0,0),
        understandability_decay = "constant",
        tags=["non-purchasable"]
    ),
        "core-top-left": Marker(
        name="Nuclear Core",
        description="Some dangerous is here...",
        icon_coords=(0,64),
        icon_image = 1,
        base_cost=0,
        usability_init = (0,0,0),
        usability_decay = "constant",
        visibility_init = (0,0,0),
        visibility_decay = "constant",
        respectability_init = (0,0,0),
        respectability_decay = "constant",
        likability_init = (0,0,0),
        likability_decay = "constant",
        understandability_init = (0,0,0),
        understandability_decay = "constant",
        tags=["non-purchasable"]
    ),
    "core-top-right": Marker(
        name="Nuclear Core",
        description="Some dangerous is here...",
        icon_coords=(16,64),
        icon_image = 1,
        base_cost=0,
        usability_init = (0,0,0),
        usability_decay = "constant",
        visibility_init = (0,0,0),
        visibility_decay = "constant",
        respectability_init = (0,0,0),
        respectability_decay = "constant",
        likability_init = (0,0,0),
        likability_decay = "constant",
        understandability_init = (0,0,0),
        understandability_decay = "constant",
        tags=["non-purchasable"]
    ),
    "core-bottom-left": Marker(
        name="Nuclear Core",
        description="Some dangerous is here...",
        icon_coords=(0,80),
        icon_image = 1,
        base_cost=0,
        usability_init = (0,0,0),
        usability_decay = "constant",
        visibility_init = (0,0,0),
        visibility_decay = "constant",
        respectability_init = (0,0,0),
        respectability_decay = "constant",
        likability_init = (0,0,0),
        likability_decay = "constant",
        understandability_init = (0,0,0),
        understandability_decay = "constant",
        tags=["non-purchasable"]
    ),
    "core-bottom-right": Marker(
        name="Nuclear Core",
        description="Some dangerous is here...",
        icon_coords=(16,80),
        icon_image = 1,
        base_cost=0,
        usability_init = (0,0,0),
        usability_decay = "constant",
        visibility_init = (0,0,0),
        visibility_decay = "constant",
        respectability_init = (0,0,0),
        respectability_decay = "constant",
        likability_init = (0,0,0),
        likability_decay = "constant",
        understandability_init = (0,0,0),
        understandability_decay = "constant",
        tags=["non-purchasable"]
    ),
    "null": Marker(
        name="Null Marker",
        description="",
        icon_coords=(0, 0),
        icon_image = 1,
        base_cost=0,
        usability_init = (0,0,0),
        usability_decay = "constant",
        visibility_init = (0,0,0),
        visibility_decay = "constant",
        respectability_init = (0,0,0),
        respectability_decay = "constant",
        likability_init = (0,0,0),
        likability_decay = "constant",
        understandability_init = (0,0,0),
        understandability_decay = "constant",
        tags=["non-purchasable"]
    ),
    "site": Marker(
        name="Null Marker",
        description="",
        icon_coords=(0, 0),
        icon_image = 1,
        base_cost=0,
        usability_init = (0,0,0),
        usability_decay = "constant",
        visibility_init = (0,0,0),
        visibility_decay = "constant",
        respectability_init = (0,0,0),
        respectability_decay = "constant",
        likability_init = (0,0,0),
        likability_decay = "constant",
        understandability_init = (0,0,0),
        understandability_decay = "constant",
        tags=["non-purchasable"]
    )
}

def get_marker_keys():
    """Returns the keys of the marker dictionary as a list"""
    return list(markers) # Casting a dictionary to a list returns the keys as a list
