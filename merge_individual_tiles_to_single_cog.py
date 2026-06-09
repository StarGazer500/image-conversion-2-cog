import subprocess, glob

folder = r"C:\Users\LENOVO\Rainforest Builder Dropbox\05_RB SL - All team\05_Planning\01_Spatial\01_Drone Imagery\01_Chiefdom\01_Fakunya\2026\FAK_PROPOSED_S03-03-26_E12-03-26_R40"
tiles = glob.glob(folder + r"\*.tif")
vrt = r"C:\Users\LENOVO\Desktop\tiling\mosaic.vrt"
output = r"C:\Users\LENOVO\Desktop\tiling\fukunya_proposed.tif"

# Step 1 - build VRT (instant, no copying)
with open(r"C:\Users\LENOVO\Desktop\tiling\filelist.txt", "w") as f:
    f.write("\n".join(tiles))

subprocess.run(["gdalbuildvrt", "-input_file_list", 
                r"C:\Users\LENOVO\Desktop\tiling\filelist.txt", vrt])

# Step 2 - convert VRT directly to COG (multithreaded)
subprocess.run([
    "gdal_translate",
    vrt, output,
    "-of", "COG",
    "-co", "COMPRESS=DEFLATE",
    "-co", "LEVEL=9",
    "-co", "PREDICTOR=2",
    "-co", "BLOCKSIZE=512",
    "-co", "NUM_THREADS=ALL_CPUS",
    "-co", "BIGTIFF=YES",
    "-co", "OVERVIEWS=AUTO",
    "-co", "OVERVIEW_RESAMPLING=AVERAGE",
    "-ot", "Byte"
])