from js import document

def generate_message(*args):

    name = document.getElementById("name").value
    age = document.getElementById("age").value
    school = document.getElementById("school").value

    message = f"""
👤 Student Profile
Name\t: {name}
Age\t: {age}
School\t: {school}

📝 Notes:
{name} is currently {age} years old and studies at {school}.
This information was gathered through input fields and displayed using a multiline string in Python via PyScript.
"""

    output_div = document.getElementById("output")
    output_div.innerText = ""
    output_div.innerText = message

