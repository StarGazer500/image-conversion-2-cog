# Drone Imagery Tiling Tools

Python scripts for merging drone image tiles and converting them to Cloud-Optimized GeoTIFFs (COG) using GDAL.

## Scripts

### [merge_individual_tiles_to_single_cog.py](merge_individual_tiles_to_single_cog.py)

Merges a folder of individual drone image tiles into a single COG.

**Workflow:**
1. Scans a folder for `.tif` files and writes paths to `filelist.txt`
2. Builds a VRT mosaic from the file list (fast, no data copying)
3. Converts the VRT directly to a COG with DEFLATE compression

**To use:** Edit the `folder` and `output` variables at the top of the script, then run:
```bash
python merge_individual_tiles_to_single_cog.py
```

### [convert_single_image_to_single_cog.py](convert_single_image_to_single_cog.py)

Converts a single existing GeoTIFF to COG format.

**To use:** Edit the `input_tif` and `output_cog` variables at the top of the script, then run:
```bash
python convert_single_image_to_single_cog.py
```

## Output files

| File | Description |
|------|-------------|
| `*_merged.tif` | Merged COG output for each survey area |
| `mosaic.vrt` | Intermediate VRT mosaic (auto-generated) |
| `filelist.txt` | Intermediate tile path list (auto-generated) |

## Requirements

- Python 3
- GDAL command-line tools (`gdalbuildvrt`, `gdal_translate`) available on PATH

## Running the scripts

### Standalone (OSGeo4W shell or any environment with GDAL)
```bash
python merge_individual_tiles_to_single_cog.py
```

### QGIS Python Console
Open the QGIS Python Console (**Plugins > Python Console**) and run:
```python
exec(open(r"C:\Users\LENOVO\Desktop\tiling\merge_individual_tiles_to_single_cog.py").read())
```

GDAL is bundled with QGIS via OSGeo4W, so no separate GDAL installation is needed when running inside the QGIS environment.

## COG settings

Both scripts use the following settings:
- **Format:** COG (Cloud-Optimized GeoTIFF)
- **Compression:** DEFLATE
- **Data type:** Byte (8-bit)
- **Overview resampling:** AVERAGE
- **Threading:** All available CPUs
- **BIGTIFF:** YES (supports files >4 GB)
