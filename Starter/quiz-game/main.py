from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)
final_score = quiz.score
question_number = quiz.question_number

while quiz.still_has_questions():
    quiz.next_question()
print("You have completed the quiz")
print(f"Your final score is {final_score}/{question_number}")