import lzma
import datetime
import functools
from dataclasses import dataclass
import struct


class BinaryRotator:
    """A class for bytes readizng."""

    def __init__(self, data: bytes) -> None:
        self.buffer: bytes = data
        self.offset: int = 0

    def read(self, offset: int) -> bytes:
        """Reads offseted data."""

        data = self.buffer[self.offset:self.offset+offset]
        self.offset += offset
        return data

    def read_int(self, size: int, signed: bool) -> int:
        """Read a int."""
        return int.from_bytes(
            self.read(size),
            "little",
            signed=signed
        )

    def read_u8(self) -> int:
        return self.read_int(1, False)

    def read_u16(self) -> int:
        return self.read_int(2, False)

    def read_i16(self) -> int:
        return self.read_int(2, True)

    def read_u32(self) -> int:
        return self.read_int(4, False)

    def read_i32(self) -> int:
        return self.read_int(4, True)

    def read_u64(self) -> int:
        return self.read_int(8, False)

    def read_i64(self) -> int:
        return self.read_int(8, True)

    def read_f32(self) -> float:
        return struct.unpack("<f", self.read(4))

    def read_f64(self) -> float:
        return struct.unpack("<f", self.read(8))

    def read_uleb128(self) -> int:
        """Reads a uleb bytes into int."""
        if self.read_u8() != 0x0b:
            return ""

        val = shift = 0
        while True:
            b = self.read_u8()
            val |= (b & 0b01111111) << shift
            if (b & 0b10000000) == 0:
                break
            shift += 7
        return val

    def read_string(self) -> str:
        """Read string."""
        s_len = self.read_uleb128()
        return self.read(s_len).decode()


@dataclass
class ReplayFrame:
    delta: int


@dataclass
class OsuReplayFrame(ReplayFrame):
    x: int
    y: int
    keys: int


@dataclass
class TaikoReplayFrame(ReplayFrame):
    x: int
    keys: int


@dataclass
class CatchReplayFrame(ReplayFrame):
    x: int
    dashing: bool


@dataclass
class ManiaReplayFrame(ReplayFrame):
    keys: int




