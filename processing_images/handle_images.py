from processing_images.dataset_config import CLAHEConfig, BlurConfig, ThresholdConfig

import cv2 as cv
import numpy as np
import numpy.typing as npt
from pathlib import Path


def read_images(
    image: Path
) -> npt.NDArray[np.uint8]:
    read_image = (cv.imread(str(image), cv.IMREAD_GRAYSCALE)).astype(dtype = np.uint8)

    return read_image

def check_image_type(
    image: npt.NDArray[np.uint8]
) -> npt.NDArray[np.uint8]:
    
    if image.dtype != np.uint8:
        print(f"Warning: Input image dtype is {image.dtype}, converting to uint8")
        image = image.astype(np.uint8)

    if len(image.shape) == 3:
        if image.shape[2] == 3:
            print("Warning: Image given appears to be in colour, converting to grayscale")
            image = (cv.cvtColor(image, cv.COLOR_BGR2GRAY)).astype(np.uint8)
        if image.shape[2] == 4:
            print("Warning: Image appears to be in alpha, converting to grayscale")
            image = (cv.cvtColor(image, cv.COLOR_BGRA2GRAY)).astype(np.uint8)

    if len(image.shape) > 2 and image.shape[2] > 1:
        raise ValueError("Input image must be grayscale or convertible to grayscale")
    
    return image

def apply_threshold(
    image: npt.NDArray[np.uint8],

    clahe_config: CLAHEConfig,
    blur_config: BlurConfig,
    threshold_config: ThresholdConfig
) -> npt.NDArray[np.uint8]:
    
    clahe: cv.CLAHE = cv.createCLAHE(
        clipLimit= clahe_config.clip_limit, 
        tileGridSize=clahe_config.tile_grid_size
    )

    contrast_enhanced: npt.NDArray[np.uint8] = np.array(clahe.apply(image), dtype=np.uint8)

    blurred: npt.NDArray[np.uint8] = np.array(cv.GaussianBlur(contrast_enhanced, blur_config.kernel_size, 0), dtype=np.uint8)

    _, otsu_thresholded = cv.threshold(
        blurred, 0, 255, threshold_config.method    
    )

    return otsu_thresholded.astype(dtype=np.uint8)

def write_images(
    image_path: Path,
    image: npt.NDArray[np.uint8]
) -> None: 
    cv.imwrite(str(image_path), image)
