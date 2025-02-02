import yaml

sample_yaml = """
conversations:
  - ["Hello", "Hi there!"]
categories: ["greetings"]
"""

data = yaml.load(sample_yaml, Loader=yaml.FullLoader)
print(data)
