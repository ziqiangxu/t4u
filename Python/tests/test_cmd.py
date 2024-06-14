import pytest
from t4u import cmd


def test_exec():
    with pytest.raises(RuntimeError):
       cmd.exec('unknown-cmd 1')
    
    cmd.exec('sleep 1', timeout=2)
