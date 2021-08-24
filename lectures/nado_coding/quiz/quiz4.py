class Word:
    def __init__(self, question, ex1, ex2, answer):
        self.question = question
        self.ex1 = ex1
        self.ex2 = ex2
        self.answer = answer
    def show_question(self):
        print(f'" {self.question} "의 뜻은?')
        print(f'1. {self.ex1}')
        print(f'2. {self.ex2}')
    def check_answer(self, answer):
        if self.answer == answer:
            print('정답입니다.')
        else:
            print('틀렸습니다.')

q1 = Word('얼죽아', '얼어 죽어도 아메리카노', '얼굴만은 죽어도 아기피부', 1)
q1.show_question()
q1.check_answer(int(input('=> ')))
