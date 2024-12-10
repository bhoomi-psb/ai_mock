from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/help')
def help_page():
    return render_template('help.html')

@app.route('/about-us')
def about_us():
    return render_template('about-us.html')

@app.route('/interview-section')
def interview_section():
    return render_template('interview-section.html')

@app.route('/start-interview', methods=['GET', 'POST'])
def start_interview():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        interview_type = request.form['interview_type']
        experience = request.form['experience']
        return render_template(
            'start-interview.html',
            name=name,
            email=email,
            interview_type=interview_type,
            experience=experience
        )
    return redirect(url_for('interview_section'))

if __name__ == '__main__':
    app.run(debug=True)
