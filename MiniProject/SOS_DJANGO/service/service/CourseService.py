from django.db import connection

from .BaseService import BaseService
from service.models import Course

from ORS.utility.DataValidator import DataValidator


class CourseService(BaseService):

    def search(self,params):
        pageNo =  (params['pageNo']-1) * self.pageSize
        sql = "select * from sos_course where 1=1"
        val = params.get("courseName", None)
        if DataValidator.isNotNull(val):
            sql += " and courseName = '"+val+"' "
        sql += " limit %s,%s"
        cursor = connection.cursor()
        cursor.execute(sql, [pageNo, self.pageSize])
        params['index'] = ((params['pageNo'] - 1) * self.pageSize)+1
        result = cursor.fetchall()
        columnName = ('id','courseName','courseDescription','courseDuration')
        res = {
            "data": [],
            "MaxId":1 # Using it through ORSAPI
        }
        res["index"] = params["index"] # Using it through ORSAPI
        for x in result:
            print({columnName[i]: x[i] for i,_ in enumerate(x)})
            res['MaxId'] = params['MaxId'] = x[0]
            res['data'].append({columnName[i]: x[i] for i,_ in enumerate(x)})
        return res


    def get_model(self):
        return Course


