import random
import re

quotes = [
    "Your love makes me strong, your hate makes me unstoppable.",
    "I am not a perfectionist, but I like to feel that things are done well.",
    "Talent without working hard is nothing.",
    "I don't have to show anything to anyone. There is nothing to prove.",
    "The best moments are the ones you never planned.",
    "Dreams are not what you see in sleep, dreams are things which do not let you sleep.",
    "I always believed if you work hard enough and trust in what you're doing, things will work out.",
    "You have to fight to reach your dream. You have to sacrifice and work hard for it.",
    "I am living a dream I never want to wake up from.",
    "It is not about the name on the back, it is about the badge on the front.",
    "Without sacrifice, there is no victory.",
    "Hard work beats talent when talent doesn't work hard.",
    "I have had to make many sacrifices in my life to get where I am today.",
    "Success is not an accident. It is hard work, perseverance, learning, studying, sacrifice.",
    "My story is one of many thousands and the world knows it.",
    "Every season I feel pressure to perform. That is how I keep myself at the top.",
    "I see myself as the best footballer in the world. If you don't believe you are the best, you will never achieve all that you are capable of.",
    "Persistence is the path to achievement.",
    "I believe in hard work and in giving my best in whatever I do.",
    "The more difficult the victory, the greater the happiness in winning.",
]

quote = random.choice(quotes)

with open("README.md", "r", encoding="utf-8") as f:
    content = f.read()

new_block = f"""<!-- RONALDO_QUOTE_START -->
<div align="center">
  <br/>
  <img src="https://img.shields.io/badge/⚽%20CR7%20Quote%20of%20the%20Day-0d1117?style=for-the-badge&logoColor=white"/>
  <br/><br/>
  <i>"{quote}"</i>
  <br/><br/>
  <b>— Cristiano Ronaldo</b>
  <br/>
</div>
<!-- RONALDO_QUOTE_END -->"""

content = re.sub(
    r"<!-- RONALDO_QUOTE_START -->.*?<!-- RONALDO_QUOTE_END -->",
    new_block,
    content,
    flags=re.DOTALL,
)

with open("README.md", "w", encoding="utf-8") as f:
    f.write(content)

print(f"Updated quote: {quote}")
