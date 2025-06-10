import cv2 as cv
from typing import Dict, Tuple
from dataclasses import dataclass
from pathlib import Path

# Turn this into YAML

DATASET_KAGGLE_CONFIG: Dict[str, str] = {
    # Default is CEDAR dataset
    "cedar_dataset": "shreelakshmigp/cedardataset",
}

FOLDER_PATH: Dict[str, Path] = {
    "raw_forged_folder": Path("raw_signature_images/CEDAR/full_forg"),
    "raw_original_folder": Path("raw_signature_images/CEDAR/full_org"),
    "output_forged_folder": Path("processed_signature_images/CEDAR/forged"),
    "output_original_folder": Path("processed_signature_images/CEDAR/original")
}


@dataclass 
class CLAHEConfig:
    clip_limit: float = 2.0
    tile_grid_size: Tuple[int, int] = (8,8)

@dataclass
class BlurConfig:
    kernel_size: Tuple[int, int] = (5,5)

@dataclass
class ThresholdConfig:
    method: int = cv.THRESH_BINARY + cv.THRESH_OTSU