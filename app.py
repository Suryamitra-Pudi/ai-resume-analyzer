from flask import Flask, render_template, request
import PyPDF2
import re

app = Flask(__name__)

job_roles = {
    "data_scientist": "We are looking for candidates with Python, SQL, Machine Learning, Data Analysis, and Communication skills.",
    
    "ml_engineer": "Candidates should have Machine Learning, TensorFlow, Python, and strong problem solving skills.",
    
    "frontend_dev": "Looking for skills in HTML, CSS, JavaScript, React, and UI/UX understanding.",
    
    "backend_dev": "Candidates should have Python, SQL, APIs, backend frameworks, and system design knowledge.",
    
    "fullstack_dev": "Looking for frontend and backend skills including JavaScript, Python, databases, and APIs."
}
suggestion_map = {
    "python": "Improve Python by building real-world projects",
    "sql": "Practice SQL queries and database design",
    "machine learning": "Work on ML models and real datasets",
    "data analysis": "Learn Pandas, NumPy and EDA techniques",
    "tensorflow": "Learn deep learning using TensorFlow",
    "html": "Learn semantic HTML and accessibility",
    "css": "Improve CSS, Flexbox and Grid",
    "javascript": "Practice JS, DOM and async concepts",
    "react": "Build projects using React",
    "api": "Learn REST API development",
    "django": "Build backend using Django",
    "flask": "Create APIs using Flask",
    "communication": "Improve communication and teamwork skills"
}

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/analyze', methods=['POST'])
def analyze():
    file = request.files['resume']
    role = request.form['role']
    job_desc = job_roles.get(role, "")

    if file:
        pdf_reader = PyPDF2.PdfReader(file)
        resume_text = ""

        for page in pdf_reader.pages:
            resume_text += page.extract_text()

        # lowercase
        resume_text = resume_text.lower()
        job_desc = job_desc.lower()

        # remove punctuation
        resume_text = re.sub(r'[^\w\s]', '', resume_text)
        job_desc = re.sub(r'[^\w\s]', '', job_desc)

        # 🔥 IMPORTANT SKILLS LIST
        role_skills = {
            "data_scientist": ["python", "sql", "machine learning", "data analysis", "communication"],
    
            "ml_engineer": ["python", "machine learning", "tensorflow", "data analysis"],
    
            "frontend_dev": ["html", "css", "javascript", "react"],
    
            "backend_dev": ["python", "sql", "api", "django", "flask"],
    
            "fullstack_dev": ["html", "css", "javascript", "python", "sql", "api"]
     }

        matched = []
        missing = []

        skills = role_skills.get(role, [])
        for skill in skills:
                if skill in resume_text:
                    matched.append(skill)
                else:

                    missing.append(skill)

        # score
        if len(matched) + len(missing) > 0:
           score = int((len(matched) / (len(matched) + len(missing))) * 100)
        else:
           score = 0
        # 🔥 suggestions
        # 🔥 suggestions (FINAL FIX)
        suggestions = []

        print("DEBUG MISSING:", missing)

        for skill in missing:
            if skill in suggestion_map:
                suggestions.append(suggestion_map[skill])             


        return render_template("result.html", score=score, matched=matched, missing=missing, suggestions=suggestions)

    return "Error"


if __name__ == '__main__':
 import os

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)