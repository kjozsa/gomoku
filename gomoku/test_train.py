from gomoku.trainer import train, load_or_create_model


def test_train():
    # model_x = load_or_create_model('../trained/sqe-masked2.h5')
    model_o = load_or_create_model('../trained/sqe-weighted2s.h5')

    train('../trained/sqe-weighted2s.h5', '../trained/sqe-weighted2ss.h5', batch_size=200, sample_size=50, model_x=model_o)  # , model_x=model_x, model_o=model_o

    # model_o = load_or_create_model('../trained/sqe-weighted3.h5')
    # train('../trained/sqe-weighted3.h5', '../trained/sqe-weighted3.h5', batch_size=100, sample_size=50, model_x=model_x, model_o=model_o)
    #
    # model_o = load_or_create_model('../trained/sqe-weighted3.h5')
    # train('../trained/sqe-weighted3.h5', '../trained/sqe-weighted3.h5', batch_size=100, sample_size=50, model_x=model_x, model_o=model_o)
    #
    # model_o = load_or_create_model('../trained/sqe-weighted3.h5')
    # train('../trained/sqe-weighted3.h5', '../trained/sqe-weighted3.h5', batch_size=100, sample_size=50, model_x=model_x, model_o=model_o)
