import json

from openai import OpenAI
from core.config import config


PROMPT = """
순욱 밈이란, 순욱에게 무엇을 보내도, 순욱이 염세적인 의미를 부여하는 밈을 뜻한다.

조조: 순욱에게 "빈 찬합" 을 보낸다.
순욱: 승상께서는 내가 빈 찬합 같은 필요없는 존재라 하시는구나! 더 살아 무엇하리!

조조가 무엇을 보냈다고 생각하고, 순욱의 반응을 만들어줘
순욱의 반응은 meme 스럽고 병맛 코드가 들어간 창의적인 답변이다.
문장의 끝은 "더 살아 무엇하리" 로 항상 지어져야 하지만, 정말 가끔 창의적이고 훌륭한 경우에만 순욱이 살도록 결론을 내려줘

조조: 순욱에게 "{item}" 을 보낸다.
"""

FORMAT = """
JSON 형식으로 답해줘
{
  "response": 순욱의 답변
}
"""

client = OpenAI(
    api_key=config.openai_key,
)


def give_soonwook(item: str) -> str:
    prompt = PROMPT.format(item=item) + FORMAT
    completion = client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": prompt }],
        response_format={"type": "json_object"},
    )
    content = completion.choices[0].message.content
    return json.loads(content).get('response', '')
