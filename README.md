# Adaptive Tutor

A source-grounded study companion (Track D: Personalized Tutoring and Adaptive Learning).
It answers only from lecture videos, slides and textbooks, cites the exact page, slide or
timestamp, runs adaptive quizzes, and models what the student knows.

Sample courses included: Data Structures and Design and Analysis of Algorithms (DAA).

## Run it
Open `index.html` in a browser. No install or server needed. Everything runs in the browser.

## What is inside
- `index.html` : the whole prototype (library and ingestion, tutor chat, adaptive quiz, learner model, dashboard, evaluation)
- `test_set.json` : team-built test set (questions with known source locations, plus off-material queries)
- `ragas_eval.py` : script to run RAGAS (faithfulness, answer relevancy, context precision and recall) on your backend

## Features
- Add your own `.pptx`, `.pdf`, `.txt`, `.md` or `.srt/.vtt` files; topics, concepts and prerequisites are tagged automatically
- Cited answers with refusals for off-material questions, plus Hindi explanations
- Quizzes (multiple choice, short answer, numerical), mock exams, verification and no repeated questions
- Bayesian knowledge tracing with a forgetting curve, intake chat and diagnostic for new students
- Evaluation tab with RAGAS-style metrics and simulated students

## Limits of this prototype
It is a front-end demo. Retrieval is keyword-based and video transcription, image captioning,
LLM answers and cross-model verification need a backend.
