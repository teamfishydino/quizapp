from fastapi import Response


# https://pytest-with-eric.com/pytest-advanced/pytest-fastapi-testing/#Writing-Tests-with-Pytest
def test_create_and_get_quizzes(test_client, quiz_payload) -> None:
    # Check if quiz collection is empty
    response: Response = test_client.get("/api/quizzes/")
    assert response.status_code == 200
    assert len(response.json()) == 0

    # Create and get quiz
    response: Response = test_client.post("/api/quizzes/", json=quiz_payload)
    response_json = response.json()
    assert response.status_code == 201
    assert response_json.pop("id")
    assert response_json.pop("created_at")
    assert response_json == quiz_payload

    # Create one more quiz and check collection size after insertion
    response: Response = test_client.post("/api/quizzes/", json=quiz_payload)
    response: Response = test_client.get("/api/quizzes/")
    assert len(response.json()) == 2


def test_create_and_get_quiz(test_client, quiz_payload) -> None:
    # Create quiz and save id
    response: Response = test_client.post("/api/quizzes/", json=quiz_payload)
    quiz_id = response.json().pop("id")

    # Get quiz by id
    response: Response = test_client.get(f"/api/quizzes/{quiz_id}")
    assert response.status_code == 200
    response_json = response.json()
    assert response_json.pop("id")
    assert response_json.pop("created_at")
    assert response_json == quiz_payload


def test_get_quiz_not_found(test_client):
    non_existent_quiz_id = "64e16f8a2f9b1c3d4e5a6b7c"
    response = test_client.get(f"/api/quizzes/{non_existent_quiz_id}")
    assert response.status_code == 404
    response_json = response.json()
    assert (
        response_json["detail"]
        == f"No quizzes exist with the ID {non_existent_quiz_id}"
    )


def test_get_quiz_invalid_id(test_client):
    invalid_quiz_id = "12345"
    response = test_client.get(f"/api/quizzes/{invalid_quiz_id}")
    assert response.status_code == 400
    response_json = response.json()
    assert response_json["detail"] == "Invalid MongoDB ID"


def test_create_quiz_with_wrong_payload(test_client) -> None:
    response: Response = test_client.post("/api/quizzes/", json={})
    assert response.status_code == 422
