CRUD TASK

- routes:
    create employee
    POST http://127.0.0.1:5000/employee
        body{
            "employee_id": 344567891,
            "name": "itayk",
            "age": 31
            }

    update employee
    PUT http://127.0.0.1:5000/employee
        body{
            "employee_id": 344567891,
            "name": "itayk",
            "age": 31
            }

    get employee
    GET http://127.0.0.1:5000/employee/1

    get all employees
    GET http://127.0.0.1:5000/employee

    delete employee
    DELETE http://127.0.0.1:5000/employee/1

some improvements
- create new micro services (db)
- API, BL, DAL
- separate into config file
- try & catch
- hierarchy of directories
- integration tests
- unit tests
- input validations
- error handling
- fix response format (rid, body, DAL exception etc)
- fix serialization
- add more fields (created_at, updated_at, deleted_at)
- logger (for debug)
- Constant file
- resource bundle (multi languages functionality)