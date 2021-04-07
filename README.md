# InvenioRDM Architecture Examples

## Install

```
mkvirtualenv training
pip install -r requirements.txt
```

## Examples

### Hello World

```
cd 1-helloworld
flask run
```

```
curl -X GET http://127.0.0.1:5000
```

### Architecture layers

```
cd 2-layers
flask run
```

```
curl -X POST \
    -H "Accept: application/json" \
    -H "Content-Type: application/json" \
    -d '{"id": 1, "title": "Test", "priority": 1}' \
    "http://127.0.0.1:5000/todos?user=1"

curl -X GET \
    -H "Accept: application/json" \
    "http://127.0.0.1:5000/todos/1?user=1"
```
