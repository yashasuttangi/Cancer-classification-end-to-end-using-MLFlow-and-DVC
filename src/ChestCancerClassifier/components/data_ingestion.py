import os 
import zipfile
import gdown 
from ChestCancerClassifier import logger 
from ChestCancerClassifier.utils.common import get_size
from ChestCancerClassifier.entity.config_entity import DataIngestionConfig

class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config 

    def download_data(self) -> str:
        '''
        Fetch data from the URL 
        '''
        try:
            dataset_url = self.config.source_URL
            zip_download_dir = self.config.local_data_file
            os.makedirs("artifacts/data_ingestion", exist_ok=True)
            logger.info(f"Downloading data from {dataset_url} into file {zip_download_dir}")
            file_id = dataset_url.split("/")[-2]
            prefix = "https://drive.google.com/uc?/export=download&id="
            gdown.download(prefix + file_id, zip_download_dir, quiet=False)
            logger.info(f"Downloaded data successfully!")
        except Exception as e:
            raise e
        
    def extract_zip_file(self):
        '''
        Extract zip file into the data directory
        '''
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            logger.info(f"Extracting zip file: {self.config.local_data_file} into dir: {unzip_path}")
            zip_ref.extractall(unzip_path)
        logger.info(f"Extracted zip file successfully into dir: {unzip_path}")