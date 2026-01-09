from pyscript import display, document

def calculate_gwa(e):
    # Getting the names
    fname = document.getElementById('fname').value
    lname = document.getElementById('lname').value

    # Getting and converting grades
    eng = float(document.getElementById('English').value)
    fil = float(document.getElementById('Filipino').value)
    math = float(document.getElementById('Math').value)
    sci = float(document.getElementById('Science').value)
    ss = float(document.getElementById('Social_Studies').value)
    pe = float(document.getElementById('PE').value)

    # Calculate the GWA
    gwa = (eng + fil + math + sci + ss + pe) / 6

    # Conditional Statements (if-else)
    if gwa > 74:
        result_status = "PASSED"
    else:
        result_status = "FAILED"

    # Producing the output
    output_text = f"Hello {fname} {lname}! Your GWA is {gwa:.2f}. Result: {result_status}"
    display(output_text, target='output', append=False)

def refresh_fields(e):
    # Simple list to clear all inputs
    fields = ['fname', 'lname', 'English', 'Filipino', 'Math', 'Science', 'Social_Studies', 'PE']
    for field in fields:
        document.getElementById(field).value = ""
    display("", target='output', append=False)