from t4u import archive


def test_zip_dir():
    b = archive.zip_dir('../test-data/test-dir/', 'tmp/t.zip')
    with open('tmp/t.zip', 'rb') as f:
        assert f.read() == b
