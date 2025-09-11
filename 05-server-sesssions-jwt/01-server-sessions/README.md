# Sessions and Cookies

If you already have read the notes, you can skip to the [Using the Example](#using-the-example) section below.

## Cookies

Cookies are pieces of data that your web client stores locally using your browser, desktop app, mobile device, or other client. In the case of browsers, cookies are often times held in some kind of small database (e.g. sqlite) for efficient retrieval. Cookies can be created/modified by the client application and can hold general information like UI state/settings, behavior/usage tracking, and other **NON-SENSITIVE** data. Cookies are associated with the domain of a website and sent along with requests to the web services and the values can be read, modified, or new cookie values can be created.

Cookie Features:

* Storage capacity limited to ~4KB per cookie
* Cookies have a wide range of lifespans
    * Minutes, Weeks, as long as the browser is open, etc.
    * Most browsers only allow a cookie to live for a maximum of 400 days
    * The client or web service can set the expiration for a cookie
* **NOT INTENDED FOR SECURE STORAGE**
    * No passwords, social security numbers, or other sensitve data


## Sessions

This example will use the `session` object in Flask. The default behavior of this mechanism isn't necessarily the tradional way that sessions are handled. The `session` object, creates a session cookie that is cryptographically signed (using a secret key) and holds session data, but it is **NOT ENCRYPTED**. This means if a client or bad actor were to modify the cookie, the server can detect the change due to the signing and respond accordingly. The data in the session cookie can be simlar to that of a normal cookie described above, but usually session are handled differently.

In general (and by using the `Flask-Session` extension), server-side sessions used and consist of two parts. For the client, a session cookie (signed or unsigned) is sent to that contains the ID of the session and some metadata (like when it expires). The actual data for the session is stored in a database or caching solution (like an in-memory Redis datastore) on the server. Since only a generated session ID is stored on the client, the web service performs a lookup on that ID to identify details of the session. When we consider the REST principles, this introduces server-side state and violates that principle. However, this does improve security as the data doesn't leave the server, reduces the amount of data to transfer, and allows for centralized control over authentication and access (must easier to revoke a session if it is found to have been hijacked). We simulate this with the `session` object built into Flask by only sending an ID and storing data for the session in a data structure that will be reset each time the server is restarted.

## Sessions vs Cookies

| Feature          | Sessions                                                                                                  | Cookies                                                                                     |
|------------------|-----------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------|
| Storage Location | (Usually) Server-side                                                                                     | Client-side (e.g. in the browser)                                                           |
| Data Stored      | All data for login status, shopping carts, etc. are on the server                                         | Small piece of data such as a session ID                                                    |
| Capacity         | Large (the actual data is held on the server)                                                             | Very small (4KB per cookie)                                                                 |
| Lifespan         | Temporary; Expires after inactivity or browser close                                                      | Usually persistent upon browser close but have an expiration, or temporary (session cookie) |
| Security         | More secure as session data is stored on the server. No direct access by the client.                      | Less secure. Data can be changed by client and server.                                      |
| Use Cases        | Storing sensitive data (login/authentication related), managing cross platform data like a shopping cart. | Saving/loading user preferences (UI mode, language, defaults) and tracking for analytics.   |

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
