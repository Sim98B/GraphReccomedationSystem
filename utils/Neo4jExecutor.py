from dotenv import load_dotenv
import os
from neo4j import GraphDatabase
import logging
from utils.logger import setup_logging

setup_logging()
logger = logging.getLogger("NEO4J")

load_dotenv()
db_user = os.getenv("DB_USER")
db_password = os.getenv("DB_PASSWORD")
db_host = os.getenv("DB_HOST")
db_port = os.getenv("DB_PORT")
db_name = os.getenv("DB_NAME")

class Neo4jExecutor:
    def __init__(self):
        self._user = db_user
        self._password = db_password
        self._host = db_host
        self._port = db_port
        self._db = db_name
        self._uri = f"bolt://{self._host}:{self._port}"

        try:
            self._driver = GraphDatabase.driver(self._uri, auth=(self._user, self._password), encrypted=False)
            logger.info("Connected to Neo4j")
        except Exception as e:
            logger.exception("Failed to connect to Neo4j: %s", e)
            raise

    def close(self):
        """
        Closes connection to Neo4j
        """
        if self._driver:
            self._driver.close()
            logger.info("Closed Neo4j connection")

    def run_query(self, query: str, parameters: dict = None):
        """
        Executes query and returns results
        :param query: a string with query to execute
        :param parameters: query parameters
        :return: query results
        """
        parameters = parameters or {}
        try:
            with self._driver.session(database=self._db) as session:
                result = session.run(query, parameters)
                records = [record.data() for record in result]
                logger.debug("Executed query: %s | Params: %s", query, parameters)
                return records
        except Exception as e:
            logger.exception("Error executing query: %s", e)
            raise

"""
executor = Neo4jExecutor()

# Esempio: recupera tutti i vini di tipo "rosso"
query = "MATCH (w:Wine) WHERE w.type = $type RETURN w.name AS name, w.rating AS rating"
params = {"type": "rosso"}
records = executor.run_query(query, params)

for r in records:
    print(r)

executor.close()
"""

executor = Neo4jExecutor()

# Esempio: recupera tutti i vini di tipo "rosso"
query = "MATCH (w:Wine) WHERE w.type = $type RETURN w.name AS name, w.rating AS rating"
params = {"type": "rosso"}
records = executor.run_query(query, params)