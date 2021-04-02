from flask import Flask, request, Response, jsonify, make_response, json
from models import db, Employee, EmployeeSchema
import http.client

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)


@app.before_first_request
def create_table():
    db.create_all()


@app.route('/employee', methods=['GET'])
def get_all_employees():
    get_employees = Employee.query.all()

    if get_employees:
        employee_schema = EmployeeSchema(many=True)
        employees = employee_schema.dump(get_employees)
        return make_response(jsonify({"employees": employees}))
    return f"employee table is still empty"


@app.route('/employee/<employee_id>', methods=['GET'])
def get_employee_by_id(employee_id):
    get_employee = Employee.query.filter_by(employee_id=employee_id).first()
    if get_employee:
        employee_schema = EmployeeSchema()
        employee = employee_schema.dump(get_employee)
        return make_response(jsonify({"employee": employee}))
    return f"Employee with employee_id = {employee_id} Does not exist"


@app.route('/employee/<employee_id>', methods=['PUT'])
def update_employee_by_id(employee_id):
    get_employee = Employee.query.filter_by(employee_id=employee_id).first()
    if get_employee:
        data = request.get_json()
        if data.get('employee_id'):
            get_employee.employee_id = data['employee_id']
        if data.get('name'):
            get_employee.name = data['name']
        if data.get('age'):
            get_employee.age = data['age']

        db.session.add(get_employee)
        db.session.commit()
        employee_schema = EmployeeSchema(only=['id', 'employee_id', 'name', 'age'])
        employee = employee_schema.dump(get_employee)
        return make_response(jsonify({"employee": employee}))
    return f"Employee with employee_id = {employee_id} Does not exist"


@app.route('/employee/<employee_id>', methods=['DELETE'])
def delete_employee_by_id(employee_id):
    get_employee = Employee.query.filter_by(employee_id=employee_id).first()
    if get_employee:
        db.session.delete(get_employee)
        db.session.commit()
        return Response(
            response='Employee Deleted',
            status=http.client.OK,
            mimetype='application/json'
        )
    return f"Employee with employee_id = {employee_id} Does not exist"


@app.route('/employee', methods=['POST'])
def create_employee():
    data = request.get_json()
    employee_schema = EmployeeSchema()
    employee = employee_schema.load(data)
    old_employee = Employee.query.filter_by(employee_id=employee.employee_id).first()

    if not old_employee:
        db.session.add(employee)
        db.session.commit()
        return Response(
            response=json.dumps({'employee': data}),
            status=http.client.OK,
            mimetype='application/json'
        )
    return f"Employee with employee_id = {employee.employee_id} is already exist"


if __name__ == "__main__":
    app.run(debug=True, port=5000, host='127.0.0.1')
