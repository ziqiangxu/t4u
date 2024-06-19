import hashlib
from os import PathLike


def md5(file_path: PathLike) -> str:
    """Compute a file's md5 digest

    Args:
        file_path (PathLike): _description_

    Returns:
        str: _description_
    """
    md5_hash = hashlib.md5()
    with open(file_path, 'rb') as file:
        for chunk in iter(lambda: file.read(8192), b''):
            md5_hash.update(chunk)
    md5_value = md5_hash.hexdigest()
    return md5_value
