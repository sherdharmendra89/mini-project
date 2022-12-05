from django.shortcuts import render

from .BaseCtl import BaseCtl
from service.service.RoleService import RoleService

from service.models import Role


class RoleListCtl(BaseCtl):
    count = 1
    def request_to_form(self, requestForm):
        # self.form['id']= requestForm.get('id', None)
        self.form['name'] = requestForm.get('name', None)
        self.form['description'] = requestForm.get('description', None)
        self.form['ids'] = requestForm.getlist('ids', None)


    def display(self, request, params={}):
        RoleListCtl.count = self.form['pageNo']
        record = self.get_service().search(self.form)
        self.pageList = record['MaxId']
        self.pageList = record['data']
        res = render(request, self.get_template(),{'pageList':self.pageList,'form':self.form})
        return res

    def deleteRecord(self, request, params={}):

        if (bool(self.form['ids']) == False):
            self.form['error'] = True
            self.form['messege'] = "Please Select at least one Checkbox"
            record = self.get_service().search(self.form)
            self.page_list = record['data']
            res = render(request, self.get_template(), {'pageList': self.page_list, 'form': self.form})
        else:
            for ids in self.form['ids']:
                print(ids, "idssss")
                self.get_service().delete(ids)
                record = self.get_service().search(self.form)
                self.pageList = record['data']
                self.form['pageNo'] = 1

            res = render(request, self.get_template(), {'form': self.form, 'pageList': self.pageList})
        return res

    def next(self, request, params = {}):
        RoleListCtl.count += 1

        self.form['pageNo'] = RoleListCtl.count
        record = self.get_service().search(self.form)
        print(record, "rcorddd")
        self.page_list = record['data']
        if self.page_list == []:
            self.form['mesg'] = "No record found"
        self.form['LastId'] = Role.objects.last().id
        print(self.page_list, "pagelistttt")

        res = render(request, self.get_template(), {'pageList': self.page_list, 'form': self.form})
        return res
    def previous(self, request, params):
        RoleListCtl.count -= 1
        self.form['pageNo'] = RoleListCtl.count
        record = self.get_service().search(self.form)
        pageList = record['data']
        res = render(request, self.get_template(), {'pageList':pageList, 'form':self.form})
        return res


    def get_template(self):
        return "RoleList.html"

    def get_service(self):
        return RoleService()