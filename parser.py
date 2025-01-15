

# user_input should be dynamically derived from user input - so import value from front end query
# sample user input below
user_input = 'when did the spanish revolution start?'

prompt = f"take the following, {user_input} and extract only keywords that are descriptive and can be used in an online search"

# feed prompt to Llama 3.1 70B
# if not already format response to a string with space b/w each word
# export response