from pyscript import display, document # type: ignore

def collecting_data(event=None):
    first = document.getElementById("fn").value
    last = document.getElementById("ln").value

    math = float(document.querySelector("#Math").value)
    english = float(document.querySelector("#English").value)
    filipino = float(document.querySelector("#Filipino").value)
    pe = float(document.querySelector("#PE").value)
    ict = float(document.querySelector("#ICT").value)
    science = float(document.querySelector("#Science").value)

    subject = [math, english, filipino, pe, ict, science]

    gwa = sum(subject) / len(subject)
    if gwa >= 95:
        remark = "Excellent"
    elif gwa >= 85:
        remark = "Good"
    elif gwa >= 75:
        remark = "Satisfactory"
    else:
        remark = "Failed"

    
    display(f"Name: {first} {last}", target="grades")
    display(f"Grades: {subject}", target="grades", append=True)
    display(f"GWA: {gwa}", target="grades", append=True)
    display(f"Remark: {remark}", target="grades", append=True)

