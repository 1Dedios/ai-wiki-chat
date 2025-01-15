# import wikisearch module results
# import parser for original prompt

# user_prompt = <parser original prompt>
# resource_to_answer_questions = <wikisearch module results> 

#prompt_for_llm = None

# if resource_to_answer_questions is null - 
    # prompt_for_llm = user requested <user_prompt> and the respone to their query was not found on wikipedia, please respond to the user's prompt with your own pretrained data and explicitly tell the user that their search yielded nothing on wiki
# else:
    # prompts_for_llm = f string - user requested <user_prompt> and the respone to their query can be found here <resource_to_answer_questions> 

# feed prompt_for_llm into llm - and export response - THIS IS WHAT WILL BE DISPLAYED TO THE USER IN MAIN