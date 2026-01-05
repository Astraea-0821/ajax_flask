from flask_restful import Resource

class Users(Resource):
    def get(self):
        return {"users":"所有使用者"},200
    def post(self):
        return {"users":"新增使用者"},200

class User(Resource):
    def get(self,user_id):
        #根據user id 讀取資料
        return {"users":user_id},200

    def put(self,user_id):
        return {"users修改":user_id},200

    def delete(self,user_id):
        return {"users刪除":user_id},200

