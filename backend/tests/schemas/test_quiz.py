from quizapp.schemas.quiz import QuestionSchema


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
