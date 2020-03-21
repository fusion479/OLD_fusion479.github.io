# Stuy Fusion 479 Website

## Local deployment

### Virtual environment

- To prevent conflicts with globally installed packages, it is recommended to run everything below in a virtual environment.

Set up a virtual environment by running the following in your terminal:

```shell
python3 -m venv venv
```

To enter your virtual environment, run the following:

```shell
. venv/bin/activate
```

To exit your virtual environment, run the following:

```shell
deactivate
```

### Dependencies

Run the following line in your virtual environment

```shell
pip install -r requirements.txt
```

### Running on localhost

Run the following command

```shell
cd fusion
python __init__.py
```
