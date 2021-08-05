from PyWinda import dfm_module
import pytest

def testing_empty():
    assert dfm_module.dummy(7, 3) == 10