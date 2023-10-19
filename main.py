from cnnClassifier import logger
from cnnClassifier.pipeline.stage_01_data_injestion import DataInjestionTrainingPipeline
from cnnClassifier.pipeline.stage_02_prepare_base_model import PrepareBaseModelTrainingPipeline
from cnnClassifier.pipeline.stage_03_model_training import ModelTrainingPipeline
from cnnClassifier.pipeline.stage_04_model_evaluation import EvaluationPipeline

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



STAGE_NAME = "Training"
try: 
   logger.info(f"*******************")
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
   model_trainer = ModelTrainingPipeline()
   model_trainer.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e


STAGE_NAME = "Evaluation stage"

try:
        logger.info(f"*******************")
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = EvaluationPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e
