# MaskFusion
MaskFusion is a Python-based image processing tool designed to create precise and high-quality cutouts by combining mask images with original images.
---

# High-Quality Image Cutout Tool

This Python script processes images by combining mask files with original images to create high-quality cutouts. It leverages OpenCV to refine the cutout process by converting mask images to binary, aligning resolutions, and seamlessly merging them with the original images.

This tool is ideal for applications requiring precise background removal, such as photo editing, object segmentation, or creative content generation.

## Features

- Combines mask and original images for accurate cutouts.
- Automatically converts masks to binary format for better precision.
- Ensures resolution consistency between masks and original images.
- Produces high-quality output images with transparent or custom backgrounds.

---

## Workflow Overview

1. **Mask Processing**:
   - Converts mask images to grayscale and applies binary thresholding to ensure clear separation between foreground and background.

2. **Resolution Matching**:
   - Resizes original images to match the resolution of corresponding mask images.

3. **Image Blending**:
   - Uses the processed mask to remove the background from the original image, leaving only the foreground.

4. **Output Generation**:
   - Saves the final cutout images to the specified output folder.

---

## Requirements

- Python 3.7 or higher
- OpenCV (`cv2`)
- NumPy

### Installation

Install the required dependencies using the following command:

```bash
pip install opencv-python-headless numpy
```

---

## Usage

### Command Format

Run the script using the following command:

```bash
python change.py <mask_folder> <original_folder> <output_folder>
```

### Arguments

- `<mask_folder>`: Path to the folder containing mask images (e.g., `.png` format).
- `<original_folder>`: Path to the folder containing original images (e.g., `.jpg` format).
- `<output_folder>`: Path to the folder where processed cutout images will be saved.

### Example

```bash
python change.py ./masks ./originals ./outputs
```

This command processes all images in the `./masks` and `./originals` directories and saves the cutouts in the `./outputs` directory.

---

## Integration with MiVOS

This script relies on high-quality mask images to achieve optimal cutout results. We recommend using [MiVOS](https://github.com/hkchengrex/MiVOS) to generate mask files. MiVOS is a state-of-the-art object segmentation tool that can handle both static images and dynamic videos, producing accurate masks for seamless integration with this script.

---

## Directory Structure

Before running the script, ensure the directory structure is as follows:

```
project/
│
├── change.py               # The cutout script
├── masks/                  # Folder containing mask images
│   ├── 01.png
│   ├── 02.png
│   └── ...
├── originals/              # Folder containing original images
│   ├── 01.jpg
│   ├── 02.jpg
│   └── ...
└── outputs/                # Folder for processed cutout images
```

---

## Customization and Extension

1. **Adjust Cutout Precision**:
   - Modify the binary threshold value in the script (`cv2.threshold`) to adapt to different mask characteristics.

2. **Support Additional Formats**:
   - Extend the script to handle other file formats such as `.jpeg` or `.bmp` by updating the file extension filters.

3. **Transparent Backgrounds**:
   - Enhance the output to include transparent backgrounds by converting to RGBA format in OpenCV.

---

## Troubleshooting

### 1. No Output or Incorrect Results
- Ensure the filenames in the `mask_folder` and `original_folder` match.
- Verify that the file formats are correct (e.g., `.png` for masks and `.jpg` for originals).

### 2. Missing Dependencies
- Reinstall the required dependencies using:
  ```bash
  pip install opencv-python numpy
  ```

---

## Contributions

We welcome contributions! Feel free to submit issues or pull requests to improve this tool.

---

## License

This project is licensed under the [MIT License](LICENSE).

---

## Author

- [eddie-cui](https://github.com/eddie-cui)

