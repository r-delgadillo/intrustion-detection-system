# from azureml.core import Workspace, Dataset
# from glob import glob

# import pandas as pd

# subscription_id = '820b737c-cdd7-46bf-9ead-f144ba6e9d1e'
# resource_group = 'SIE-AZ-ML'
# workspace_name = 'IDS'

# workspace = Workspace(subscription_id, resource_group, workspace_name)

# dataset = Dataset.get_by_name(workspace, name='CIC-IDS-2018')
# dataset.to_pandas_dataframe()


import pandas as pd
from glob import glob

# DataFrame: df
file_names = [
    'F:\\Data\\Friday-23-02-2018_TrafficForML_CICFlowMeter.csv',
    'F:\\Data\\Friday-23-02-2018_TrafficForML_CICFlowMeter.csv',
    'F:\\Data\\Friday-23-02-2018_TrafficForML_CICFlowMeter.csv'
]
data_frames = []

print('Reading files')
for f in file_names:
    print('Starting file' + f)
    data_frames.append(pd.read_csv(f))
    # data_frames = [pd.read_csv(f) for f in files_names]
    print('Success')

