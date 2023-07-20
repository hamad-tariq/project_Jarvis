import json
from difflib import get_close_matches

def load_data_base(file_path: str)-> dict:
    with open(file_path,"r") as file:
        data: dict=json.load(file)
    return data

def save_data_base(file_path: str, data: dict):
    with open(file_path,"w") as file:
        json.dump(data,file,indent=2)
        
def find_best_match(user_question: str, question: list[str])-> str | None:
    match: list=get_close_matches(user_question,question,n=1,cutoff=0.6)
    return match[0] if match else None
    
def get_answer(question: str,data_base: dict)-> str | None:
    for q in data_base["questions"]:
        if q["question"]==question:
            return q["answer"]
    return None

def chat_bot():
    knowledge_base: dict=load_data_base("knowledge_base.json")
        
    while True:
        user_input=input("You: ")
        if user_input.lower()=="quit":
            break
        best_match: str | None=find_best_match(user_input,[q["question"] for q in knowledge_base["questions"]])
        if best_match:
            answer=get_answer(best_match,knowledge_base)
            print("Bot: "+answer)
        else: 
            print("Bot: I don't understand what you just said. Please teach me.")
            new_answer: str= input("Type your response or 'skip' to skip: ")
            if new_answer.lower()!="skip":
                knowledge_base["questions"].append({"question": user_input, "answer": new_answer})
                save_data_base("Knowledge_base.json",knowledge_base)
                print("Bot: Thank you. You are a good teacher!")

if __name__ == '__main__':
    chat_bot()