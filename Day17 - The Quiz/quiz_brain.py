class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0
    
    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        response = input(f"Q{self.question_number}. {current_question.text} (True/False): ")
        self.check_answer(response, current_question.answer)
    
    def check_answer(self, response, answer):
        if response.lower() == answer.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("That's wrong.")
        print(f"The correct answer is: {answer}")
        print(f"Current Score: {self.score}/{self.question_number}\n")