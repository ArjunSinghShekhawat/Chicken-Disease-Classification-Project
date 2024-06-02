from src.logger import logging
from src.exception import CustomeException
import sys
from src.pipeline.stage_01_data_ingestion_pipeline import DataIngestionTrainingPipeline


STAGE_NAME = "Data ingestion Stage"

if __name__=="__main__":
    try:
        logging.info(f">>>>>>>>>{STAGE_NAME}<<<<<<<<<<<")
        obj = DataIngestionTrainingPipeline()
        obj.main()
        logging.info(f">>>>>>>>>>>{STAGE_NAME} Completed <<<<<<<<<<<<")
    except Exception as e:
        raise CustomeException(e,sys)