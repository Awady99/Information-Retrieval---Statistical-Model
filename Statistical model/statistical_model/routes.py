from flask import render_template, request
from statistical_model import app
from statistical_model.statistical_model_main import main_fun, format_input


# @app.route("/about")
# def about():
#     return render_template('about.html', title='About')


@app.route('/')
@app.route('/Home')
@app.route('/home')
def home():
    return render_template('home.html', showdata=False)      #show data beyezher el white box for the result


@app.route('/', methods=['GET', 'POST'])
def my_form_post():
    if request.method == 'POST':
        text = str(request.form['text']).replace(" ", "")
        if text == "":
            return render_template('home.html', list=None, error=True, query=format_input(text), showdata=False)   #if empty query it returns to the same html page
        return render_template('home.html', list=main_fun(text), query=format_input(text), showdata=True, error=False)
    return render_template('home.html', showdata=False, error=False)



