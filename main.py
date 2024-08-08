from flask import Flask, render_template, request
app = Flask(__name__)
app.route('/')
def hello_world():
  return render_template('index.html', message='Its my first website')
app.route('/about')
def about():
  return render_template('about.html')
app.route('/news')
def news():
  return render_template('news.html')
app.route('/form', methods=['GET', 'POST'])
def render_form():
    message = ''
    if request.method == 'POST':
        text = request.form.get('text')
        if request.form['submit_button'] == 'Lowercase':
            message = text.lower()
        elif request.form['submit_button'] == 'Capital':
            message = text.upper()
        elif request.form['submit_button'] == 'Enko':
            message = "Hi Enko"
        elif request.form['submit_button'] == 'Count words':
            word_counts = len(text.split())
            message = f"There are {word_counts} words"
    return render_template('form.html', message=message)
if __name__ == '__main__':
    app.run(debug=True)