from cnnClassifier import logger
from cnnClassifier.pipeline.stage_01_data_injestion import DataInjestionTrainingPipeline

STAGE_NAME = "Data Injestion Stage"

try:
        logger.info(f"<<<< {STAGE_NAME} has started >>>>>")
        obj = DataInjestionTrainingPipeline()
        obj.main()
        logger.info(f"{STAGE_NAME} is completed")
except Exception as e:
        logger.exception(e)
        raise e
    