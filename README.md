# Custom Logging Filter

This log filter implementation is based on the [structlog](https://www.structlog.org/en/stable/processors.html) processor.

## Limitations

To avoid the Python circular import issues, you need to keep Redis/LaunchDarkly connection settings separate from the [settings](app/src/settings.py) module.
Additionally, you can't use variables from `django.conf.settings` to initialize the filters storage client.


## Requirements
This project uses Docker to run the application.

## Usage
Use the following command to start containers:
```bash
./run.sh start app
```

By default, the project won’t log any messages where the `filtered` attribute set to `True`. 
You can change this by specifying certain words to bypass the filter using the following request:

```bash

curl --location 'http://127.0.0.1:9029/log/filter/' \ 
     --header 'Content-Type: application/json' \
     --data '{"log_filter": "Redis"}'
``` 

This request allows messages containing the word `Redis` in the `event` key to be logged, even if they are marked as filtered.
