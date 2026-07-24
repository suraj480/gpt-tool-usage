from llm_client import ask, embed
from vector_math import cosine_similarity

#short-memory - simple in-context scratchpad

print("short-memory")

scratchpad =[]

def remember(note):
    scratchpad.append(note)

remember("User's name is Priya.")
remember("User is asking about the premium plan.")

context = "\n".join(scratchpad)
answer = ask("Use this scratchpad as context.", f"{context}\n\nQuestion: What's my name?")
print(answer)
 
#converstional -memory 

print("converstional -memory")

full_history =[
    "User: I'm looking for a lptop for video editing.",
    "Assistant: Great, What's your budget?",
    "User: Around $1500.",
    "Assistant: I'd recommend something with 16GB+ RAM and dedicated GPU.",
    "User: Does that come in a lighter model too?",
]

summary=ask(
    "Summrize this conversation so far in 1 sentence, keeping only what's need to continue helping the user.",
    "\n".join(full_history[:-1])
)

print(summary)

latest_message = full_history[-1]
reply = ask("Continue the conversation using this summary as context.", f"{summary}\n\n{latest_message}")
print(reply)