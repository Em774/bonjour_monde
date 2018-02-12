import pytest
import bonjour
import builtins
from unittest import mock

def test_bonjour_no_name():
    """
    Checks that if no name is passed, we get "Bonjour Monde"
    """
    assert bonjour.bonjour() == 'Bonjour, Monde'


def test_bonjour_with_name():
    """
    If passed a name, returns "Bonjour, name"
    """
    assert bonjour.bonjour('Emilie') == 'Bonjour, Emilie'
