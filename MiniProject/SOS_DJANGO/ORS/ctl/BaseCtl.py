from django.http import HttpResponse

class BaseCtl():
    # Contains preload data
    preload_data = {}

    # Contains list of objects, it will be displayed at list page
    page_list = {}

    '''
    Initialize controller attributes
    '''
    #
    def __init__(self):
        self.form = {}
        self.form["id"] = 0
        self.form["messege"] = ""
        self.form["error"] = False
        self.form["inputError"] = {}
        self.form["pageNo"] = 1


    '''
    It loads preload data of the page 
    '''

    def preload(self, request):
        print("This is preload")



    '''
    execute method is executed for each HTTP request.  
    It in turn calls display() or submit() method for 
    HTTP GET and HTTP POST methods 
    '''

    def execute(self, request, params={}):
        # print("This is execute")
        self.preload(request)
        if "GET" == request.method:
            return self.display(request, params)
        elif "POST" == request.method:
            self.request_to_form(request.POST)
            if self.input_validation():
                return self.display(request, params)

            if (request.POST.get("operation") == "Delete"):
                return self.deleteRecord(request, params)
            elif (request.POST.get("operation") == "next"):
                print("oppp")
                return self.next(request, params)
            elif (request.POST.get("operation") == "previous"):
                return self.previous(request, params)

            else:
                return self.submit(request, params)

        else:
            messege = "Request is not supported"
            return HttpResponse(messege)

    def input_validation(self):
        self.form['error'] = False
        self.form['messege'] = ""








