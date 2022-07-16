class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        answer = input(
            f"Q.{self.question_number}: {current_question.text}. (True/False): ")
        self.check_answer(answer, current_question.answer)

    def still_has_question(self):
        if self.question_number < len(self.question_list):
            return True
        else:
            return False

    def check_answer(self, useranswer, q_answer):
        if useranswer.lower() == q_answer.lower():
            print("You get it Right")
            self.score += 1
        else:
            print("Thats's Wrong")
        print(f"The correct answer was: {q_answer}")
        print(f"Your current score is : {self.score}/{self.question_number}")
        print("\n")
