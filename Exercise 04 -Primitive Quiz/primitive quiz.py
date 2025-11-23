questions = {
    "France": "paris",
    "Germany": "berlin",
    "Italy": "rome",
    "Spain": "madrid",
    "Hungary": "budapest",
    "Egypt": "cairo",
    "Netherlands": "amsterdam",
    "Lebanon": "beirut",
    "Norway": "oslo",
    "Jordan": "amman"
}

for country, capital in questions.items():
    answer = input(f"What is the capital of {country}? ")

    if answer.lower() == capital:
        print("Correct!")
    else:
     print("Wrong!")