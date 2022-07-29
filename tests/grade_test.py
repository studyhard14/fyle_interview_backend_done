from urllib import response

def test_grade_assignment_empty_header(client, h_teacher_1):
    #header is not provided
    response = client.post(
        '/teacher/assignments/grade',
        headers={},
        json={
            "id": 2,
            "grade": "A"
        }

    )

    assert response.status_code == 401
    data = response.json

    assert data['error'] == 'FyleError'



def test_grade_assignment(client, h_teacher_1):
    response = client.post(
        '/teacher/assignments/grade',
        headers=h_teacher_1,
        json={
            "id":1,
            "grade":"A"
        }
    )

    assert response.status_code == 200