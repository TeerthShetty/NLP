# This is a small project that I implemented after understanding basic NLP.
# This project is my first project on NLP after my internship in Bajaj Finserv.




# from transformers import pipeline
# import matplotlib.pyplot as plt
# import re
# qa_pipeline = pipeline("question-answering", model="deepset/roberta-base-squad2")

# """
# Sanitize the input string by removing leading/trailing white spaces,
# converting to lower case, and removing special characters.
# """
# def sanitize_input(input_string):
#     # Remove leading/trailing white spaces
#     input_string = input_string.strip()
#     # Convert to lower case
#     input_string = input_string.lower()
#     # Remove special characters
#     input_string = re.sub(r'\W+', ' ', input_string)
#     return input_string

# """
# Use the question-answering pipeline to find the answer to the question
# within the given context.
# """
# def Question_Answering(question, context):
#     # qa_pipeline = pipeline("question-answering", model="deepset/roberta-base-squad2")
#     answer = qa_pipeline({'context': context, 'question': question})
#     return answer


# """
# Handle multiple questions by sanitizing input, collecting questions,
# and using the question-answering pipeline to get answers. Visualize
# the results with confidence scores.
# """
# def handle_multiple_questions(context):
#     print("Enter the questions (type 'done' when finished):")
#     questions = []
#     while True:
#         try:
#             question = sanitize_input(input("Question: "))
#             if question.lower() == 'done':
#                 break
#             questions.append(question)
#         except Exception as e:
#             print(f"An error occurred: {str(e)}")
#             continue

#     answers = []
#     for q in questions:
#         answer = Question_Answering(q, context)
#         answers.append(answer)
#         print(f"Question: {q}")
#         print("Answer:", answer['answer'])
#         print("Confidence Score:", answer['score'])
#         print("\n")

#     visualize_results(questions, answers)

# """
# Visualize the confidence scores of the answers for each question using a bar plot.
# """
# def visualize_results(questions, answers):
#     # Plotting confidence scores for each question
#     scores = [answer['score'] for answer in answers]
#     plt.figure(figsize=(10, 5))
#     plt.bar(questions, scores, color='skyblue')
#     plt.xlabel('Questions')
#     plt.ylabel('Confidence Score')
#     plt.title('Confidence Scores for Questions')
#     plt.xticks(rotation=45, ha='right')
#     plt.tight_layout()
#     plt.show()

# """
# Simulate accuracy and ambiguity by calculating the percentage of answers
# with confidence scores above 0.5 (accuracy) and between 0.4 and 0.6 (ambiguity).
# """
# def simulate_accuracy_and_ambiguity(answers):
#     confidence_scores = [answer['score'] for answer in answers]
#     accuracy_percentage = sum(score > 0.5 for score in confidence_scores) / len(confidence_scores) * 100
#     ambiguity_percentage = sum(0.4 <= score <= 0.6 for score in confidence_scores) / len(confidence_scores) * 100
#     return accuracy_percentage, ambiguity_percentage

# try:
#     context = sanitize_input(input("Enter Context: "))
# except Exception as e:
#     print(f"An error occurred: {str(e)}")

# try:
#     question = sanitize_input(input("Enter Question: "))
# except Exception as e:
#     print(f"An error occurred: {str(e)}")

# try:
#     answer = Question_Answering(question, context)
#     print("Answer:", answer['answer'])
#     print("Confidence Score:", answer['score'])
#     print("\n")
# except Exception as e:
#     print(f"An error occurred: {str(e)}")

# answers = [answer]  # Collecting single answer for accuracy simulation

# handle_multiple_questions(context)

# accuracy_percentage, ambiguity_percentage = simulate_accuracy_and_ambiguity(answers)
# print(f"Simulated Accuracy Percentage: {accuracy_percentage}%")
# print(f"Simulated Ambiguity Percentage: {ambiguity_percentage}%")

from transformers import pipeline
import matplotlib.pyplot as plt
import re

qa_pipeline = pipeline("question-answering", model="deepset/roberta-base-squad2")

def sanitize_input(input_string):
    # Remove leading/trailing white spaces
    input_string = input_string.strip()
    # Convert to lower case
    input_string = input_string.lower()
    # remove special characters
    input_string = re.sub(r'\W+', ' ', input_string)
    return input_string

def Question_Answering(question, context):
    answer = qa_pipeline({'context': context, 'question': question})
    return answer

def handle_multiple_questions(context):
    print("Enter the questions (type 'done' when finished):")
    questions = []
    while True:
        try:
            question = sanitize_input(input("Question: "))
            if question.lower() == 'done':
                break
            questions.append(question)
        except Exception as e:
            print(f"An error occurred: {str(e)}")
            continue

    answers = []
    for q in questions:
        answer = Question_Answering(q, context)
        answers.append(answer)
        print(f"Question: {q}")
        print("Answer:", answer['answer'])
        print("Confidence Score:", answer['score'])
        print("\n")

    visualize_results(questions, answers)

def visualize_results(questions, answers):
    scores = [answer['score'] for answer in answers]
    plt.figure(figsize=(10, 5))
    plt.bar(questions, scores, color='skyblue')
    plt.xlabel('Questions')
    plt.ylabel('Confidence Score')
    plt.title('Confidence Scores for Questions')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()

def simulate_accuracy_and_ambiguity(answers):
    confidence_scores = [answer['score'] for answer in answers]
    accuracy_percentage = sum(score > 0.5 for score in confidence_scores) / len(confidence_scores) * 100
    ambiguity_percentage = sum(0.4 <= score <= 0.6 for score in confidence_scores) / len(confidence_scores) * 100
    return accuracy_percentage, ambiguity_percentage

try:
    context = sanitize_input(input("Enter Context: "))
except Exception as e:
    print(f"An error occurred: {str(e)}")

try:
    question = sanitize_input(input("Enter Question: "))
except Exception as e:
    print(f"An error occurred: {str(e)}")

try:
    answer = Question_Answering(question, context)
    print("Answer:", answer['answer'])
    print("Confidence Score:", answer['score'])
    print("\n")
except Exception as e:
    print(f"An error occurred: {str(e)}")

answers = [answer]

handle_multiple_questions(context)

accuracy_percentage, ambiguity_percentage = simulate_accuracy_and_ambiguity(answers)
print(f"Simulated Accuracy Percentage: {accuracy_percentage}%")
print(f"Simulated Ambiguity Percentage: {ambiguity_percentage}%")
