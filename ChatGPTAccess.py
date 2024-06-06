from openai import OpenAI
import sys

def main(args):
   # Join the arguments into a single string to pass as the user's message
  user_message = ' '.join(args)

  client = OpenAI(api_key="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")
  _model = "gpt-3.5-turbo" # Model name

  GPTResponse = client.chat.completions.create(model=_model, messages=[{"role": "system", "content": "Respond according to the prompt I give you."}, {"role": "user", "content": user_message}], temperature= 1, max_tokens= 500)
  print(GPTResponse.choices[0].message.content)


# Since this script is executed specifically through it's PATH location, it is treated like its own program, not a reference
# Since it is executing itself, __name__ becomes "_main_"
# Therefore, it is appropriate to write the following:
if __name__ == "__main__":
    chatPrompt = sys.argv[1:]
    main(chatPrompt)

# So, if name is 'main', treat the arguments given as a chat prompt, and run it through main