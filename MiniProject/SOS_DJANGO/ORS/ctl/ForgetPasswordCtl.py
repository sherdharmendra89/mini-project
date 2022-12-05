from django.shortcuts import render

from .BaseCtl import BaseCtl
from service.models import User

from service.service.EmailService import EmailService

from service.service.EmailMessege import EmailMessege


class ForgetPasswordCtl(BaseCtl):
    def request_to_form(self, requestForm):
        self.form["login_id"] = requestForm["login_id"]

    def display(self, request, params):
        return render (request, self.get_template())


    def submit(self, request, params):
        q = User.objects.filter()
        q = q.filter(login_id = self.form["login_id"])
        userList = ""
        for userData in q:
            userList = userData
        if userList != "":
            emsg = EmailMessege()
            emsg.to = [self.form['login_id']]
            emsg.subject = "Forget Password"
            mailResponse = EmailService.send(emsg, 'ForgetPassword', userList)
            if mailResponse == 1:
                self.form['error'] = False
                self.form["messege"] = "Please check your mail"
                res = render(request, self.get_template(), {'form':self.form})
            else:
                self.form['error'] = True
                self.form["messege"] = "Please check your internet connection"
                res = render(request, self.get_template(), {'form': self.form})
        else:
            self.form['error'] = True
            self.form["messege"] = "Login Id not Exist"
            res = render(request, self.get_template(), {'form': self.form})


        return res


    def get_template(self):
        return "ForgetPassword.html"

