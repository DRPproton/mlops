if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test

from sklearn.feature_extraction import DictVectorizer
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

@transformer
def transform(data, *args, **kwargs):
    
    dv = DictVectorizer()
    categorical = ['PULocationID', 'DOLocationID']
    numerical = ['trip_distance']

    data[categorical] = data[categorical].astype(str)

    train_dicts  = data[categorical].to_dict(orient='records')
    X_train = dv.fit_transform(train_dicts)

    lr = LinearRegression()
    y_train = data.duration

    model = lr.fit(X_train, y_train)
    print(model.intercept_)

    return model, dv


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'