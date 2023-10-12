from cnnClassifier.config.configuration import ConfigurationManager
from cnnClassifier.components.data_injestion import DataInjestion
from cnnClassifier import logger

STAGE_NAME = "Data Injestion Stage"

class DataInjestionTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        data_injestion_config = config.get_data_injestion_config()
        data_injestion = DataInjestion(config=data_injestion_config)
        data_injestion.download_file()
        data_injestion.extract_zip_file()


if __name__ == '__main__':
    try:
        logger.info(f"<<<< {STAGE_NAME} has started >>>>>")
        obj = DataInjestionTrainingPipeline()
        obj.main()
        logger.info(f"{STAGE_NAME} is completed")
    except Exception as e:
        logger.exception(e)
        raise e
    