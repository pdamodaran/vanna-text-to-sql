from src.database_trainer import DatabaseTrainer
import config


############################################################################################
# NOTE: To execute this code, you will need to create a file called config.py that defines
# the following constants (refer to the `sample_config.py` file for an example):
#   - VANNA_API_KEY
#   - MODEL
#   - POSTGRES_HOST
#   - POSTGRES_PORT
#   - POSTGRES_USER
#   - POSTGRES_PWD
#   - POSTGRES_DB
#   - DDL
############################################################################################

db_creds = {
    "host": config.POSTGRES_HOST,
    "port": config.POSTGRES_PORT,
    "user": config.POSTGRES_USER,
    "password": config.POSTGRES_PWD,
    "dbname": config.POSTGRES_DB,
}
database_trainer = DatabaseTrainer(
    api_key=config.VANNA_API_KEY, model=config.MODEL, db_creds=db_creds
)
database_trainer.train(ddl=config.DDL)
