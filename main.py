from cnnClassifier import logger
from cnnClassifier.pipeline.stage_01_data_injestion import DataInjestionTrainingPipeline
from cnnClassifier.pipeline.stage_02_prepare_base_model import PrepareBaseModelTrainingPipeline

STAGE_NAME = "Data Injestion Stage"

try:
        logger.info(f"<<<< {STAGE_NAME} has started >>>>>")
        obj = DataInjestionTrainingPipeline()
        obj.main()
        logger.info(f"{STAGE_NAME} is completed")
except Exception as e:
        logger.exception(e)
        raise e


STAGE_NAME="Prepare base model"

try:
        logger.info(f"<<<< {STAGE_NAME} has started >>>>>")
        obj = PrepareBaseModelTrainingPipeline()
        obj.main()
        logger.info(f"{STAGE_NAME} is completed")
except Exception as e:
        logger.exception(e)
        raise e


    