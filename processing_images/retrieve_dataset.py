import kagglehub
from CONFIG import DATASET_KAGGLE_CONFIG

# Downloading dataset from kaggle
path = kagglehub.dataset_download(
    handle = DATASET_KAGGLE_CONFIG["cedar_dataset"]
)

print(f"Dataset at: {path}")