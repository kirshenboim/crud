from flask_sqlalchemy import SQLAlchemy
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from marshmallow import fields


db = SQLAlchemy()


class Employee(db.Model):
    __tablename__ = "employee"

    id = db.Column(db.Integer, primary_key=True)
    employee_id = db.Column(db.Integer(), unique=True)
    name = db.Column(db.String(), index=False, unique=False, nullable=False)
    age = db.Column(db.Integer(), index=True, unique=False, nullable=False)

    def __init__(self, employee_id, name, age):
        self.employee_id = employee_id
        self.name = name
        self.age = age

    def __repr__(self):
        return f"{self.name}:{self.employee_id}"


class EmployeeSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Employee
        sqla_session = db.session
        include_relationships = True
        load_instance = True

    id = fields.Number(dump_only=True)
    employee_id = fields.Number(required=True)
    name = fields.String(required=True)
    age = fields.Number(required=True)
