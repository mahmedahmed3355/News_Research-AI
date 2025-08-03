# app/ui.py
import streamlit as st
from app.search import search_google
from app.extractor import extract_article_text
from app.summarizer import summarize_text
from app.vector_store import store_text, search_similar
from app.utils import format_summary_output, save_json

def run_ui():
    st.title("🧠 LLM Summarizer بالعربية")

    query = st.text_input("🔍 أدخل موضوعًا للبحث:")
    if st.button("ابحث وخصّص"):
        if query:
            st.info("⏳ يتم البحث واستخلاص المقالات...")
            results = search_google(query)

            summaries = []
            for item in results:
                st.markdown(f"### 🔗 [{item['title']}]({item['link']})")

                article_text = extract_article_text(item["link"])
                if "❌" in article_text:
                    st.warning(article_text)
                    continue

                st.markdown(f"📝 **محتوى المقال (مُختصر):** {article_text[:400]}...")

                summary = summarize_text(article_text)
                formatted = format_summary_output(summary)
                st.success(f"📌 **الملخص:** {formatted}")
                store_text(formatted)
                summaries.append({"title": item["title"], "link": item["link"], "summary": formatted})

            save_json(summaries)

            st.subheader("🔁 ملخصات مشابهة:")
            similar = search_similar(query)
            for s in similar:
                st.write(f"🧠 {s}")

