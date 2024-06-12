# vanna-text-to-sql
Learn how to build a text-to-sql application using Vanna.AI and Streamlit

## Create a free Vanna.AI account

Follow the instructions in the [Vanna.AI](https://vanna.ai) website to create an account.  Once you are logged in, you will need to do the following:

- Get an API key (click on `API Keys` on the left side of the page) 
- Create a new RAG model (click on `RAG Models` on the left side of the page and choose a unique name for your model and click on the `Create Model` button)

## Steps to run the application

### Create a virtual environment

```
virtualenv venv
```

### Activate the virtual environment

```
source venv/bin/activate
```

### Install the required packages

```
pip install -r requirements.txt
```

### Train the RAG model
Follow the instructions in `train.py` to pass the variables required to run the code.  You will need to ensure that your database is running.  You can set up a test database to try this out.  Here is a [Github repo](https://github.com/pthom/northwind_psql) you can use to set one up.

```
python train.py
```

### Run the Streamlit application

```
python -m streamlit run sql_app.py
```

### Check out a demo of the application
https://github.com/pdamodaran/vanna-text-to-sql/assets/7106134/f2108665-9abc-4882-8612-4b288c855047

