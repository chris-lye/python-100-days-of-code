class QuizBrain:
    def __init__(self, q_list) -> None:
        self.question_number = 0
        self.question_list = q_list
        self.score = 0
        
    def next_question(self):
        current_q = self.question_list[self.question_number]
        self.question_number += 1
        answer = input(f"Q.{self.question_number}: {current_q.text} (True/False): ")
        self.check_answer(answer, current_q.answer)
              
    def still_has_questions(self):
        if  self.question_number < len(self.question_list):
            return True
        return False
    
    def check_answer(self, answer, real_ans):
        if answer.lower() ==  real_ans.lower():
            print("Correct!")
            self.score += 1
        else:
            print("Wrong!")
        print(f"The correct answer was {real_ans}.")
        print(f"Current score: {self.score}/{self.question_number}")
        print("\n")