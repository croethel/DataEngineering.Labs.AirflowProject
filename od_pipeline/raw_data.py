import pandas as pd

class Raw:

    def import_raw_data():
        # Imports raw data and returns a DataFrame
        raw_data = pd.read_csv('/Users/roethelchristine/airflow/airflow/data/VSRR_Provisional_Drug_Overdose_Death_Counts.csv')
        data = pd.DataFrame(raw_data)
        return data