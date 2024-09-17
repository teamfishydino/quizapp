from pydantic import BaseModel, Field, field_validator


class QuestionSchema(BaseModel):
    question: str = Field(..., max_length=140)
    answer: bool = Field(...)

    def __hash__(self) -> int:
        return hash(self.question)

    def __eq__(self, other) -> bool:
        if isinstance(other, QuestionSchema):
            return self.__hash__() == other.__hash__()
        return False

    def __ne__(self, other) -> bool:
        return not self.__eq__(other)


class QuizSchema(BaseModel):
    name: str = Field(..., max_length=30)
    creator: str = Field(..., max_length=30)
    tags: set[str] = Field(set())
    questions: set[QuestionSchema] = Field(...)

    @field_validator("tags")
    @classmethod
    def validate_list_max_size_and_items_max_length(cls, tags: set[str]):
        assert len(tags) < 30, "Total number of tags must not exceed 30!"
        for tag in tags:
            assert (
                len(tag) < 30
            ), "The length of each tag must not exceed 30 characters!"
        return tags

    @field_validator("questions")
    @classmethod
    def validate_list_min_size(cls, questions: set[QuestionSchema]):
        assert len(questions) > 0, "The list must contain at least 1 question!"
        return questions

    class Config:
        json_schema_extra = {
            "example": {
                "name": "The Ultimate Life Quiz",
                "creator": "Anonymous",
                "tags": ["life", "philosophy", "science"],
                "questions": [
                    {
                        "question": "Is the meaning of life, the universe, and everything equal to 42?",
                        "answer": True,
                    },
                    {
                        "question": "Is the speed of light in a vacuum 300,000 km/h?",
                        "answer": False,
                    },
                ],
            }
        }
