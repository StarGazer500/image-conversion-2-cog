import subprocess
import glob
import os

# --- Configuration ---
# Option A: point to a folder and all .tif files inside will be used
tiles_folder = r"C:\Users\LENOVO\Rainforest Builder Dropbox\05_RB SL - All team\05_Planning\01_Spatial\01_Drone Imagery\01_Chiefdom\01_Fakunya\2026\FAK_PROPOSED_S03-03-26_E12-03-26_R40"

# Option B: point to an existing filelist.txt (set to None to use Option A)
filelist = r"C:\Users\LENOVO\Desktop\tiling\filelist.txt"

# Output VRT path
output_vrt = r"C:\Users\LENOVO\Desktop\tiling\mosaic_new.vrt"
# ---------------------

if filelist and os.path.isfile(filelist):
    cmd = [
        "gdalbuildvrt",
        "-input_file_list", filelist,
        output_vrt,
    ]
    print(f"Building VRT from filelist: {filelist}")
else:
    tiles = sorted(glob.glob(os.path.join(tiles_folder, "*.tif")))
    if not tiles:
        print(f"No .tif files found in: {tiles_folder}")
        raise SystemExit(1)
    print(f"Building VRT from {len(tiles)} tiles in: {tiles_folder}")
    cmd = ["gdalbuildvrt", output_vrt] + tiles

subprocess.run(cmd, check=True)
print(f"Done! VRT saved to: {output_vrt}")
