from app import predict


def test_predict():
    assert predict(5) == 10


def test_zero():
    assert predict(0) == 0