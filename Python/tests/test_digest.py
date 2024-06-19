from t4u.digest import md5


def test_md5():
    assert '6581c35e063322bc6c4f100c4aa48340' == md5('../test-data/sh-binary')
