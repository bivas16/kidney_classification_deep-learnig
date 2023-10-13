from cnnClassifier.constants import *
import os
from cnnClassifier.utils.common import read_yaml, create_directories
from cnnClassifier.entity.config_entity import DataInjestionConfig

class ConfigurationManager:
    def __init__(self,config_file_path= CONFIG_FILE_PATH,params_file_path= PARAMS_FILE_PATH):
        self.config = read_yaml(config_file_path)
        self.params = read_yaml(params_file_path)

        create_directories([self.config.artifacts_root])

    def get_data_injestion_config(self) -> DataInjestionConfig:
        config = self.config.data_injestion

        create_directories([config.root_directory])

        data_injestion_config = DataInjestionConfig(
                root_dir= config.root_directory,
                source_URL= config.source_URL,
                local_data_file= config.local_data_file,
                unzip_dir= config.unzip_dir
            )
        
        return data_injestion_config