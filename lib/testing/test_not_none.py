#!/usr/bin/env python3

from not_none_functions import return_true


def test_return_true():
    """in not_none_functions, function "return_true" returns a value that is True."""
    result = return_true()
    assert result is True
