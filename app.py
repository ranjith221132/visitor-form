from flask import Flask, render_template

app = Flask(__name__)

@app.route('/visitor/visitorform')
def custom_route():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)  # Allow access from external IPs
