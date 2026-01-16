"""Top-level package for {{ cookiecutter.project_name }}."""

__author__ = """{{ cookiecutter.developer_name }}"""
__email__ = '{{ cookiecutter.developer_email }}'

# Load local dev environment
import scion_analytics

import mlflow
import pathlib

mlruns = pathlib.Path(__file__).parent / 'mlruns'

mlflow.set_tracking_uri(f'file:{mlruns.as_posix()}') 

MODEL = mlflow.sklearn.load_model("models:/{{ cookiecutter.project_slug }}/latest")