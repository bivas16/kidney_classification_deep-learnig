import os
import zipfile
import gdown
from cnnClassifier import logger
from cnnClassifier.utils.common import get_size
from cnnClassifier.entity.config_entity import DataInjestionConfig


class DataInjestion:
    def __init__(self, config:DataInjestionConfig):
        self.config = config
    
    def download_file(self) -> str:
        "Fetch DATA"

        try:
            dataset_url= self.config.source_URL
            zip_download_dir = self.config.local_data_file
            os.makedirs("artifacts/data_injestion", exist_ok=True)
            logger.info(f"Downloading data from {dataset_url} into file {zip_download_dir}")

            file_id = dataset_url.split("/")[-2]
            prefix =  "https://drive.google.com/uc?/export=download&id="
            gdown.download(prefix+file_id, zip_download_dir)

            logger.info(f"Downloaded data from {dataset_url} into {zip_download_dir}")

        except Exception as e:
            raise e
        
    def extract_zip_file(self):
        "Extractng the zip file into the data directory"

        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file, 'r') as f:
            f.extractall(unzip_path) 