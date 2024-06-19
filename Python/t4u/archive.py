from io import BytesIO
import os
import zipfile
from os.path import join, realpath


def zip_dir(source_dir, saving_path: os.PathLike = None) -> bytes:
    """Pack a directory to a zip file, all content saving in memory.
    TODO support exclude_patten=[],
    Args:
        source_dir (_type_): _description_
        saving_path (os.PathLike, optional): _description_. Defaults to None.
    """
    bi = BytesIO()
    # TODO pack all files in the directory
    source_path_length = len((source_dir))
    with zipfile.ZipFile(bi, 'w') as zip_file:
        path_iterator = os.walk(source_dir, followlinks=True)
        for i in path_iterator:
            dirname = i[0]
            for filename in i[2]:
                full_path = join(dirname, filename)
                real_path = realpath(full_path)
                arc_path = full_path[source_path_length:]
                zip_file.write(real_path, arc_path)
    bi.seek(0)
    b = bi.read()
    if saving_path:
        dir = os.path.dirname(saving_path)
        os.makedirs(dir, exist_ok=True)
        with open(saving_path, 'wb') as f:
            f.write(b)
    return b
