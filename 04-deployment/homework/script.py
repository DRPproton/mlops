import pickle
import pandas as pd
import sys
import numpy as np

with open('model.bin', 'rb') as f_in:
    dv, model = pickle.load(f_in)




def read_data(filename: str, year, month):
    df = pd.read_parquet(filename)
    
    df['duration'] = df.tpep_dropoff_datetime - df.tpep_pickup_datetime
    df['duration'] = df.duration.dt.total_seconds() / 60

    df = df[(df.duration >= 1) & (df.duration <= 60)].copy()

    df['ride_id'] = f'{year:04d}/{month:02d}_' + df.index.astype('str')
    
    return df


def prepare_and_predict(df: pd.DataFrame):
    categorical = ['PULocationID', 'DOLocationID']
    df[categorical] = df[categorical].fillna(-1).astype('int').astype('str')

    dicts = df[categorical].to_dict(orient='records')
    X_val = dv.transform(dicts)
    y_pred = model.predict(X_val)

    return y_pred


def run():
    # taxi_type = sys.argv[1] # 'yellow'
    year = sys.argv[1]# 2021
    month = sys.argv[2] # 3
    year = int(year)
    month = int(month)
 

    df = read_data(f'https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_{year:04d}-{month:02d}.parquet'
                   , year, month)



    df['pred'] = prepare_and_predict(df)


    df_result = df[['ride_id', 'pred']]

    print(np.mean(df_result.pred))

    """df_result.to_parquet(
        'data_with_pred',
        engine='pyarrow',
        compression=None,
        index=False
    )"""


if __name__ == '__main__':
    run()