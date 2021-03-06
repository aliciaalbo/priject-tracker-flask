"""A web application for tracking projects, students, and student grades."""

from flask import Flask, request, render_template

import hackbright

app = Flask(__name__)


@app.route("/student")
def get_student():
    """Show information about a student."""

    github = request.args.get('github')

    first, last, github = hackbright.get_student_by_github(github)

    html = render_template("student_info.html",
                           first=first,
                           last=last,
                           github=github)
    return html

@app.route("/student-search")
def get_student_form():
    """Show form for searching for a student."""

    return render_template("student_search.html")

@app.route("/new_student")
def student_add():
    """Show form for adding a student."""

    return render_template("new_student.html")

@app.route("/added_student", methods=["POST"])
def added_student():
    """Add a new student and print confirmation.

    Given a first name, last name, and GitHub account, add student to the
    database and print a confirmation message.
    """
    first_name = request.form.get('first_name')
    last_name = request.form.get('last_name')
    github = request.form.get('github')

    hackbright.make_new_student(first_name, last_name, github)
    hackbright.get_project_by_title(title)

    print(f"Successfully added student: {first_name} {last_name}")
    return render_template('thanks.html',
                            first_name=first_name,
                            last_name=last_name,
                            github=github)

    
if __name__ == "__main__":
    hackbright.connect_to_db(app)
    app.run(debug=True, host="0.0.0.0")
