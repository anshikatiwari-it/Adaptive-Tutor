"""Evaluate the Adaptive Tutor retrieval + generation pipeline with RAGAS.

Setup:   pip install ragas datasets
         export OPENAI_API_KEY=...   (or configure another LLM/embedding provider for RAGAS)
Run:     python ragas_eval.py

Fill in answer_question() to call your backend. It must return the generated answer
and the list of retrieved context strings (the excerpts the answer was written from).
Column names follow RAGAS 0.1.x (question, answer, contexts, ground_truth);
adjust them if your RAGAS version renamed them.
"""
import json

from datasets import Dataset
from ragas import evaluate
from ragas.metrics import answer_relevancy, context_precision, context_recall, faithfulness

REFUSAL_MARKERS = ("not in your course material", "not covered", "could not find")


def answer_question(question: str) -> tuple[str, list[str]]:
    """Call your tutor. Return (answer_text, [retrieved_context, ...])."""
    raise NotImplementedError("connect this to your retrieval + generation pipeline")


tests = json.load(open("test_set.json", encoding="utf-8"))
answerable = [t for t in tests if t["answerable"]]
off_material = [t for t in tests if not t["answerable"]]

# 1) RAGAS metrics on questions the material covers
rows = {"question": [], "answer": [], "contexts": [], "ground_truth": []}
for t in answerable:
    answer, contexts = answer_question(t["question"])
    rows["question"].append(t["question"])
    rows["answer"].append(answer)
    rows["contexts"].append(contexts)
    rows["ground_truth"].append(t["ground_truth"])

result = evaluate(
    Dataset.from_dict(rows),
    metrics=[faithfulness, answer_relevancy, context_precision, context_recall],
)
print(result)
result.to_pandas().to_csv("ragas_results.csv", index=False)

# 2) Off-material queries: the tutor should decline instead of answering from outside the course
refused = 0
for t in off_material:
    answer, _ = answer_question(t["question"])
    refused += any(m in answer.lower() for m in REFUSAL_MARKERS)
print(f"Correct refusals on off-material queries: {refused}/{len(off_material)}")

# Optional: the same test set with DeepEval
#   from deepeval import evaluate as de_evaluate
#   from deepeval.metrics import FaithfulnessMetric, AnswerRelevancyMetric, ContextualPrecisionMetric, ContextualRecallMetric
#   from deepeval.test_case import LLMTestCase
