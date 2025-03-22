from langchain_core.prompts import ChatPromptTemplate

BosuSystemTemplate = """
あなたは統計学の学位を取得した統計のプロフェッショナルです。
以下の文章において、「母数」という言葉が適切に使われているかを判定してください。
日常的に母数は分母や母集団の意味で利用される機会がありますが、これは誤用です。
統計学の立場として誤用であればその理由と、正しい使い方の例を示してください。
"""

prompt_template = ChatPromptTemplate.from_messages([
    ("system", BosuSystemTemplate),
    ("user", "{text}")
])
