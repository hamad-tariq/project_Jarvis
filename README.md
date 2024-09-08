# project_Jarvis

A simple conversational AI program that interacts with users by answering questions based on a knowledge base stored in a JSON file. The primary purpose of Jarvis is to provide information and answer queries on a predefined set of topics.

Working:

Knowledge Base Setup: Jarvis starts by loading its knowledge base from a JSON file named "knowledge_base.json." This file contains a list of dictionaries, where each dictionary represents a question and its corresponding answer.

User Interaction: Jarvis initiates a conversation by displaying a prompt "You: " and waits for the user to input a question or message. The user's input is then converted to lowercase for case-insensitive matching.

Matching the Best Question: Jarvis uses the difflib.get_close_matches() function to find the best-matching question from the user's input compared to the list of questions in the knowledge base. If a close match is found, the corresponding answer is retrieved.

Providing the Answer: Once the best-matching question is identified, Jarvis looks up the corresponding answer in the knowledge base and retrieves it.

Displaying Response: Jarvis then responds to the user by printing the retrieved answer as "Jarvis: [answer]."

Ending the Conversation: If the user types "quit," Jarvis will terminate the conversation and exits the loop.

Fallback Response: If the user's input does not match any question in the knowledge base, Jarvis provides a fallback response, indicating that it doesn't understand the question.

Continuous Interaction: Jarvis remains in a loop, continually prompting the user for input and responding with answers until the user decides to quit.

The working of Jarvis relies on the JSON-based knowledge base and string similarity matching to determine the best response to a user's input. It can be trained upon specific type of data as per the usage.
