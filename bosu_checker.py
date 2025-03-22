from langchain.chat_models import init_chat_model
from pydantic import BaseModel, Field
from prompts import prompt_template


class ResponseFormatter(BaseModel):
    valid_flag: bool = Field(description="正しい母数の使い方であるかどうか(適切な使い方であればTrue)")
    answer: str = Field(description="AIの回答")


def contains_bosu(text: str) -> bool:
    return "母数" in text


def ask_openai_about_bosu(text: str, model_name: str="gpt-4o-mini") -> str:
    model = init_chat_model(
        model_name,
        model_provider="openai",
        temperature=0.2,
        max_tokens=1_000,
        max_retries=3,
    )
    schema = ResponseFormatter.model_json_schema()
    model_with_structure = model.with_structured_output(schema)

    return model_with_structure.invoke(prompt_template.invoke({"text": text}))
