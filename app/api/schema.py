from app.models import Task
from app import db,ma
#create your schema here
class TaskSchema(ma.Schema):
    class Meta:
        fields = ('id','name','details','posted')
#init the schema
task_schema = TaskSchema(strict=True)
tasks_schema = TaskSchema(strict=True,many=True)
