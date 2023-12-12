from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Horse, Race  # Replace 'models' with your actual module containing SQLAlchemy models
import pandas as pd
import glob

# Step 1: Database Connection
def connect_to_database():
    # Replace the connection string with your PostgreSQL details
    engine = create_engine('postgresql://username:password@localhost:5432/yourdatabase')
    Session = sessionmaker(bind=engine)
    return Session()

# Step 2: Data Import from .csv
def import_csv_to_database(session, folder_path):
    # Assuming two categories of spreadsheets: 'horse_data' and 'race_data'
    for category in ['horse_data', 'race_data']:
        category_path = f"{folder_path}/{category}/*.csv"
        files = glob.glob(category_path)

        for file in files:
            df = pd.read_csv(file)
            records = df.to_dict(orient='records')

            # Use the category name as the model name
            model_class = Horse if category == 'horse_data' else Race

            for record in records:
                session.add(model_class(**record))

            session.commit()

# Example Usage:
if __name__ == "__main__":
    session = connect_to_database()
    import_csv_to_database(session, '/path/to/csv/folder')
