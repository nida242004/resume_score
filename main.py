import os
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

# Ensure required NLTK packages are downloaded
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('punkt_tab')  # Adding the missing resource

class ResumeScanner:
    def __init__(self, keywords):
        self.keywords = keywords
        self.stop_words = set(stopwords.words('english'))

    def scan_folder(self, folder_path):
        results = {}
        for filename in os.listdir(folder_path):
            file_path = os.path.join(folder_path, filename)
            if os.path.isfile(file_path):
                score = self.scan_resume(file_path)
                results[filename] = score
        return results

    def scan_resume(self, file_path):
        text = ""
        encodings = ['utf-8', 'latin-1', 'windows-1252']  # Add more encodings as needed

        for encoding in encodings:
            try:
                with open(file_path, 'r', encoding=encoding) as file:
                    text = file.read()
                break  # Exit loop if reading is successful
            except (UnicodeDecodeError, FileNotFoundError):
                continue  # Try next encoding if there's an error

        # If text is still empty, raise an exception or handle it
        if not text:
            raise ValueError(f"Could not read the file: {file_path}")

        return self.calculate_score(text)

    def calculate_score(self, text):
        words = word_tokenize(text.lower())
        filtered_words = [word for word in words if word.isalnum() and word not in self.stop_words]

        print(f"Filtered words: {filtered_words}")  # Debugging line

        score = sum(1 for word in filtered_words if word in map(str.lower, self.keywords))

        print(f"Score calculated: {score}")  # Debugging line
        return score


# Usage
folder_path = r"E:\resumes"
keywords = [
    "Python",
    "Java",
    "C",
    "C++",
    "C#",
    "JavaScript",
    "HTML5",
    "CSS",
    "SQL",
    "AWS",
    "Machine Learning",
    "Data Science",
    "Big Data",
    "Software Development",
    "Agile",
    "Scrum",
    "UI/UX",
    "Mobile Development",
    "Android",
    "iOS",
    "Digital Marketing",
    "Information Technology",
    "Networking",
    "Linux",
    "DevOps",
    "Database Management",
    "Data Management",
    "Technical Support",
    "Software Engineering",
    "Quality Assurance",
    "Technical Skills",
    "Cloud Computing",
    "Business Analysis",
    "Data Entry",
    "Project Management",
    "Cybersecurity",
    "Technical Knowledge",
    "System Design",
    "Web Services",
    "Automation",
    "Troubleshooting",
    "Documentation",
    "Debugging",
    "APIs",
    "Version Control",
    "Git",
    "GitHub",
    "Data Structures",
    "Algorithms",
    "Computational Thinking",
    "Computer Science Fundamentals",
    "Critical Thinking",
    "Problem Solving"
]
scanner = ResumeScanner(keywords)
results = scanner.scan_folder(folder_path)

for resume, score in results.items():
    print(f"{resume}: {score}")
