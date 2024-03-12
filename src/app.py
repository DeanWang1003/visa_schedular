from flask import Flask
import web_api
from global_variables import CHECK_INTERVAL_IN_SEC

reschedular = web_api.VisaAppointment()


obj = [{'username': "Jason2327265623@icloud.com",
        'password': "Yaoqulang123@"},
       {'username': "1486854487@qq.com",
        'password': "Packgogogo123!"}]

app = Flask(__name__)
@app.route("/")
def index():
    return "hello world"

@app.route('/visit')
def call_nd():
    # reschedular = web_api.VisaAppointment()
    # reschedular.check_recent_available_date()    
    web_api.run_function_wrapper(CHECK_INTERVAL_IN_SEC, reschedular.check_recent_available_date())

@app.route('/login')
def login_in():
    reschedular.get_date_url("1486854487@qq.com", "Packgogogo123!")
    return "hello world"

if __name__ == "__main__":
    app.run(debug=True)


