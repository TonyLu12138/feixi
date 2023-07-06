#! /usr/bin/env python3

import re

data = """
  /dev/sdk: open failed: No medium found
  /dev/sdl: open failed: No medium found
  /dev/sdn: open failed: No medium found
  /dev/drbd1006: open failed: Wrong medium type
  /dev/drbd1012: open failed: Wrong medium type
  /dev/sdk: open failed: No medium found
  /dev/sdl: open failed: No medium found
  /dev/sdn: open failed: No medium found
  /dev/drbd1006: open failed: Wrong medium type
  /dev/drbd1012: open failed: Wrong medium type
  WARNING: Device /dev/sdj has size of 1953525168 sectors which is smaller than corresponding PV size of 21485322240 sectors. Was device resized?
  WARNING: One or more devices used as PVs in VG vg_raidtest have changed sizes.
  LV Path                /dev/thickpool-n0/r2_00000
  LV Name                r2_00000
"""

lv_path = re.search(r'LV Path\s+(\/.+)', data)

if lv_path:
    lv_path_value = lv_path.group(1)
    print("LV Path:", lv_path_value)
else:
    print("LV Path not found.")
