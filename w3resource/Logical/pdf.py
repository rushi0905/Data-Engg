from fpdf import FPDF

# A cleaned and categorized list based only on the uploaded PDF's content
qa_by_level = {
    "Beginner Level": [
        ("What is Python?", "Python is a general-purpose object-oriented programming language. It is widely used in web development, machine learning, and data science. It has a simple syntax and includes many libraries."),
        ("What is PEP 8?", "PEP 8 is the official style guide for Python code. It provides conventions for writing readable and consistent Python code."),
        ("What are Python lists and tuples?", "Lists are mutable, dynamic, and use square brackets. Tuples are immutable, fixed-length, and use parentheses."),
        ("What is an interpreted language?", "Python is interpreted, meaning it executes code line by line. If an error occurs, it stops at that line."),
        ("What are Python sets?", "Sets are unordered, unindexed, mutable collections of unique elements. Duplicate elements are not allowed."),
        ("What are Python dictionaries?", "Dictionaries store data in key-value pairs. They are ordered and mutable."),
        ("What is slicing?", "Slicing allows extracting parts of sequences like strings or lists using [start:end:step] syntax."),
    ],
    "Intermediate Level": [
        ("What is the difference between lists and arrays in Python?", "Lists can store mixed data types and don't require external libraries. Arrays (e.g., from NumPy) store elements of the same type and are more efficient for numerical operations."),
        ("What is a decorator?", "A decorator is a function that modifies the behavior of another function without changing its code."),
        ("What is a lambda function?", "Lambda is an anonymous, single-expression function defined using the lambda keyword."),
        ("Explain list and dictionary comprehensions.", "List: [x for x in iterable if condition], Dict: {k: v for (k, v) in iterable}"),
        ("What is a generator?", "Generators are functions that use 'yield' to return items one at a time, maintaining state between calls."),
        ("What are local and global variables?", "Local variables are defined inside functions. Global variables are defined outside and accessible throughout the program."),
    ],
    "Advanced Level": [
        ("What is inheritance in Python?", "Inheritance allows a class (child) to inherit attributes and methods from another class (parent)."),
        ("What is polymorphism?", "Polymorphism allows functions or methods to behave differently based on the object or input."),
        ("What is abstraction?", "Abstraction hides implementation details and shows only the functionality."),
        ("What is encapsulation?", "Encapsulation bundles data and methods that operate on that data into one unit."),
        ("What is exception handling in Python?", "Python handles exceptions using try, except, else, and finally blocks."),
        ("What is pickling and unpickling?", "Pickling serializes objects into byte streams. Unpickling restores them back into objects."),
        ("What is pandas groupby?", "The groupby() function splits the data into groups and applies functions like sum(), mean(), etc."),
    ]
}

# Create PDF using FPDF
class PDF(FPDF):
    def header(self):
        self.set_font("Arial", "B", 16)
        self.cell(0, 10, "Python Q&A – From Basic to Advanced", ln=True, align="C")
        self.ln(10)

    def chapter_title(self, title):
        self.set_font("Arial", "B", 14)
        self.set_fill_color(220, 220, 220)
        self.cell(0, 10, title, 0, 1, 'L', fill=True)
        self.ln(2)

    def question_answer(self, question, answer):
        self.set_font("Arial", "B", 12)
        self.multi_cell(0, 8, f"Q: {question}")
        self.set_font("Arial", "", 12)
        self.multi_cell(0, 8, f"A: {answer}")
        self.ln(4)

# Initialize and build the PDF
pdf = PDF()
pdf.add_page()

for level, qas in qa_by_level.items():
    pdf.chapter_title(level)
    for q, a in qas:
        pdf.question_answer(q, a)

# Save PDF
output_file_path = "/mnt/data/Python_QA_Basic_to_Advanced.pdf"
pdf.output(output_file_path)
output_file_path
