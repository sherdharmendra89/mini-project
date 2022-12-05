


from service.models import Marksheet
from ORS.utility.DataValidator import DataValidator
from .BaseService import BaseService
from django.db import connection

'''
It contains Role business logics.   
'''
class MarksheetService(BaseService):

    def search(self,params):
        print("Page No -->",params["pageNo"])
        pageNo = (params["pageNo"]-1)*self.pageSize
        sql="select * from sos_marksheet where 1=1"
        val = params.get("rollNumber", None)
        if DataValidator.isNotNull(val):
            sql+=" and rollNumber = '"+val+"' "
        sql+=" limit %s,%s" 
        cursor = connection.cursor()
        print("------------->",sql,pageNo,self.pageSize)
        params['index'] = ((params['pageNo'] - 1) * self.pageSize)+1
        cursor.execute(sql,[pageNo,self.pageSize])
        result=cursor.fetchall()
        columnName=("id","rollNumber","name","physics","chemistry","maths")
        res={
            "data":[],
            "MaxId":1 # Using it through ORSAPI
        }
        res["index"] = params["index"] # Using it through ORSAPI
        for x in result:
            print({columnName[i] :  x[i] for i, _ in enumerate(x)})
            res["MaxId"] =  params['MaxId'] = x[0]
            res["data"].append({columnName[i] :  x[i] for i, _ in enumerate(x)})            
        return res 
        
    def get_model(self):
        return Marksheet
