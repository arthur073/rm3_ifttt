import web
import json
import os

# User variables
passcode="mygreatpassword"


urls = (
   '/(.*)', 'main_process'
)
app = web.application(urls, globals())

class main_process:
    def POST(arg1,arg2):
        form_data = web.data()
        jform_data = json.loads(form_data)
        if jform_data['auth'] == passcode:    
            dir_path = os.path.dirname(os.path.realpath(__file__))
            os.system('python ' + dir_path + '/rm3_mini_controller/BlackBeanControl.py -c ' + json.dumps(jform_data['action']))
            return "OK - " + json.dumps(jform_data['action'])

if __name__ == "__main__":
    app.run()

