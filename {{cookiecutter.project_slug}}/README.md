# {{ cookiecutter.project_name }}

> {{ cookiecutter.project_short_description }}

## Workflow

1. Run the following command to start a local mlflow server that logs models for production `./start mlflow-prod`
1. Develop your model in `dev/` using an mlflow workflow. See `dev/mlflow_example.ipynb` for a walkthrough of a basic mlflow workflow.
1. Add and commit the `package/src/{{ cookiecutter.project_slug }}/mlruns` directory
1. Build the package by running `pip install ./package`
1. Load the packaged model:
```python
from {{ cookiecutter.project_slug }} import MODEL
```

## Documentation Standards

The three notebooks in `docs/` must be authored.

## Code Standard

- [ ] Single responsibility of functions. Functions must not execute more than one major operation apart from high level functions that are executing a sequence of single responsibility functions.
- [ ] Variable names must be descriptive for maintainability and lineage.
- [ ] Inputs to a function must be annotated with their datatype.
- [ ] Outputs of functions must be annotated within the function's signature
- [ ] Docstrings should provide a descriptive summary of the inputs, the function's primary operation, and the function's output
- [ ] Data redundancy must be minimized. Whenever possible config values should be pulled directly from the configuration object, not stored in a separate variable. Variables that have been cast to a different datatype should be named in such a way to indicate the original source variable.
- [ ] Code templating with classes must be used for a specific reason such the need for subclassing or for caching data between calls of a method. 
- [ ] Over-abstraction of code must be minimized. Small, easy to read, operations should not be abstracted into helper functions unless it reduces redundancy and improves maintainability or when the operation is something users may want to overwrite with a subclass. Readability and maintainability must be heavily weighted.
- [ ] Code must past flake8 linting tests


## Project Structure
```
{{cookiecutter.project_slug}}
├── dev
│   ├── mlflow_example.ipynb
│   ├── README.md
│   ├── mlruns/ # gitignored
│   └── artifact-storage # gitignored
├── docs
│   ├── data_engineering.ipynb
│   ├── model_build.ipynb
│   └── model_evaluation.ipynb
├── package
│   ├── HISTORY.md # log descriptive summaries of model updates here
│   ├── justfile # included by cookiecutter. Not familiar but seems useful.
│   ├── MANIFEST.in # package config
│   ├── pyproject.toml # package config
│   └── src
│       └── {{cookiecutter.project_slug}}
│           ├── __init__.py
│           ├── __main__.py
│           ├── {{cookiecutter.project_slug}}.py
│           ├── cli.py
│           ├── utils.py
│           └── mlruns # model config files used in production
├── README.md
├── requirements.txt
├── start
└── tests
    ├── __init__.py
    └── test_{{cookiecutter.project_slug}}.py
```



