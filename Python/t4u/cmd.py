import subprocess

def exec(command: str, timeout: float | None = None):
    """Execute command

    Args:
        command (str): _description_
        timeout (float | None, optional): 超时时间，以秒为单位。

    Returns:
        _type_: _description_
    """
    res = subprocess.run(command, shell=True, 
                   stdout=subprocess.PIPE, 
                   stderr=subprocess.PIPE, 
                   encoding='utf-8', timeout=timeout)
    if res.returncode != 0:
        raise RuntimeError(f'Failed to execute "{command}", this is the stderr:\n'
                           f'{res.stderr}')
    return res
