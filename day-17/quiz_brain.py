class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list

    def next_question(self):
        curreny_question = self.question_list[self.question_number]
        self.question_number += 1
        answer = input(
            f"Q.{self.question_number}: {curreny_question.text}.(True/False)?:")
        self.check_answer(answer, self.question_number)

    def still_has_question(self):
        if self.question_number < len(self.question_list):
            return True
        else:
            return False

    def check_answer(self, useranswer, q_answer):
        return useranswer == self.question_list[q_answer]
