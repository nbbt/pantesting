from flask import Flask, jsonify
from pantesting.db.orm import Host

app = Flask(__name__)

@app.route('/')
def index():
    return app.send_static_file('html/index.html')

@app.route('/get_hosts/<host_id>')
def get_hosts(host_id):
    hosts = [Host(name='PayPal', description='Just paypal', url='http://paypal.com',
                  user='newt')]
    if host_id == 'all':
        return jsonify({'all': [host.to_dict() for host in hosts]})

if __name__ == '__main__':
    app.run(debug=True)