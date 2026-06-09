import subprocess

input_tif = r"C:\Users\LENOVO\Rainforest Builder Dropbox\03_RB Ghana - All Team\03_Planning\00_Spatial\04_Drone Imagery\01_Data\01_Forest Reserves\03_Anhwiaso South Compartment\2026\ASO_S21-04-26_E21-04-26_R53\your_file.tif"  # ← point to actual .tif file
output_cog = r"C:\Users\LENOVO\Desktop\image_coregistration\coregistration_output_ASO_S21-05-26_E21-05-26_R53\May_output_cog.tif"

subprocess.run([
    "gdal_translate",
    input_tif,          # ← input must be passed here
    output_cog,         # ← output must be passed here
    "-of", "COG",
    "-ot", "Byte",
    "-co", "COMPRESS=DEFLATE",
    "-co", "LEVEL=9",
    "-co", "PREDICTOR=2",
    "-co", "BLOCKSIZE=512",
    "-co", "NUM_THREADS=ALL_CPUS",
    "-co", "BIGTIFF=YES",
    "-co", "OVERVIEWS=AUTO",
    "-co", "OVERVIEW_RESAMPLING=AVERAGE"
])

print("Done!")