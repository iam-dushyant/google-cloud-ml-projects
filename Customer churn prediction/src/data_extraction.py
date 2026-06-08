from google.cloud import storage
from io import StringIO
import pandas as pd


class DataLoader:

    def __init__(
        self,
        project_id: str,
        bucket_name: str
    ):
        self.project_id = project_id
        self.bucket_name = bucket_name

        self.storage_client = storage.Client(
            project=project_id
        )

        self.bucket = self.storage_client.bucket(
            bucket_name
        )

    def load_csv(
        self,
        blob_name: str
    ) -> pd.DataFrame:

        blob = self.bucket.blob(blob_name)

        csv_data = blob.download_as_text()

        df = pd.read_csv(
            StringIO(csv_data)
        )

        return df


if __name__ == "__main__":

    PROJECT_ID = "pmle-exam-prep"
    BUCKET_NAME = "pmle-project-1"

    loader = DataLoader(
        project_id=PROJECT_ID,
        bucket_name=BUCKET_NAME
    )

    df = loader.load_csv(
        "Customer_churn_dataset/raw_data.csv"
    )

    print(df.head())
    print(f"Rows: {len(df)}")