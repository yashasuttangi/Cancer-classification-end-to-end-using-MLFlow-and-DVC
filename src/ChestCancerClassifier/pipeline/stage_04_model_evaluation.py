from ChestCancerClassifier.config.configuration import ConfigurationManager
from ChestCancerClassifier import logger
from ChestCancerClassifier.components.model_evaluation_mlflow import Evaluation 

STAGE_NAME = "Model Evaluation Stage"

class EvaluationPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        eval_config = config.get_evaluation_config()
        evaluation = Evaluation(eval_config)
        evaluation.evaluation()
        evaluation.save_score()
        # evaluation.log_into_mlflow()

if __name__ == "__main__":
    try:
        logger.info(">>>>>>>>>> {STAGE_NAME} started <<<<<<<<<<")
        obj = EvaluationPipeline()
        obj.main()
        logger.info(">>>>>>>>>> {STAGE_NAME} completed <<<<<<<<<<\n\nx")
    except Exception as e:
        logger.exception(e)
        raise e