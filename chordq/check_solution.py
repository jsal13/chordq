from chordq.note import Note


def check_solution(user_answer: str, answer: list[Note]) -> bool:
    """
    Check a user solution against the actual solution.

    Args:
        user_answer (str): User's string answer.
        answer (list[Note]): Answer as a list of Notes, including the tonic.

    Returns:
        bool: True if the answer is correct.
    """
    parsed_user_answer = [
        Note(note=user_note) for user_note in user_answer.strip().split()
    ]
    # Include the tonic?
    if len(parsed_user_answer) + 1 == len(answer):
        parsed_user_answer.insert(0, answer[0])

    return parsed_user_answer == answer
