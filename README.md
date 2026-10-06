# Smart Study Resource Finder

## Project Overview

Smart Study Resource Finder is a student-friendly web application that helps users find relevant information from their study materials.

The application reads study PDFs stored in the data folder. Students can enter a topic or question, and the system searches the available PDF content and displays relevant results.

## Objectives

* To make study material searching easy.
* To find information quickly from PDF files.
* To save students' time.
* To provide a simple and user-friendly interface.
* To organize multiple study resources in one place.

## Technologies Used

* Python
* Streamlit
* PyPDF
* Pandas
* NumPy
* Scikit-learn
* Sentence Transformers
* ChromaDB
* Transformers
* PyTorch
* LangChain

## Project Structure

```text
Smart_Study_Resource_Finder/
│
├── app.py
├── README.md
├── requirements.txt
│
└── data/
    ├── DBMS.pdf
    ├── Java.pdf
    ├── Data Structures.pdf
    └── other PDF files
```

## Working

1. Study PDF files are added to the data folder.
2. The application reads the PDF files.
3. Text is extracted from the PDFs.
4. The student enters a topic or question.
5. The system searches for matching information.
6. Relevant results are displayed on the screen.

## How to Run

Open the project folder in VS Code and run:

```bash
python -m streamlit run app.py
```

The application will open in the web browser.

## Example Searches

Students can search for topics such as:

* Database
* Primary Key
* Binary Tree
* Java Inheritance
* Data Mining

## Features

* Simple user interface
* Multiple PDF support
* Keyword-based searching
* Fast search results
* Easy to add new study materials
* Student-friendly design

## Future Enhancements

* AI-based question answering
* Semantic search
* ChromaDB vector search
* PDF summarization
* Voice-based search
* Better result ranking
* Support for additional document formats

## Conclusion

Smart Study Resource Finder provides an easy way for students to search their study materials. The project can be enhanced with AI and semantic search technologies to provide more accurate and intelligent results.
