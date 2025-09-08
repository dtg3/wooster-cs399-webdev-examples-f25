# Authentication

If you already have read the notes, you can skip to the [Using the Example](#using-the-example) section below.

## Using the Example
This example does **NOT** have a `.flaskenv` file. Now that we will be storing secrets in them, we do not want to have these files accidentially added to version control or publically transferred. The technical term for this happening is **BAD**.

You can create your .flaskenv file using the previous examples as a template, and add a `SECRET_KEY` to the configuration. You can easily generate a secret key using Python on your command line. First run Python using the `python` or `python3` command. Then enter the following code:

```python
>>> import secrets
>>> secrets.token_hex(32)
```

The 32 sets the number of bytes used for the secret value. We want the secret key to be long and random, so 32 or 64 bits is considered sufficient.

Once you have your `.flaskenv` setup, make sure your virtual environement running, and you can start your application with:

```bash
flask run
```

You can also run the Pytest suite, with:

```bash
pytest
```
