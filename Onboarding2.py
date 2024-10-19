from openai import OpenAI
from pyswip import Prolog
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

def translate_to_prolog(natural_language_input):
    client = OpenAI(api_key=api_key)
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": f"Translate the following natural language statement to Prolog: '{natural_language_input}. Just give the prolog code, nothing more is required.'"}
        ]
    )
    prolog_code = response.choices[0].message.content.strip()  # Strip to remove any leading/trailing whitespace
    return prolog_code

def run_prolog_code(prolog_code):
    # Initialize the Prolog interpreter
    prolog = Prolog()

    # Clean up the Prolog code
    prolog_lines = prolog_code.strip().splitlines()

    # Parse and assert Prolog facts and rules
    for line in prolog_lines:
        line = line.strip()
        if line:  # Only process non-empty lines
            # Debug output
            print(f"Asserting: {line}")  
            # Remove the trailing period before asserting
            if line.endswith('.'):
                line = line[:-1]  # Remove the period
            prolog.assertz(line)

    # Query to check if Socrates is human
    human_results = list(prolog.query("human(socrates)."))
    print("Results from querying if Socrates is human:")
    print(human_results)  # Should return [{'': ''}]

    # Query to check if Socrates is mortal
    mortal_results = list(prolog.query("mortal(socrates)."))
    print("Results from querying if Socrates is mortal:")
    print(mortal_results)  # Should return [{'': ''}]

    # Final output
    if mortal_results:
        print("Socrates is mortal:", mortal_results)
    else:
        print("Socrates is not mortal.")

def main():
    # Example natural language input
    natural_language_input = "Socrates is a human and all humans are mortal."

    # Translate the natural language input to Prolog
    prolog_code = translate_to_prolog(natural_language_input)
    print(f"Generated Prolog Code:\n{prolog_code}\n")

    # Run the generated Prolog code
    run_prolog_code(prolog_code)

if __name__ == "__main__":
    main()
