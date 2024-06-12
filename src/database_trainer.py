from vanna.remote import VannaDefault

INFO_SCHEMA_QUERY = "SELECT * FROM INFORMATION_SCHEMA.COLUMNS"


class DatabaseTrainer:
    """
    DatabaseTrainer uses Vanna AI to learn in the internals of a Postgres database
    to enable users to use natural language to generate and execute SQL queries
    """

    def __init__(self, api_key=None, model=None, db_creds=None):
        """
        Parameters
        ----------
        api_key : string
            The API key used to connect to Vanna AI

        model : string
            The name of the model that will be trained; the model needs
            to be set up in your Vanna AI account prior to use

        db_creds : dict
            Credentials to connect to a Postgres database.  The dictionary
            must contain the following keys: host, port, user, password, dbname
        """
        if api_key is None or api_key == "":
            raise ValueError("api_key must be a valid non-empty string")
        if model is None or model == "":
            raise ValueError("model must be valid non-empty string")
        if db_creds is None:
            raise ValueError("db_creds must be a valid non-empty dictionary")
        # Initialize vanna
        self.vn = self._init_vanna(api_key=api_key, model=model)
        # Connect to the Postgres database
        self._connect_db(db_creds)

    def _init_vanna(self, api_key, model):
        """
        Initialize the VannaDefault class by using the API key to connect to
        the model set up in your Vanna AI account
        """
        vn = VannaDefault(api_key=api_key, model=model)
        return vn

    def _connect_db(self, db_creds):
        """
        Connect Vanna to the postgres database
        """
        self.vn.connect_to_postgres(
            host=db_creds["host"],
            port=db_creds["port"],
            user=db_creds["user"],
            password=db_creds["password"],
            dbname=db_creds["dbname"],
        )

    def train(self, ddl=None):
        """
        Train the model
        Parameters
        ----------
        ddl : string
            "CREATE TABLE" SQL statements of the tables in your database.
        """
        if ddl is None or ddl == "":
            raise ValueError("ddl must be a valid non-empty string")
        # query the information_schema to get the table and column information from the database
        db_info_schema = self.vn.run_sql(INFO_SCHEMA_QUERY)
        # break up the information schema into bite-sized chunks that will be referenced by the LLM
        plan = self.vn.get_training_plan_generic(db_info_schema)
        self.vn.train(plan=plan)
        self.vn.train(ddl=ddl)
        print("Training complete!")
