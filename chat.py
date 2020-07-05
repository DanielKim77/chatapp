from flask import Flask, render_template, request
from flask_socketio import SocketIO
app = Flask(__name__)
socketio = SocketIO(app)
messages = []

@app.route('/')
def main():
	return render_template('index.html', messages=messages)

@app.route('/clear/', methods=['POST'])
def clear():
	global messages
	messages = []
	# print('VGHYJNBVGFYHUKJHBVFGHYUJNBVGFHYUIJNBVFGHYUJJNBVFGHJBV CFGHBVCFGFU')
	return main()


@socketio.on('my event')
def handle_text(json, methods=['GET','POST']):
	print('FORM',request.form)
	if request.method == 'POST':
		print(request.form['clear'])
	global messages
	print(str(json))
	messages.append(json)
	print(messages)
	socketio.emit('my response', json)
if __name__ == '__main__':
	socketio.run(app,debug=True)