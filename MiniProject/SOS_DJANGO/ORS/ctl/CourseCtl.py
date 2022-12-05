from django.shortcuts import render
from .BaseCtl import BaseCtl
from service.models import College, Course
from service.service.CourseService import CourseService
from ORS.utility.DataValidator import DataValidator


class CourseCtl(BaseCtl):
    def display(self, request, params={}):
        res = render(request, self.get_template(), {'form': self.form})
        return res

    def request_to_form(self, requestForm):
        self.form['id'] = requestForm['id']
        self.form['courseName'] = requestForm['courseName']
        self.form['courseDescription'] = requestForm['courseDescription']
        self.form['courseDuration'] = requestForm['courseDuration']

    def model_to_form(self, obj):
        if obj==None:
            return
        self.form['id'] = obj.id
        self.form['courseName'] = obj.courseName
        self.form['courseDescription'] = obj.courseDescription
        self.form['courseDuration'] = obj.courseDuration

    def form_to_model(self, obj):
        pk = int (self.form['id'])
        if (pk > 0):
            obj.id = pk
        obj.courseName = self.form['courseName']
        obj.courseDescription = self.form['courseDescription']
        obj.courseDuration = self.form['courseDuration']
        return obj


    def submit(self, request, params={}):
        r = self.form_to_model(Course())
        self.get_service().save(r)
        self.form['id'] = r.id
        self.form['error'] = False
        self.form['messege'] = "DATA HAS BEEN SAVED SUCCESSFULLY"
        res = render(request, self.get_template(), {'form': self.form})
        return res

    def input_validation(self):
        super().input_validation()
        inputError = self.form['inputError']
        if DataValidator.isNull(self.form['courseName']):
            self.form['error'] = True
            inputError['courseName'] = "Course name can not be null"
        if DataValidator.isNull(self.form['courseDescription']):
            self.form['error'] = True
            inputError['courseDescription'] = "Course description can not be null"
        if DataValidator.isNull(self.form['courseDuration']):
            self.form['error'] = True
            inputError['courseDuration'] = "Course duration can not be null"
        return self.form['error']




    def get_template(self):
        return 'Course.html'

    def get_service(self):
        return CourseService()