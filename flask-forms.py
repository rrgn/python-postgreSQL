####### ex-5

from flask import Flask, render_template, request, redirect
import pg

db = pg.DB(dbname='students_db')

app = Flask('MyFormApp')

@app.route('/')
def form():
    # Render the form.html template
    return render_template(
        'form-student.html',
        title='Enter new student')

# This URL receives the form submit and processes it
@app.route('/submit_form', methods=['POST'])
def submit_form():
    student_name = request.form['student_name']
    student_website = request.form['student_website']
    cohort_start_date = request.form['cohort_start_date']
    db.insert('student', name=student_name, website=student_website, cohort_start_date=cohort_start_date)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
