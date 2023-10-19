from cnnClassifier.constants import *
import os
from cnnClassifier.utils.common import read_yaml, create_directories, save_json
from cnnClassifier.entity.config_entity import (DataInjestionConfig, PrepareBaseModelConfig, TrainingConfig, EvaluationConfig)


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
    


    def get_prepare_base_model(self)->PrepareBaseModelConfig:
        config = self.config.prepare_base_model

        create_directories([config.root_dir])

        prepare_base_model_config = PrepareBaseModelConfig(
            root_dir=Path(config.root_dir),
            base_model_path= Path(config.base_model_path),
            updated_base_model_path=Path(config.updated_base_model_path),
            params_image_size= self.params.IMAGE_SIZE,
            params_weights= self.params.WEIGHT,
            params_include_top= self.params.INCLUDE_TOP,
            params_learning_rate = self.params.LEARNING_RATE,
            params_classes = self.params.CLASSES
            
        )
        
        return prepare_base_model_config


    def get_training_config(self)->TrainingConfig:
        training = self.config.training
        prepare_base_model = self.config.prepare_base_model
        params = self.params
        training_data = os.path.join(self.config.data_injestion.unzip_dir, "CT-KIDNEY-DATASET-Normal-Cyst-Tumor-Stone")
        create_directories([
            Path(training.root_dir)
        ])

        training_config = TrainingConfig(
            root_dir=Path(training.root_dir),
            trained_model_path= Path(training.trained_model_path),
            updated_base_model_path= Path(prepare_base_model.updated_base_model_path),
            training_data= Path(training_data),
            params_epochs= params.EPOCH,
            params_batch_size= params.BATCH_SIZE,
            params_image_size= params.IMAGE_SIZE,
            params_is_augmentation= params.AUGMENTATION
            
            )
        
        return training_config
    
    def get_evaluation_config(self) -> EvaluationConfig:
        eval_config = EvaluationConfig(
            path_of_model="artifacts/training/model.h5",
            training_data="artifacts/data_injestion/CT-KIDNEY-DATASET-Normal-Cyst-Tumor-Stone",
            mlflow_uri="https://dagshub.com/bivas16/kidney_classification_deep-learnig.mlflow",
            all_params=self.params,
            params_image_size=self.params.IMAGE_SIZE,
            params_batch_size=self.params.BATCH_SIZE
        )
        return eval_config

