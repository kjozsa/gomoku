from gomoku.trainer import train, load_or_create_model


def test_train():
    model = load_or_create_model('../trained/sqe-masked2.h5')
    train('../trained/sqe-masked2.h5', '../trained/sqe-masked3.h5', batch_size=50, sample_size=400, model_x=model, model_o=model)
