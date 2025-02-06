from flask import Flask, render_template, request, redirect, url_for
from career_expert import CareerExpert
from career_data import career_details

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        interest = request.form["interest"].lower().strip()
        skill = request.form["skill"].lower().strip()
        education = request.form["education"].lower().strip()

        return redirect(url_for("results", interest=interest, skill=skill, education=education))
    
    return render_template("index.html")

@app.route("/results")
def results():
    interest = request.args.get("interest")
    skill = request.args.get("skill")
    education = request.args.get("education")

    expert = CareerExpert()
    recommendations = expert.recommend(interest, skill, education)

    return render_template("results.html", recommendations=recommendations)

@app.route("/career/<career_name>")
def career_profile(career_name):
    career_info = career_details.get(career_name)
    if not career_info:
        return render_template("error.html", message="Career not found.")

    # Get related careers (any career that shares at least one skill)
    related_careers = [name for name, details in career_details.items()
                       if name != career_name and set(details["skills"]).intersection(set(career_info["skills"]))]

    return render_template("career_profile.html", career=career_info, career_name=career_name, related_careers=related_careers)

saved_careers_list = []

@app.route("/save_career/<career_name>")
def save_career(career_name):
    if career_name not in saved_careers_list:
        saved_careers_list.append(career_name)
    return redirect(url_for('saved_careers'))

@app.route("/saved_careers")
def saved_careers():
    return render_template("saved_careers.html", saved_careers=saved_careers_list)


@app.route("/search", methods=["GET", "POST"])
def search():
    results = []
    if request.method == "POST":
        query = request.form["query"].strip().lower()
        results = [career for career in career_details.keys() if query in career.lower()]
    return render_template("search.html", results=results)

@app.route("/compare", methods=["GET", "POST"])
def compare():
    career1, career2 = None, None
    if request.method == "POST":
        career1 = request.form.get("career1")
        career2 = request.form.get("career2")
        return redirect(url_for("compare_results", career1=career1, career2=career2))
    return render_template("compare.html", careers=list(career_details.keys()))

@app.route("/compare_results")
def compare_results():
    career1 = request.args.get("career1")
    career2 = request.args.get("career2")

    if not career1 or not career2 or career1 == career2:
        return render_template("error.html", message="Please select two different careers.")

    details1 = career_details.get(career1)
    details2 = career_details.get(career2)

    return render_template("compare_results.html", career1=career1, career2=career2, details1=details1, details2=details2)

if __name__ == "__main__":
    app.run(debug=True)
