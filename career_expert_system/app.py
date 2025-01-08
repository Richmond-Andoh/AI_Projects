
from flask import Flask, render_template, request


app = Flask(__name__)
app.secret_key = '4b3403665fea6a662c1d5c9e3f3cd3f0'

@app.route('/', methods=['GET', 'POST'])
def home():
    recommendations = []
    if request.method == 'POST':
        user_interest = request.form.get('interest')
        user_skills = request.form.get('skills').split(',')  # Input skills as comma-separated values
        user_education = request.form.get('education')
        
        #recommendations = recommend_career(user_interest, user_skills, user_education)
    
    return render_template('index.html', recommendations=recommendations)

if __name__ == '__main__':
    app.run(debug=True)
