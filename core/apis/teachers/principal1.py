# from flask import Blueprint
# from core import db
# from core.apis import decorators
# from core.apis.responses import APIResponse
# from core.models.teachers import Teacher
# from .schema import TeacherSchema


# assignments_resources = Blueprint('assignments_resources', __name__)

# @assignments_resources.route('/teachers', methods=['GET'], strict_slashes=False)
# @decorators.authenticate_principal
# def list_teachers(p):
#     """Returns List of teachers"""
#     teachers = Teacher.get_teachers()
#     principal_teachers_dump = TeacherSchema().dump(teachers, many=True)
#     return APIResponse.respond(data= principal_teachers_dump)

