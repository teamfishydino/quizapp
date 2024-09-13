from fastapi import Response


def test_get_quizzes(test_client):
    response: Response = test_client.get("/api/quizzes/")
    assert response.status_code == 200
    assert len(response.json()) == 0
