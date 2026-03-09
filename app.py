from flask import Flask, request, redirect

app = Flask(__name__)

patients = []

def triage(fever, cough, breath):

    if breath == "yes":
        return "HIGH", "Emergency referral to hospital"

    if fever == "yes" and cough == "yes":
        return "MEDIUM", "Visit PHC"

    return "LOW", "Home care"


@app.route("/")
def home():

    return """
    <h1 style='color:green'>AI Health Triage</h1>

    <form action='/login' method='post'>

    Select Role<br><br>

    <select name='role'>
    <option value='patient'>Patient</option>
    <option value='asha'>ASHA Worker</option>
    </select>

    <br><br>

    <button type='submit'>Login</button>

    </form>
    """


@app.route("/login", methods=["POST"])
def login():

    role = request.form["role"]

    if role == "patient":
        return redirect("/symptoms")

    return redirect("/asha")


@app.route("/symptoms")
def symptoms():

    return """
    <h2>Enter Symptoms</h2>

    <form action='/analyze' method='post'>

    Fever (yes/no)<br>
    <input name='fever'><br><br>

    Cough (yes/no)<br>
    <input name='cough'><br><br>

    Breathing Difficulty (yes/no)<br>
    <input name='breath'><br><br>

    <button type='submit'>Analyze</button>

    </form>
    """


@app.route("/analyze", methods=["POST"])
def analyze():

    fever = request.form["fever"]
    cough = request.form["cough"]
    breath = request.form["breath"]

    risk, advice = triage(fever, cough, breath)

    patients.append({"risk": risk, "advice": advice})

    return f"""
    <h2>AI Triage Result</h2>

    Risk Level: <b>{risk}</b><br><br>

    Advice: {advice}<br><br>

    <a href='/'>Back</a>
    """


@app.route("/asha")
def asha():

    html = "<h2>ASHA Worker Dashboard</h2><br>"

    for p in patients:

        html += f"""
        <div style='border:1px solid gray;padding:10px;margin:10px'>
        Risk: <b>{p['risk']}</b><br>
        Advice: {p['advice']}
        </div>
        """

    html += "<br><a href='/'>Back</a>"

    return html


app.run(debug=True)
