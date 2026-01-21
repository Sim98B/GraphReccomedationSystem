import matplotlib.pyplot as plt
import logging
from utils.logger import setup_logging
from utils.Neo4jExecutor import Neo4jExecutor
import pandas as pd

setup_logging()
logger = logging.getLogger("EDA")

executor = Neo4jExecutor()
query = """
MATCH (u:User)-[r:RATED]->(w:Wine)
RETURN u.user_id AS user, w.name AS wine, r.rating AS rating
LIMIT 50
"""
query = """
MATCH (u:User)-[r:RATED]->(w:Wine)
RETURN r{.*}
LIMIT 5
"""
records = executor.run_query(query)
for r in records:
    print(r)