from quizapp.schemas.quiz import QuestionSchema, QuizSchema


def test_question_equality():
    question_one = QuestionSchema(
        question="Is the meaning of life, the universe, and everything equal to 42?",
        answer=True,
    )
    question_two = QuestionSchema(
        question="Is the meaning of life, the universe, and everything equal to 42?",
        answer=True,
    )
    question_three = QuestionSchema(
        question="Is the speed of light in a vacuum 300,000 km/h?",
        answer=False,
    )
    assert question_one == question_two
    assert question_one != question_three


def test_quiz_schema_list_order_and_uniqueness(
    quiz_payload_for_list_order_and_uniqueness_test,
    correct_answers_for_list_order_and_uniqueness_test,
):
    quiz = QuizSchema(**quiz_payload_for_list_order_and_uniqueness_test)
    questions, tags = correct_answers_for_list_order_and_uniqueness_test
    assert quiz.questions == [QuestionSchema(**question) for question in questions]
    assert quiz.tags == tags
