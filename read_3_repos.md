# OpenSource Projects

Task
* Find 3 Open-source projects in an area or language I am passionate about.

## Repo 1: Apprise
https://github.com/caronc/apprise/

A notification system for multiple platforms.(slack, webex, text msg, email, etc) written in python. Docker is offered, and has an api for controlling it after install which runs on port 8000.


Code Structures
- setup.py
- babel is imported as frontend.
- expects `requirements.txt` or `win-requirements`.txt and `dev-requirements.txt`.
- executed as `apprise` and command line args.

command line args
  - `-b` for body of message
  -  `-c` for config location
  -  `-n` for notification-type, basically log level

arg responses

-  exit status returns 0,1,2,3 much like I had to do in C class.
   - 0 success. 
   - 1 1 couldn't be sent. 
   - 2 error in command line. 
   - 3. user filtering prevented urls from loading.

Example
```
apprise -vv -t "my title" -b "my notification body" \
"mailto://myemail:mypass@gmail.com" \
"pbul://o.gn5kj6nfhv736I7jC3cj3QLRiyhgl98b"
```


File Structures
- contains __init.py__ files where there are modules.
- Manual in /packaging/man
- configuration files can be in the format of either **TEXT** or **YAML**
- 



Find a method and understand it better:

Members of:
```python
class Apprise(object)
```
this is the notification manager. Loads a set of server urls while applying the Asset() module to each if specified. If no asset is provided, then the default asset is used.

Looking at `instantiate` function within the `Apprise Class`.

1. sets variable results to none
2. sets asset variable if not already set.
3. tries to acquire tokens from plugin urls, failure logic if it doesn't work
4. if results exist, use them.
5. tries to load dict with schema
6. calling common.py often. especially `common.NOTIFY_SCHEMA_MAP`
7. provides the errors at ever step to the logger.error and loggable_url
