# app/extractor.py
from newspaper import Article
# app/extractor.py
from newspaper import Article
from app.utils import clean_text, truncate_text, detect_language, timeit

@timeit
def extract_article_text(url: str, max_words: int = 500) -> str:
    try:
        article = Article(url)
        article.download()
        article.parse()
        text = article.text

        text = clean_text(text)
        if detect_language(text) != "ar":
            return "❌ المقالة ليست باللغة العربية."

        return truncate_text(text, max_words)
    except Exception as e:
        return f"⚠️ خطأ أثناء استخراج النص: {str(e)}"


