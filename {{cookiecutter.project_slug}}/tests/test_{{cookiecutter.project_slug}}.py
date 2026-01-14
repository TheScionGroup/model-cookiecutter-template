#!/usr/bin/env python
import pytest

"""Tests for `{{ cookiecutter.project_slug }}` package."""

# from {{ cookiecutter.project_slug }} import {{ cookiecutter.project_slug }}


@pytest.fixture
def phrase():
    """Sample pytest fixture.

    See more at: http://doc.pytest.org/en/latest/fixture.html
    """
    
    return 'orange hat'


def test_content(phrase):
    """Sample pytest test function with the pytest fixture as an argument."""
    
    assert len(phrase) == 10
