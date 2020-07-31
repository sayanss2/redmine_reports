from flask import Flask, render_template, request
import red_api

app = Flask(__name__)
 
@app.route('/')
# @app.route('/index.html')
def test_main():
    return render_template('index.html')


@app.route('/process_data', methods=['POST'])
def funcname():
    api_data = request.form.get('api_data')
    return render_template('download.html',message='Ваш ключ API: ' + api_data)


# 404 error handler
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(debug=True)