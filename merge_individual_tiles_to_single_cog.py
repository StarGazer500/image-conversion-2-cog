import subprocess, glob

folder = r"C:\Users\LENOVO\Rainforest Builder Dropbox\03_RB Ghana - All Team\03_Planning\00_Spatial\04_Drone Imagery\01_Data\01_Forest Reserves\08_Tano Suhien\2026\TS_S20-02-26_E22-02-26_R45"
tiles = glob.glob(folder + r"\*.tif")
vrt = r"C:\Users\LENOVO\Desktop\tiling\mosaic.vrt"
output = r"C:\Users\LENOVO\Desktop\tiling\tano_suhien.tif"

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
    "-co", "NUM_THREADS=ALL_CPUS",
    "-co", "BIGTIFF=YES",
    "-co", "OVERVIEW_RESAMPLING=AVERAGE",
    "-ot", "Byte"
])

print("Done!")