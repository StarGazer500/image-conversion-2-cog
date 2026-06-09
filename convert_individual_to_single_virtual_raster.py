import subprocess
import glob
import os

# --- Configuration ---
# Option A: point to a folder and all .tif files inside will be used
tiles_folder = r"D:\image_coregistration\raw_images\April_tiles"


# Output VRT path
output_vrt = r"D:\image_coregistration\raw_images\April_mosaic.vrt"
# ---------------------


# else:
tiles = sorted(glob.glob(os.path.join(tiles_folder, "*.tif")))
if not tiles:
    print(f"No .tif files found in: {tiles_folder}")
    raise SystemExit(1)
print(f"Building VRT from {len(tiles)} tiles in: {tiles_folder}")
cmd = ["gdalbuildvrt", output_vrt] + tiles



subprocess.run(cmd, check=True)
print(f"Done! VRT saved to: {output_vrt}")
