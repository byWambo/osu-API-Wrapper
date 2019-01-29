import enum


class Mods(enum.Enum):

    NoMod = 0
    NoFail = 1
    Easy = 2
    TouchDevice = 4
    Hidden = 8
    HardRock = 16
    SuddenDeath = 32
    DoubleTime = 64
    Relax = 128
    HalfTime = 256
    Nightcore = 576
    Flashlight = 1024
    Autoplay = 2048
    SpunOut = 4096
    AutoPilot = 8192
    Perfect = 16416


def calculate(raw):
    mods = list()
    for mod in Mods:
        if (mod.value & raw) == mod.value:
            mods.insert(0, mod.name)
    return mods
