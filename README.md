# mytemp.email-python3-wrapper

A simple Python3 wrapper for temporary emails using https://mytemp.email

## Getting Started

Download mytemp.py to your project folder and import like so

```python
from mytemp import get_email, make_email
```

### Prerequisites

You will need to pip install the following to properly run this wrapper

```
pip install requests
```

## Running the tests

The following are all the ways that the wrapper can be used currently

### Create a new temporary email

This creates a new temporary email to be used for 24 hours

```python
from mytemp import get_email, make_email

sid = 73358 # from your account
returned = make_email(sid)
hash = returned[0] # hash that will be used when reading emails in inbox
email = returned[1] # the email that was created
```

### Check inbox of an email

Checks entire inbox of an email

```python
from mytemp import get_email, make_email

hash = 'e30077f4' # has for the email account
email = 'xcsb@uacro.com' # the email
emails = get_email(hash, email) # returns all emails within the inbox
```
### Create email then check inbox

This is everthing used together

```python
from mytemp import get_email, make_email

sid = 73358 # from your account
returned = make_email(sid)
hash = returned[0] # hash that will be used when reading emails in inbox
email = returned[1] # the email that was created
emails = get_email(hash, email) # returns all emails within the inbox
```


## Authors

* **Jake Strouse** -- [Profile](https://github.com/jakestrouse00)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Thanks of course to Andrei Husanu who created mytemp.email for which this wrapper was created for.
