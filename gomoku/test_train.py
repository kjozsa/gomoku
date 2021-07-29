from gomoku.trainer import train


def test_train():
    train('../trained/test.h5', batch_size=2, sample_size=5)


def test_train_gomoku_model():
    train('../trained/gomoku2.h5', batch_size=1, sample_size=100)
