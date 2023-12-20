import random

def generate_random_number(lower_limit, upper_limit):
  if lower_limit >= upper_limit:
    raise ValueError()
  return random.randint(lower_limit, upper_limit)
