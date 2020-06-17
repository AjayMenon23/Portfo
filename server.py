from flask import Flask, render_template, url_for, request,redirect
import csv
app = Flask(__name__)
print(__name__)

@app.route('/submitForm', methods=['POST', 'GET'])
def submitForm():
    if request.method == 'POST':
        try:
            data=request.form.to_dict()
            # write_to_file(data)
            write_to_csv(data)
            return redirect('thanks.html')
        except:
            return "didnt save to database"
    else:
        return 'error'

@app.route('/')
def home_of_me():
    return render_template('index.html')



@app.route('/index.html')
def home_me():
    return render_template('index.html')



@app.route('/<string:page_name>')
def page(page_name):
    return render_template(page_name)


def write_to_file(data):
    with open('database.txt',newline='',mode='a') as database:
        email = data["email"]
        subject = data["txt"]
        body= data["msg"]
        file = database.write(f'\n{email},{subject},{body}')


def write_to_csv(data):
    with open('database.csv',mode='a') as database2:
        email = data["email"]
        subject = data["txt"]
        body= data["msg"]
        csv_writer = csv.writer(database2,delimiter=',',quotechar='"',quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,subject,body])