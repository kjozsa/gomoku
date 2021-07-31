from gomoku.trainer import train, load_or_create_model


def test_train():
    model_x = load_or_create_model('../trained/sqe-masked2.h5')
    model_o = load_or_create_model('../trained/sqe-masked3.h5')

    train('../trained/sqe-masked3.h5', '../trained/sqe-masked3.h5', batch_size=2, sample_size=2)  # , model_x=model, model_o=model
    train('../trained/sqe-masked3.h5', '../trained/sqe-masked3.h5', batch_size=2, sample_size=2, model_x=model_x, model_o=model_o)

    train('../trained/sqe-masked3.h5', '../trained/sqe-masked3.h5', batch_size=60, sample_size=400)  # , model_x=model, model_o=model
    train('../trained/sqe-masked3.h5', '../trained/sqe-masked3.h5', batch_size=60, sample_size=400, model_x=model_x, model_o=model_o)

    train('../trained/sqe-masked3.h5', '../trained/sqe-masked3.h5', batch_size=60, sample_size=400)  # , model_x=model, model_o=model
    train('../trained/sqe-masked3.h5', '../trained/sqe-masked3.h5', batch_size=60, sample_size=400, model_x=model_x, model_o=model_o)

    train('../trained/sqe-masked3.h5', '../trained/sqe-masked3.h5', batch_size=60, sample_size=400)  # , model_x=model, model_o=model
    train('../trained/sqe-masked3.h5', '../trained/sqe-masked3.h5', batch_size=60, sample_size=400, model_x=model_x, model_o=model_o)

    train('../trained/sqe-masked3.h5', '../trained/sqe-masked3.h5', batch_size=60, sample_size=400)  # , model_x=model, model_o=model
    train('../trained/sqe-masked3.h5', '../trained/sqe-masked3.h5', batch_size=60, sample_size=400, model_x=model_x, model_o=model_o)
