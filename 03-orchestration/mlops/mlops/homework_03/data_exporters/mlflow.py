
import mlflow
import pickle

if 'data_exporter' not in globals():
    from mage_ai.data_preparation.decorators import data_exporter


mlflow.set_tracking_uri("http://mlflow:5000")
mlflow.set_experiment("nyc-taxi-experiment")

@data_exporter
def export_data(data, *args, **kwargs):
    model, dv = data
    
    with mlflow.start_run():
        with open('lin_reg.bin', 'wb') as f_out:
            pickle.dump(dv, f_out)

        mlflow.log_artifact('lin_reg.bin')
        mlflow.sklearn.log_model(model, 'model')
    print('ok')