class ReplayFile:
    """A class representing replay file data."""

    def __init__(self) -> None:
        self.__reader = None

        self.mode: int = 0
        self.osu_version: int = 0
        self.map_md5: str = ""
        self.player_name: str = ""
        self.replay_md5: str = ""
        self.n300: int = 0
        self.n100: int = 0
        self.n50: int = 0
        self.ngeki: int = 0
        self.nkatu: int = 0
        self.nmiss: int = 0
        self.score: int = 0
        self.max_combo: int = 0
        self.perfect: bool = False
        self.mods: int = 0
        self.life_graph: str = ""
        self.timestamp: datetime.datetime = 0
        self._frames: list = None
        self._score_id: int = None
        self._seed: int = None
        self._accuracy: float = None
        self._target_practice_hits: float = None

    @classmethod
    def from_bytes(cls, bytedata: bytes, pure_lzma: bool = False):
        """Parses replay from bytes data."""
        cls.__init__(cls)  # new_instance = cls()

        cls.__reader = BinaryRotator(bytedata)  # new_instance.__reader = ...
        # new_instance.parse_data(pure_lzma)
        return cls.parse_data(cls, pure_lzma)

    @classmethod
    def from_file(cls, file_path: str, pure_lzma: bool = False):
        """Parses replay from file path."""
        new_instance = cls()

        with open(file_path, "rb") as stream:
            new_instance.__reader = BinaryRotator(stream.read())
        return new_instance.parse_data(pure_lzma)

    def __hash__(self):
        return hash(self.replay_md5)

    def parse_lzma(self) -> None:
        """Parses only lzma data from replay."""
        data = lzma.decompress(self.__reader.buffer,
                               format=lzma.FORMAT_AUTO).decode("ascii")
        frames = [frame.split("|") for frame in data.split(",")[:-1]]

        for action in frames:
            if self.osu_version >= 20130319 and action[0] == "-12345":
                # After 20130319 replays started to have seeds.
                self.seed = int(action[3])
                continue

            # We dont know what mode is it so we assume its standard.
            frame = OsuReplayFrame(int(action[0]), float(
                action[1]), float(action[2]), int(action[3]))
            self.frames.append(frame)

    def parse_osu_mods(self):
        """
        None 	0 	
        NoFail 	1 (0) 	
        Easy 	2 (1) 	
        TouchDevice 	4 (2) 	Replaces unused NoVideo mod
        Hidden 	8 (3) 	
        HardRock 	16 (4) 	
        SuddenDeath 	32 (5) 	
        DoubleTime 	64 (6) 	
        Relax 	128 (7) 	
        HalfTime 	256 (8) 	
        Nightcore 	512 (9) 	always used with DT : 512 + 64 = 576
        Flashlight 	1024 (10) 	
        Autoplay 	2048 (11) 	
        SpunOut 	4096 (12) 	
        Relax2 	8192 (13) 	Autopilot
        Perfect 	16384 (14) 	
        Key4 	32768 (15) 	
        Key5 	65536 (16) 	
        Key6 	131072 (17) 	
        Key7 	262144 (18) 	
        Key8 	524288 (19) 	
        keyMod 	1015808 	k4+k5+k6+k7+k8
        FadeIn 	1048576 (20) 	
        Random 	2097152 (21) 	
        LastMod 	4194304 (22) 	Cinema
        TargetPractice 	8388608 (23) 	osu!cuttingedge only
        Key9 	16777216 (24) 	
        Coop 	33554432 (25) 	
        Key1 	67108864 (26) 	
        Key3 	134217728 (27) 	
        Key2 	268435456 (28) 	
        ScoreV2 	536870912 (29) 	
        Mirror 	1073741824 (30) 	
        """
        MODS = {
            "HD": 8,
            "HR": 16,
            "DT": 64,
            "EZ": 2,
            "HT": 256,
            "NC": 512,
            "NF": 1,
            "SD": 32,
            "PF": 16384,
            "FL": 1024,
            "RX": 128,
            "AP": 2048,
            "SO": 4096,
        }

        return functools.reduce(
            lambda acc, val: f"{acc} {val[0]}" if self.mods & val[1] else acc, MODS.items(), "")

    @property
    def accuracy(self):
        if self._accuracy is None:
            all_hit_objects = max(self.n300 + self.n100 +
                                  self.n50 + self.nmiss, 1)
            weighted_value = self.n300 + self.n100 * 1/3 + self.n50 * 1/6
            self._accuracy = weighted_value/all_hit_objects*100
        return self._accuracy

    @property
    def frames(self):
        if self._frames is None:
            self.read_lzma()
        return self._frames

    @property
    def score_id(self):
        if self._score_id is None:
            self.read_lzma()
        return self._score_id

    @property
    def target_practice_hits(self):
        if self._target_practice_hits is None:
            self.read_lzma()
        return self._target_practice_hits

    @property
    def seed(self):
        if self._seed is None:
            self.read_lzma()
        return self._seed

    def read_lzma(self):
        lzma_len = self.__reader.read_i32()
        lzma_data = self.__reader.read(lzma_len)
        data = lzma.decompress(
            lzma_data, format=lzma.FORMAT_AUTO).decode("ascii")
        frames = [frame.split("|") for frame in data.split(",")[:-1]]
        self._frames = []
        for action in frames:
            if self.osu_version >= 20130319 and action[0] == "-12345":
                # After 20130319 replays started to have seeds.
                self._seed = int(action[3])
                continue

            if self.mode == 0:
                frame = OsuReplayFrame(int(action[0]), float(
                    action[1]), float(action[2]), int(action[3]))
            elif self.mode == 1:
                frame = TaikoReplayFrame(
                    int(action[0]), float(action[1]), int(action[3]))
            elif self.mode == 2:
                frame = CatchReplayFrame(
                    int(action[0]), float(action[1]), action[3] == "1")
            elif self.mode == 3:
                frame = ManiaReplayFrame(int(action[0]), int(action[1]))

            self._frames.append(frame)

        # Reference: https://github.com/ppy/osu/blob/84e1ff79a0736aa6c7a44804b585ab1c54a84399/osu.Game/Scoring/Legacy/LegacyScoreDecoder.cs#L78-L81
        if self.osu_version >= 20140721:
            self._score_id = self.__reader.read_i64()
        elif self.osu_version >= 20121008:
            self._score_id = self.__reader.read_i32()

        if self.mods & 8388608:
            self._target_practice_hits = self.__reader.read_f64()

    def parse_timestamp(self, ticks: int):
        return datetime.datetime(1, 1, 1) + datetime.timedelta(microseconds=ticks // 10)

    def parse_data(self, only_lzma: bool):
        """Parses all replay data."""
        if only_lzma:
            self.parse_lzma(self)
            return self

        self.mode = self.__reader.read_u8()
        self.osu_version = self.__reader.read_i32()
        self.map_md5 = self.__reader.read_string()
        self.player_name = self.__reader.read_string()
        self.replay_md5 = self.__reader.read_string()
        self.n300 = self.__reader.read_u16()
        self.n100 = self.__reader.read_u16()
        self.n50 = self.__reader.read_u16()
        self.ngeki = self.__reader.read_u16()
        self.nkatu = self.__reader.read_u16()
        self.nmiss = self.__reader.read_u16()
        self.score = self.__reader.read_i32()
        self.max_combo = self.__reader.read_u16()
        self.perfect = self.__reader.read_u8() == 1
        self.mods = self.__reader.read_i32()
        self.life_graph = self.__reader.read_string()
        self.timestamp = self.parse_timestamp(self.__reader.read_i64())

        return self
