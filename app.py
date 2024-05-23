from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

events = [
    {
        'id': 1,
        'title': 'Концерт известного артиста',
        'date': '2024-06-01',
        'time': '18:00',
        'location': 'Концертный зал',
        'available_tickets': 100
    },
    {
        'id': 2,
        'title': 'Марафон',
        'date': '2024-07-10',
        'time': '08:00',
        'location': 'Центральный парк',
        'available_tickets': 50
    }
]

@app.route('/')
def index():
    return render_template('index.html', events=events)

@app.route('/event/<int:event_id>')
def event_details(event_id):
    event = next((event for event in events if event['id'] == event_id), None)
    if event:
        return render_template('event_details.html', event=event)
    else:
        return 'Event not found', 404

@app.route('/register/<int:event_id>', methods=['POST'])
def register(event_id):
    event = next((event for event in events if event['id'] == event_id), None)
    if event and event['available_tickets'] > 0:
        event['available_tickets'] -= 1
        return redirect(url_for('event_details', event_id=event_id))
    return 'Registration failed', 400

if __name__ == '__main__':
    app.run(debug=True)
