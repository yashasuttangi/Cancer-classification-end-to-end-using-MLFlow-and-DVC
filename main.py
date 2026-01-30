from ChestCancerClassifier import logger 
from ChestCancerClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from ChestCancerClassifier.pipeline.stage_02_prepare_base_model import PrepareBaseModelTrainingPipeline
from ChestCancerClassifier.pipeline.stage_03_model_trainer import ModelTrainingPipeline
from ChestCancerClassifier.pipeline.stage_04_model_evaluation import EvaluationPipeline
import dagshub
import mlflow

STAGE_NAME = "Data Ingestion Stage"

try:
    logger.info(">>>>>>>>>> {STAGE_NAME} started <<<<<<<<<<")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(">>>>>>>>>> {STAGE_NAME} completed <<<<<<<<<<\n\nx")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Prepare Base Model"

try:
    logger.info(f"*****************")
    logger.info(f">>>>>>> stage {STAGE_NAME} started <<<<<<<<< ")
    prepare_base_model = PrepareBaseModelTrainingPipeline()
    prepare_base_model.main()
    logger.info(f">>>>>>>> stage {STAGE_NAME} completed <<<<<<<< \n \nx ==========x")
except Exception as e:
    logger.exception(e)
    raise e 

STAGE_NAME = "Training"
try:
    logger.info(f"*****************")
    logger.info(f">>>>>>>> stage {STAGE_NAME} started <<<<<<<")
    model_evaluation = ModelTrainingPipeline()
    model_evaluation.main()
    logger.info(f">>>>>>>> stage {STAGE_NAME} completed <<<<<<<")
except Exception as e:
    logger.exception(e)
    raise e 



dagshub.init(
    repo_owner="yashuttangi",
    repo_name="Cancer-classification-end-to-end-using-MLFlow-and-DVC",
    mlflow=True
)

mlflow.set_experiment("ChestCancerClassification")

STAGE_NAME = "Evaluation Stage"
try:
    logger.info(f"******************")
    logger.info(f">>>>>>>> stage {STAGE_NAME} started <<<<<<<<<")
    model_evaluation = EvaluationPipeline()
    model_evaluation.main()
    logger.info(f">>>>>>>>> stage {STAGE_NAME} completed <<<<<<<\n\nx========x")
except Exception as e:
    logger.exception(e)
    raise e 
