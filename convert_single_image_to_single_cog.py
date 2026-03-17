import subprocess

input_tif = r"C:\Users\LENOVO\Desktop\tiling\output.tif"
output_cog = r"C:\Users\LENOVO\Desktop\tiling\output_cog.tif"

subprocess.run([
    "gdal_translate",
    input_tif, output_cog,
    "-of", "COG",
    "-ot", "Byte",
    "-co", "COMPRESS=DEFLATE",
    "-co", "NUM_THREADS=ALL_CPUS",
    "-co", "BIGTIFF=YES",
    "-co", "OVERVIEW_RESAMPLING=AVERAGE"
])

print("Done!")