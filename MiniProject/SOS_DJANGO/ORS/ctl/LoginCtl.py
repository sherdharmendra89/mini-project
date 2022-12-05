from django.shortcuts import render, redirect
from .BaseCtl import BaseCtl
from service.service.UserService import UserService

from ORS.utility.DataValidator import DataValidator


class LoginCtl(BaseCtl):
    # print("This is loggg")

    def request_to_form(self, requestForm):
        self.form["login_id"] = requestForm["login_id"]
        self.form["password"] = requestForm["password"]

    def input_validation(self):
        super().input_validation()
        inputError =self.form['inputError']
        if(DataValidator.isNull(self.form['login_id'])):
            inputError['login_id'] = "LoginID not be null"
            self.form['error'] = True
        if(DataValidator.isemail(self.form['login_id'])):
            inputError['login_id'] = "LoginID is not email"
            self.form['error'] = True
        if (DataValidator.isNull(self.form["password"])):
            inputError["password"] = "Password can not be null"
            self.form["error"] = True

        return self.form["error"]


    def submit(self, request, params = {}):
        PATH = params.get('path')
        user = self.get_service().authenticate(self.form)
        # print(user, "userrrr")
        if (user is None):
            self.form['error'] = True
            self.form["messege"] = "Invalid ID or Password"
            res = render(request, self.get_template(), {"form": self.form})
        else:
            # print("LLLLLLLLLLLLL", PATH)
            request.session["user"] = user
            request.session['name'] = user.role_Name
            # print(request.session["user"] )
            # print(request.session['name'] )
            if PATH is None:
                # print("pathnoeee")
                res = redirect('/ORS/Welcome/')
            else:
                # print("elsepathnoeee")
                res = redirect('/ORS/Welcome/')
        return res


    def display(self, request, params = {}):
        return render(request, self.get_template(), {'form':self.form})

    def get_template(self):
        return "Login.html"

    def get_service(self):
        return UserService()