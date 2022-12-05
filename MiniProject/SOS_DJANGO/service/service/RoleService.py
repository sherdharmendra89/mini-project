from django.db import connection

from .BaseService import BaseService
from ..models import Role


class RoleService(BaseService):
    def search(self, params = {}):

        pageNo = (params["pageNo"] - 1 ) * self.pageSize
        sql = "select * from sos_role where 1 = 1"
        sql += " limit %s, %s"
        cursor = connection.cursor()

        params['index'] = ((params['pageNo'] - 1) * self.pageSize) + 1

        cursor.execute(sql, [pageNo, self.pageSize])
        result = cursor.fetchall()
        columnName = ['id', 'name', 'description']
        res = {
            'data': [],
            'MaxId': 1
        }
        res["index"] = params["index"]


        for x in result:
            res["MaxId"] = params['MaxId'] = x[0]

            res['data'].append({columnName[i]: x[i] for i, _ in enumerate(x)})

        return res

    def get_model(self):
        return Role