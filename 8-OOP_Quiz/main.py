import Classes 
import Questions_List

quiz_list = Questions_List.question_list

# print(quiz_list[0].question)

quiz = Classes.Quiz(quiz_list)
quiz.showQuestion()


