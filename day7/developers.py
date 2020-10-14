from flask import Flask
from flask_restful import reqparse, abort, Api, Resource

app = Flask(__name__)
api = Api(app)

DEVELOPERS = {
    1: "Akash",
    2: "Himanshu",
    3: "Vamsi"
}

TASKS = {
    1: "Develop an API", 2: "Unit testing",
    3: "Design the database", 4: "Normalize the database",
    5: "Deploy to cloud", 6: "Integrated testing",

}

DEVELOPER_TASKS = {
    DEVELOPERS[1]: {1: TASKS[1], 2: TASKS[2]},
    DEVELOPERS[2]: {3: TASKS[3], 5: TASKS[5]},
    DEVELOPERS[3]: {6: TASKS[6], 4: TASKS[4]}
}


def abort_if_dev_doesnt_exist(dev_id):
    if dev_id not in DEVELOPERS:
        abort(404, message=f'Developer with ID \'{dev_id}\' does not exist')


def abort_if_task_doesnt_exist(task_id):
    if task_id not in TASKS:
        abort(404, message=f"Task with ID {task_id} does not exist")


def abort_if_task_not_related(dev_id, task_id):
    tasks_of_developer = DEVELOPER_TASKS[DEVELOPERS[dev_id]]
    if task_id not in tasks_of_developer:
        abort(404, message="No such task for the given developer")


class DevelopersByDevID(Resource):

    def get(self, dev_id):
        abort_if_dev_doesnt_exist(dev_id)
        return {dev_id: DEVELOPERS[dev_id]}


class TasksByID(Resource):
    def get(self, task_id):
        abort_if_task_doesnt_exist(task_id)
        return {task_id: TASKS[task_id]}


class TasksByDeveloperId(Resource):
    def get(self, dev_id):
        abort_if_dev_doesnt_exist(dev_id)
        return {f"{DEVELOPERS[dev_id]}": DEVELOPER_TASKS[DEVELOPERS[dev_id]]}


class IndividualTasksByDevId(Resource):
    def get(self, dev_id, task_id):
        abort_if_dev_doesnt_exist(dev_id)
        abort_if_task_not_related(dev_id, task_id)
        my_task = DEVELOPER_TASKS[DEVELOPERS[dev_id]]
        return {f"{DEVELOPERS[dev_id]} with task ID {task_id} is ": my_task[task_id]
                }


api.add_resource(TasksByID, "/tasks/<int:task_id>")
api.add_resource(DevelopersByDevID, "/developers/<int:dev_id>")
api.add_resource(TasksByDeveloperId, "/developers/<int:dev_id>/tasks")
api.add_resource(IndividualTasksByDevId, "/developers/<int:dev_id>/tasks/<int:task_id>")

if __name__ == "__main__":
    app.run(debug=True)
