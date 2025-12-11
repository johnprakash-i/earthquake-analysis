import sys
import os

# Add project root to sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from config.db_config import DB_CONFIG
from sqlalchemy import create_engine
import pandas as pd


# Create engine using DB_CONFIG
engine = create_engine(
    f"mysql+pymysql://{DB_CONFIG['user']}:{DB_CONFIG['password']}@{DB_CONFIG['host']}/{DB_CONFIG['database']}"
)

# Load cleaned CSV
df = pd.read_csv("../data/cleaned_data.csv")

# Insert into MySQL
df.to_sql("earthquakes", con=engine, if_exists="append", index=False)

print("Data inserted successfully!")
