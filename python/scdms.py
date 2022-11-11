# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild

import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO
from enum import Enum


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 9):
    raise Exception("Incompatible Kaitai Struct Python API: 0.9 or later is required, but you have %s" % (kaitaistruct.__version__))

class Scdms(KaitaiStruct):

    class Headers(Enum):
        channel_hdr = 0
        waveform_hdr = 1
        dcrc_hdr = 2
        detector_hdr = 3
        readout_hdr = 4
        trigger_hdr = 5
        prim_dcrc_hdr = 6
        primitive_hdr = 7
        trailer = 8
        scdms_hdr = 9

    class TriggerTypes(Enum):
        physics = 1
        borr = 2
        irr = 3
        eorr = 4
        bcr = 5
        borts = 6
        eorts = 7
    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self._read()

    def _read(self):
        self.scdms_hdr = Scdms.ScdmsHeader(self._io, self, self._root)
        self.n_triggers = []
        for i in range(self.scdms_hdr.total_triggers):
            _on = self.scdms_hdr.format_version
            if _on == 1:
                self.n_triggers.append(Scdms.VOneTrigger(self._io, self, self._root))
            elif _on == 2:
                self.n_triggers.append(Scdms.VTwoTrigger(self._io, self, self._root))

        self.scdms_footer = Scdms.Trailer(self._io, self, self._root)

    class VTwoTrigger(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.trigger_meta = Scdms.VTwoTrigMeta(self._io, self, self._root)
            self.n_primitives = []
            for i in range(self.trigger_meta.num_primitives):
                self.n_primitives.append(Scdms.Primitive(self._io, self, self._root))

            self.packed = self._io.read_u4le()
            self.n_detectors = []
            for i in range(self.detectors_in_event):
                self.n_detectors.append(Scdms.Detector(self._io, self, self._root))


        @property
        def detectors_in_event(self):
            if hasattr(self, '_m_detectors_in_event'):
                return self._m_detectors_in_event

            self._m_detectors_in_event = (self.packed & 268435455)
            return getattr(self, '_m_detectors_in_event', None)

        @property
        def det_header(self):
            if hasattr(self, '_m_det_header'):
                return self._m_det_header

            self._m_det_header = KaitaiStream.resolve_enum(Scdms.Headers, ((self.packed & 4026531840) >> 28))
            return getattr(self, '_m_det_header', None)


    class Channel(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.packed = self._io.read_u4le()
            self.n_pre_pulse_samples = self._io.read_u4le()
            self.n_on_pulse_samples = self._io.read_u4le()
            self.n_post_pulse_samples = self._io.read_u4le()
            self.sample_rate_low = self._io.read_u2le()
            self.sample_rate_high = self._io.read_u2le()
            self.sample = []
            for i in range(((self.n_pre_pulse_samples + self.n_on_pulse_samples) + self.n_post_pulse_samples)):
                self.sample.append(self._io.read_u2le())


        @property
        def ch_type(self):
            if hasattr(self, '_m_ch_type'):
                return self._m_ch_type

            self._m_ch_type = (self.packed & 3)
            return getattr(self, '_m_ch_type', None)

        @property
        def ch_num(self):
            if hasattr(self, '_m_ch_num'):
                return self._m_ch_num

            self._m_ch_num = ((self.packed & 60) >> 2)
            return getattr(self, '_m_ch_num', None)

        @property
        def pre_trigger_offset(self):
            if hasattr(self, '_m_pre_trigger_offset'):
                return self._m_pre_trigger_offset

            self._m_pre_trigger_offset = ((self.packed & 268435392) >> 6)
            return getattr(self, '_m_pre_trigger_offset', None)

        @property
        def chnl_header(self):
            if hasattr(self, '_m_chnl_header'):
                return self._m_chnl_header

            self._m_chnl_header = KaitaiStream.resolve_enum(Scdms.Headers, ((self.packed & 4026531840) >> 28))
            return getattr(self, '_m_chnl_header', None)


    class VOneTrigMeta(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.packed_1 = self._io.read_u4le()
            self.trigger_id = self._io.read_u4le()
            self.trigger_type = KaitaiStream.resolve_enum(Scdms.TriggerTypes, self._io.read_u4le())
            self.global_timestamp_low = self._io.read_u4le()
            self.global_timestamp_high = self._io.read_u4le()
            self.packed_2 = self._io.read_u4le()
            self.length_of_entry = self._io.read_u4le()

        @property
        def event_size(self):
            if hasattr(self, '_m_event_size'):
                return self._m_event_size

            self._m_event_size = (self.packed_1 & 268435455)
            return getattr(self, '_m_event_size', None)

        @property
        def trig_header(self):
            if hasattr(self, '_m_trig_header'):
                return self._m_trig_header

            self._m_trig_header = KaitaiStream.resolve_enum(Scdms.Headers, ((self.packed_1 & 4026531840) >> 28))
            return getattr(self, '_m_trig_header', None)

        @property
        def num_primitives(self):
            if hasattr(self, '_m_num_primitives'):
                return self._m_num_primitives

            self._m_num_primitives = (self.packed_2 & 268435455)
            return getattr(self, '_m_num_primitives', None)

        @property
        def prim_header(self):
            if hasattr(self, '_m_prim_header'):
                return self._m_prim_header

            self._m_prim_header = KaitaiStream.resolve_enum(Scdms.Headers, ((self.packed_1 & 4026531840) >> 28))
            return getattr(self, '_m_prim_header', None)


    class Detector(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.detector_meta = Scdms.DetMeta(self._io, self, self._root)
            self.n_channels = []
            for i in range(self.detector_meta.num_channels_to_follow):
                self.n_channels.append(Scdms.Channel(self._io, self, self._root))



    class ScdmsHeader(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.packed = self._io.read_u4le()

        @property
        def overall_header(self):
            if hasattr(self, '_m_overall_header'):
                return self._m_overall_header

            self._m_overall_header = KaitaiStream.resolve_enum(Scdms.Headers, ((self.packed & 4026531840) >> 28))
            return getattr(self, '_m_overall_header', None)

        @property
        def total_triggers(self):
            if hasattr(self, '_m_total_triggers'):
                return self._m_total_triggers

            self._m_total_triggers = (self.packed & 4095)
            return getattr(self, '_m_total_triggers', None)

        @property
        def format_version(self):
            if hasattr(self, '_m_format_version'):
                return self._m_format_version

            self._m_format_version = ((self.packed & 268431360) >> 12)
            return getattr(self, '_m_format_version', None)


    class VTwoTrigMeta(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.packed_1 = self._io.read_u4le()
            self.trigger_id = self._io.read_u4le()
            self.event_number = self._io.read_u4le()
            self.packed_2 = self._io.read_u4le()
            self.global_timestamp_low = self._io.read_u4le()
            self.global_timestamp_high = self._io.read_u4le()
            self.packed_3 = self._io.read_u4le()
            self.length_of_entry = self._io.read_u4le()

        @property
        def prim_header(self):
            if hasattr(self, '_m_prim_header'):
                return self._m_prim_header

            self._m_prim_header = KaitaiStream.resolve_enum(Scdms.Headers, ((self.packed_3 & 4026531840) >> 28))
            return getattr(self, '_m_prim_header', None)

        @property
        def num_primitives(self):
            if hasattr(self, '_m_num_primitives'):
                return self._m_num_primitives

            self._m_num_primitives = (self.packed_3 & 268435455)
            return getattr(self, '_m_num_primitives', None)

        @property
        def trigger_type(self):
            if hasattr(self, '_m_trigger_type'):
                return self._m_trigger_type

            self._m_trigger_type = KaitaiStream.resolve_enum(Scdms.TriggerTypes, (self.packed_2 & 15))
            return getattr(self, '_m_trigger_type', None)

        @property
        def readout_bitmask(self):
            if hasattr(self, '_m_readout_bitmask'):
                return self._m_readout_bitmask

            self._m_readout_bitmask = ((self.packed_2 & 4294967040) >> 8)
            return getattr(self, '_m_readout_bitmask', None)

        @property
        def event_size(self):
            if hasattr(self, '_m_event_size'):
                return self._m_event_size

            self._m_event_size = (self.packed_1 & 268435455)
            return getattr(self, '_m_event_size', None)

        @property
        def trig_header(self):
            if hasattr(self, '_m_trig_header'):
                return self._m_trig_header

            self._m_trig_header = KaitaiStream.resolve_enum(Scdms.Headers, ((self.packed_1 & 4026531840) >> 28))
            return getattr(self, '_m_trig_header', None)


    class Trailer(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.packed = self._io.read_u4le()

        @property
        def n_preceeding_triggers(self):
            if hasattr(self, '_m_n_preceeding_triggers'):
                return self._m_n_preceeding_triggers

            self._m_n_preceeding_triggers = (self.packed & 268435455)
            return getattr(self, '_m_n_preceeding_triggers', None)

        @property
        def trailer_header(self):
            if hasattr(self, '_m_trailer_header'):
                return self._m_trailer_header

            self._m_trailer_header = KaitaiStream.resolve_enum(Scdms.Headers, ((self.packed & 4026531840) >> 28))
            return getattr(self, '_m_trailer_header', None)


    class Primitive(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.packed_1 = self._io.read_u4le()
            self.ut = self._io.read_u4le()
            self.packed_2 = self._io.read_u4le()
            self.rt_run_time = self._io.read_u2le()
            self.trig_time = self._io.read_u2le()
            self.packed_3 = self._io.read_u4le()
            self.peak_amplitude = self._io.read_u2le()
            self.trig_word = self._io.read_u2le()

        @property
        def rt_time_fraction(self):
            if hasattr(self, '_m_rt_time_fraction'):
                return self._m_rt_time_fraction

            self._m_rt_time_fraction = (self.packed_2 & 16777215)
            return getattr(self, '_m_rt_time_fraction', None)

        @property
        def pileup(self):
            if hasattr(self, '_m_pileup'):
                return self._m_pileup

            self._m_pileup = ((self.packed_1 & 3072) >> 10)
            return getattr(self, '_m_pileup', None)

        @property
        def det_id(self):
            if hasattr(self, '_m_det_id'):
                return self._m_det_id

            self._m_det_id = ((self.packed_1 & 1020) >> 2)
            return getattr(self, '_m_det_id', None)

        @property
        def trig_time_fraction(self):
            if hasattr(self, '_m_trig_time_fraction'):
                return self._m_trig_time_fraction

            self._m_trig_time_fraction = (self.packed_3 & 16777215)
            return getattr(self, '_m_trig_time_fraction', None)

        @property
        def mask_pairs(self):
            if hasattr(self, '_m_mask_pairs'):
                return self._m_mask_pairs

            self._m_mask_pairs = ((self.packed_3 & 4278190080) >> 24)
            return getattr(self, '_m_mask_pairs', None)

        @property
        def index(self):
            if hasattr(self, '_m_index'):
                return self._m_index

            self._m_index = (self.packed_1 & 3)
            return getattr(self, '_m_index', None)

        @property
        def trig_status(self):
            if hasattr(self, '_m_trig_status'):
                return self._m_trig_status

            self._m_trig_status = ((self.packed_1 & 61440) >> 12)
            return getattr(self, '_m_trig_status', None)

        @property
        def prim_dcrc_header(self):
            if hasattr(self, '_m_prim_dcrc_header'):
                return self._m_prim_dcrc_header

            self._m_prim_dcrc_header = KaitaiStream.resolve_enum(Scdms.Headers, ((self.packed_1 & 4026531840) >> 28))
            return getattr(self, '_m_prim_dcrc_header', None)


    class VOneTrigger(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.trigger_meta = Scdms.VOneTrigMeta(self._io, self, self._root)
            self.n_primitives = []
            for i in range(self.trigger_meta.num_primitives):
                self.n_primitives.append(Scdms.Primitive(self._io, self, self._root))

            self.packed = self._io.read_u4le()
            self.n_detectors = []
            for i in range(self.detectors_in_event):
                self.n_detectors.append(Scdms.Detector(self._io, self, self._root))


        @property
        def detectors_in_event(self):
            if hasattr(self, '_m_detectors_in_event'):
                return self._m_detectors_in_event

            self._m_detectors_in_event = (self.packed & 268435455)
            return getattr(self, '_m_detectors_in_event', None)

        @property
        def det_header(self):
            if hasattr(self, '_m_det_header'):
                return self._m_det_header

            self._m_det_header = KaitaiStream.resolve_enum(Scdms.Headers, ((self.packed & 4026531840) >> 28))
            return getattr(self, '_m_det_header', None)


    class DetMeta(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.packed_1 = self._io.read_u4le()
            self.dcrc0_version = self._io.read_u1()
            self.dcrc0_serial_num = self._io.read_u1()
            self.dcrc1_version = self._io.read_u1()
            self.dcrc1_serial_num = self._io.read_u1()
            self.packed_2 = self._io.read_u4le()
            self.packed_3 = self._io.read_u4le()
            self.packed_4 = self._io.read_u4le()

        @property
        def readout_header(self):
            if hasattr(self, '_m_readout_header'):
                return self._m_readout_header

            self._m_readout_header = KaitaiStream.resolve_enum(Scdms.Headers, ((self.packed_2 & 4026531840) >> 28))
            return getattr(self, '_m_readout_header', None)

        @property
        def series_time_fraction(self):
            if hasattr(self, '_m_series_time_fraction'):
                return self._m_series_time_fraction

            self._m_series_time_fraction = (self.packed_3 & 16777215)
            return getattr(self, '_m_series_time_fraction', None)

        @property
        def num_channels_to_follow(self):
            if hasattr(self, '_m_num_channels_to_follow'):
                return self._m_num_channels_to_follow

            self._m_num_channels_to_follow = (self.packed_4 & 268435455)
            return getattr(self, '_m_num_channels_to_follow', None)

        @property
        def det_id(self):
            if hasattr(self, '_m_det_id'):
                return self._m_det_id

            self._m_det_id = ((self.packed_1 & 1020) >> 2)
            return getattr(self, '_m_det_id', None)

        @property
        def det_type(self):
            if hasattr(self, '_m_det_type'):
                return self._m_det_type

            self._m_det_type = ((self.packed_1 & 268434432) >> 10)
            return getattr(self, '_m_det_type', None)

        @property
        def index(self):
            if hasattr(self, '_m_index'):
                return self._m_index

            self._m_index = (self.packed_1 & 3)
            return getattr(self, '_m_index', None)

        @property
        def dcrc_header(self):
            if hasattr(self, '_m_dcrc_header'):
                return self._m_dcrc_header

            self._m_dcrc_header = KaitaiStream.resolve_enum(Scdms.Headers, ((self.packed_1 & 4026531840) >> 28))
            return getattr(self, '_m_dcrc_header', None)

        @property
        def channel_header(self):
            if hasattr(self, '_m_channel_header'):
                return self._m_channel_header

            self._m_channel_header = KaitaiStream.resolve_enum(Scdms.Headers, ((self.packed_4 & 4026531840) >> 28))
            return getattr(self, '_m_channel_header', None)

        @property
        def series_time(self):
            if hasattr(self, '_m_series_time'):
                return self._m_series_time

            self._m_series_time = (self.packed_2 & 65535)
            return getattr(self, '_m_series_time', None)

        @property
        def readout_status(self):
            if hasattr(self, '_m_readout_status'):
                return self._m_readout_status

            self._m_readout_status = ((self.packed_2 & 268369920) >> 16)
            return getattr(self, '_m_readout_status', None)



