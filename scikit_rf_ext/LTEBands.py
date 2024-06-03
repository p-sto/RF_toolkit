"""Definition of LTE bands with corresponding uplink/downlink frequencies"""
from dataclasses import dataclass
from typing import Optional

# ChatGPT generated ;)
_LTE_BANDS = {
    1: {'uplink': (1920, 1980), 'downlink': (2110, 2170)},
    2: {'uplink': (1850, 1910), 'downlink': (1930, 1990)},
    3: {'uplink': (1710, 1785), 'downlink': (1805, 1880)},
    4: {'uplink': (1710, 1755), 'downlink': (2110, 2155)},
    5: {'uplink': (824, 849), 'downlink': (869, 894)},
    6: {'uplink': (830, 840), 'downlink': (875, 885)},
    7: {'uplink': (2500, 2570), 'downlink': (2620, 2690)},
    8: {'uplink': (880, 915), 'downlink': (925, 960)},
    9: {'uplink': (1749.9, 1784.9), 'downlink': (1844.9, 1879.9)},
    10: {'uplink': (1710, 1770), 'downlink': (2110, 2170)},
    11: {'uplink': (1427.9, 1447.9), 'downlink': (1475.9, 1495.9)},
    12: {'uplink': (698, 716), 'downlink': (728, 746)},
    13: {'uplink': (777, 787), 'downlink': (746, 756)},
    14: {'uplink': (788, 798), 'downlink': (758, 768)},
    17: {'uplink': (704, 716), 'downlink': (734, 746)},
    18: {'uplink': (815, 830), 'downlink': (860, 875)},
    19: {'uplink': (830, 845), 'downlink': (875, 890)},
    20: {'uplink': (832, 862), 'downlink': (791, 821)},
    21: {'uplink': (1447.9, 1462.9), 'downlink': (1495.9, 1510.9)},
    22: {'uplink': (3410, 3490), 'downlink': (3510, 3590)},
    23: {'uplink': (2000, 2020), 'downlink': (2180, 2200)},
    24: {'uplink': (1625.5, 1660.5), 'downlink': (1525, 1559)},
    25: {'uplink': (1850, 1915), 'downlink': (1930, 1995)},
    26: {'uplink': (814, 849), 'downlink': (859, 894)},
    27: {'uplink': (807, 824), 'downlink': (852, 869)},
    28: {'uplink': (703, 748), 'downlink': (758, 803)},
    29: {'downlink': (717, 728)},  # Downlink only
    30: {'uplink': (2305, 2315), 'downlink': (2350, 2360)},
    31: {'uplink': (452.5, 457.5), 'downlink': (462.5, 467.5)},
    32: {'downlink': (1452, 1496)},  # Downlink only
    33: {'uplink': (1900, 1920), 'downlink': (1900, 1920)},
    34: {'uplink': (2010, 2025), 'downlink': (2010, 2025)},
    35: {'uplink': (1850, 1910), 'downlink': (1850, 1910)},
    36: {'uplink': (1930, 1990), 'downlink': (1930, 1990)},
    37: {'uplink': (1910, 1930), 'downlink': (1910, 1930)},
    38: {'uplink': (2570, 2620), 'downlink': (2570, 2620)},
    39: {'uplink': (1880, 1920), 'downlink': (1880, 1920)},
    40: {'uplink': (2300, 2400), 'downlink': (2300, 2400)},
    41: {'uplink': (2496, 2690), 'downlink': (2496, 2690)},
    42: {'uplink': (3400, 3600), 'downlink': (3400, 3600)},
    43: {'uplink': (3600, 3800), 'downlink': (3600, 3800)},
    44: {'uplink': (703, 803), 'downlink': (703, 803)},
    45: {'uplink': (1447, 1467), 'downlink': (1447, 1467)},
    46: {'uplink': (5150, 5925), 'downlink': (5150, 5925)},
    47: {'uplink': (5855, 5925), 'downlink': (5855, 5925)},
    48: {'uplink': (3550, 3700), 'downlink': (3550, 3700)},
    49: {'uplink': (3550, 3700), 'downlink': (3550, 3700)},
    50: {'uplink': (1432, 1517), 'downlink': (1432, 1517)},
    51: {'uplink': (1427, 1432), 'downlink': (1427, 1432)},
    52: {'uplink': (3300, 3400), 'downlink': (3300, 3400)},
    53: {'uplink': (2483.5, 2495), 'downlink': (2483.5, 2495)},
    65: {'uplink': (1920, 2010), 'downlink': (2110, 2200)},
    66: {'uplink': (1710, 1780), 'downlink': (2110, 2200)},
    67: {'downlink': (738, 758)},  # Downlink only
    68: {'uplink': (698, 728), 'downlink': (753, 783)},
    69: {'downlink': (2570, 2620)},  # Downlink only
    70: {'uplink': (1695, 1710), 'downlink': (1995, 2020)},
    71: {'uplink': (663, 698), 'downlink': (617, 652)},
    72: {'uplink': (461, 469), 'downlink': (451, 459)},
    73: {'uplink': (461, 466), 'downlink': (451, 456)},
    74: {'uplink': (1427, 1470), 'downlink': (1475, 1518)},
    75: {'downlink': (1432, 1517)},  # Downlink only
    76: {'downlink': (1427, 1432)},  # Downlink only
    85: {'uplink': (698, 716), 'downlink': (728, 746)},
}


@dataclass
class FrequencySpan:
    start: float
    stop: float
    unit: str

    @property
    def middle(self) -> float:
        return (self.start + self.start) / 2


@dataclass
class LTEBand:
    band_id: int
    downlink: FrequencySpan
    uplink: Optional[FrequencySpan]

    def __str__(self) -> str:
        if not self.uplink:
            return '<Band {}>: downlink only: [{}-{}] MHz'.format(
                self.band_id,
                self.downlink.start, self.downlink.stop
            )
        else:
            return '<Band {}>: uplink [{}-{}] MHz, downlink: [{}-{}] MHz'.format(
                self.band_id,
                self.uplink.start, self.uplink.stop,
                self.downlink.start, self.downlink.stop
            )


def get_lte_band(band_number: str | int) -> LTEBand:
    """Return LTEBand object based on provided int/str"""
    try:
        band_number = int(band_number)
        item = _LTE_BANDS.get(band_number)
        if not item:
            raise AttributeError('Cannot obtain definition for provided [{}] Band'.format(band_number))
    except ValueError as err:
        raise ValueError('Provide band id as a int-able value, either int or str') from err
    else:
        uplink = item.get('uplink')
        downlink = item['downlink']
        return LTEBand(
            band_id=band_number,
            uplink=FrequencySpan(start=uplink[0], stop=uplink[1], unit='MHz') if uplink else None,
            downlink=FrequencySpan(start=downlink[0], stop=downlink[1], unit='MHz')
        )
