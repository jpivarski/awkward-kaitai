# Like this:

import kaitaistruct, scdms

obj = scdms.Scdms(kaitaistruct.KaitaiStream(open("../data/scdms_raw.bin", "rb")))

print(obj.scdms_footer.trailer_header.dcrc_hdr.waveform_hdr)
