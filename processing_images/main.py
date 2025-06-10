from processing_images.handle_images import apply_threshold, read_images, check_image_type, write_images
from processing_images.dataset_config import CLAHEConfig, BlurConfig, ThresholdConfig, FOLDER_PATH

import numpy as np
import numpy.typing as npt
from pathlib import Path
import sys

def ensure_output_config(folder: Path):
    try:
        folder.mkdir(parents = True, exist_ok=True)
    except OSError as e:
        print(f'Error creating output folder {folder}: {e}', file=sys.stderr)

def preprocess_image(
    image_path: Path, 
    clahe_params: CLAHEConfig, 
    blur_params: BlurConfig, 
    threshold_params: ThresholdConfig
) -> npt.NDArray[np.uint8]:
    raw_image = read_images(image_path)
    raw_image = check_image_type(raw_image)
    processed_image = apply_threshold(
        raw_image,
        clahe_params,
        blur_params,
        threshold_params
    )
    return processed_image

def save_image(
    image_path: Path, 
    image: npt.NDArray[np.uint8]
) -> None:
    try:
        write_images(image_path, image)
    except Exception as e:
        print(f"Error saving image to {image_path}: {e}", file=sys.stderr)

def image_pipeline(
    raw_folder: Path,
    output_folder: Path,
    clahe_params: CLAHEConfig, 
    blur_params: BlurConfig, 
    threshold_params: ThresholdConfig 
) -> None:
    
    for image_path in raw_folder.glob("*.png"):
        processed_img = preprocess_image(
            image_path, 
            clahe_params, 
            blur_params, 
            threshold_params
        )

        if processed_img.size > 0:
            output_path = output_folder / image_path.name
            save_image(output_path, processed_img)
        else:
            print(f"Skipping saving for {image_path.name} due to processing errors.", file=sys.stderr)

if __name__ == '__main__':
    clahe_params = CLAHEConfig()
    blur_params = BlurConfig()
    threshold_params = ThresholdConfig()

    try:
        raw_forged_folder = FOLDER_PATH["raw_forged_folder"]
        output_forged_folder = FOLDER_PATH["output_forged_folder"]
        raw_original_folder = FOLDER_PATH["raw_original_folder"]
        output_original_folder = FOLDER_PATH["output_original_folder"]
    except KeyError as e:
        print(f"Configuration error: Missing folder path key {e} in FOLDER_PATH", file=sys.stderr)
        sys.exit(1)

    output_forged_folder.mkdir(parents = True, exist_ok = True)
    output_original_folder.mkdir(parents = True, exist_ok = True)

    image_pipeline(raw_forged_folder,
                    output_forged_folder, 
                    clahe_params, 
                    blur_params, 
                    threshold_params
                    )
    image_pipeline(raw_original_folder, output_original_folder, clahe_params, blur_params, threshold_params)
    


