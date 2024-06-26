import pytest
from django.urls import reverse
from rest_framework.status import HTTP_200_OK

from timed.projects.factories import TaskAssigneeFactory


@pytest.mark.parametrize(
    ("is_employed", "is_external", "is_customer_assignee", "is_customer", "expected"),
    [
        (False, False, True, False, 0),
        (False, False, True, True, 0),
        (True, True, False, False, 0),
        (True, False, False, False, 1),
        (True, True, True, False, 0),
        (True, False, True, False, 1),
        (True, True, True, True, 0),
        (True, False, True, True, 1),
    ],
)
def test_task_assignee_list(
    auth_client,
    is_employed,
    is_external,
    is_customer_assignee,
    is_customer,
    expected,
    setup_customer_and_employment_status,
):
    user = auth_client.user
    setup_customer_and_employment_status(
        user=user,
        is_assignee=is_customer_assignee,
        is_customer=is_customer,
        is_employed=is_employed,
        is_external=is_external,
    )
    task_assignee = TaskAssigneeFactory.create()
    url = reverse("task-assignee-list")

    res = auth_client.get(url)
    assert res.status_code == HTTP_200_OK
    json = res.json()
    assert len(json["data"]) == expected
    if expected:
        assert json["data"][0]["id"] == str(task_assignee.id)
        assert json["data"][0]["relationships"]["task"]["data"]["id"] == str(
            task_assignee.task.id
        )
