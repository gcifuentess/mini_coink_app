# Mini WebApp for Coink

This is a mini web application for Coink, in which users can be registered in a database. It also has a view where all registered users can be seen in a list.

---

![registro](https://user-images.githubusercontent.com/66188250/149825638-4905bf16-4170-4efd-88ed-972e15af2858.png)

---

![reporte](https://user-images.githubusercontent.com/66188250/149825782-fea0eed2-9a9f-4fae-a7be-8f81b2896249.png)

---

## Features

1. Users registration
    - The App uses an API to register users
    - The App has field validation for the form (trough the API)
      * The fields "Nombre completo" and "Ciudad" can't have comas or be empty
      * The field "Email" should have an e-mail format (trough regex)
    - The App verifies if the API is running. A user can't be registered if the API is down.
      * In the upper-right corner of the app there is a circle. When is green the API is up, when is gray it s down
    - The App parses the response of the API and shows the message

2. The records are stored in a SQLite database

3. Users report
    - The App has a page where all the records are displayed dynamically in a table

4. Log creation
    - Every time a user is created a log plain file is updated or created

5. The App uses SQLAlchemy as ORM

## Installation

```bash
git clone https://github.com/gcifuentess/mini_coink_app.git
```

## Requirements

* Python3
* Flask==2.0.2
* Flask_Cors==3.0.10
* SQLAlchemy==1.4.29

## Usage

### Running up the servers:
#### Automatically:

```Bash
./run.sh
```

#### Manually:

It's recommended to use two terminals or a multiplexer.

* Running the Front flask server (first terminal):
```bash
python3 -m web_dynamic.front
```

* Running the API flask server (second terminal):
```bash
python3 -m api.v1.app
```

### Accessing the web application:

Front:
```
http://localhost:5000/
```

API:
```
http://localhost:5001/api/v1/[status, users]
```

---

## Author
* **Gabriel Cifuentes** - [gcifuentess](https://github.com/gcifuentess/)
