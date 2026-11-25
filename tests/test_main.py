import main as student_app


def test_add_student_rejects_non_numeric_marks(monkeypatch, capsys):
    student_app.students.clear()
    answers = iter(["Arun", "ECE", "101", "not-a-number"])
    monkeypatch.setattr("builtins.input", lambda _prompt: next(answers))

    student_app.add_student()

    assert student_app.students == []
    assert "valid number" in capsys.readouterr().out


def test_add_student_stores_valid_record(monkeypatch):
    student_app.students.clear()
    answers = iter(["Arun", "ECE", "101", "85"])
    monkeypatch.setattr("builtins.input", lambda _prompt: next(answers))

    student_app.add_student()

    assert student_app.students == [
        {"name": "Arun", "roll_number": "101", "section": "ECE", "marks": 85.0}
    ]


def test_update_marks_rejects_non_numeric_input_without_mutating_record(monkeypatch, capsys):
    student_app.students[:] = [
        {"name": "Priya", "roll_number": "102", "section": "CSE", "marks": 75.0}
    ]
    answers = iter(["102", "invalid"])
    monkeypatch.setattr("builtins.input", lambda _prompt: next(answers))

    student_app.update_marks()

    assert student_app.students[0]["marks"] == 75.0
    assert "valid number" in capsys.readouterr().out
