from gomoku.trainer import train


def test_train():
    train('../trained/test.h5', '../trained/test2.h5', batch_size=5, sample_size=200, random=False)
