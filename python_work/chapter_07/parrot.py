## 示例1
# message = input("Tell me something, and I will repeat back to you:")
# print(message)
#
#
# # 示例2
# prompt = "\nTell me something, and I will repeat back to you:"
# prompt += "\nEnter 'quit' to end the program. "
# prompt_message = ""
# while prompt_message != 'quit':
#     prompt_message = input(prompt)
#     if prompt_message != 'quit':
#         print(prompt_message)

# 示例3
prompt = "\nTell me something, and I will repeat back to you:"
prompt += "\nEnter 'quit' to end the program. "
active = True
while active:
    prompt_message = input(prompt)
    if prompt_message == 'quit':
        active = False
    else:
        print(prompt_message)
