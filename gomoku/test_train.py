from gomoku.trainer import train


def test_train():
    train('../trained/test.h5', batch_size=2, sample_size=5)
