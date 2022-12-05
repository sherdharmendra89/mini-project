from service.models import College
from ORS.utility.DataValidator import DataValidator
from .BaseService import BaseService
from django.db import connection

'''
It contains College business logics
'''

class CollegeService(BaseService):

    def get_model(self):
        return College

    def search(self,params):
        pageNo = (params['pageNo'] - 1) * self.pageSize
        sql = "select * from sos_college where 1=1"
        val = params.get("collegeName", None)
        if DataValidator.isNotNull(val):
            sql += " and collegeName = '"+val+"' "
        sql += " limit %s,%s"
        cursor  = connection.cursor()
        print("----------",sql,pageNo,self.pageSize)
        params['index'] = ((params['pageNo'] - 1) * self.pageSize)+1
        cursor.execute(sql, [pageNo, self.pageSize]) 
        result = cursor.fetchall()
        columnName = ('id','collegeName','collegeAddress','collegeState','collegeCity','collegePhoneNumber')
        res = {
            "data": [],
            "MaxId":1 # Using it through ORSAPI
        }
        res["index"] = params['index'] # Using it through ORSAPI
        for x in result:
            res["MaxId"] = params['MaxId'] = x[0]
            res['data'].append({columnName[i]: x[i] for i,_ in enumerate(x)})
        print("MMMMMMMMMM",params.get("MaxId"))
        return res



        