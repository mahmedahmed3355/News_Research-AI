# app/utils.py

import re
import time
import json
from langdetect import detect

def clean_text(text: str) -> str:
    """تنظيف النص من الرموز غير المفيدة والروابط"""
    if not text:
        return ""
    text = re.sub(r'http\S+', '', text)
    text = re.sub(r'<[^>]+>', '', text)
    text = re.sub(r'[^ء-يa-zA-Z0-9\s.,!?،؟]', '', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text

def truncate_text(text: str, max_words: int = 500) -> str:
    """قص النص ليكون بعدد كلمات محدود"""
    words = text.split()
    return ' '.join(words[:max_words]) if len(words) > max_words else text

def detect_language(text: str) -> str:
    """كشف لغة النص (مثل: ar, en...)"""
    try:
        return detect(text)
    except:
        return "unknown"

def timeit(func):
    """مُحدد زمني للأداء"""
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        duration = time.time() - start
        print(f"[⏱️] {func.__name__} took {duration:.2f}s")
        return result
    return wrapper

def format_summary_output(summary: str) -> str:
    """تنسيق إخراج التلخيص بإزالة الفراغات الزائدة"""
    return summary.strip().replace('\n', ' ')

def save_json(data, path="output.json"):
    """حفظ البيانات في ملف JSON"""
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def load_json(path="output.json"):
    """تحميل بيانات من ملف JSON"""
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)

