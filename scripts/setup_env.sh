#!/bin/bash

# إنشاء المجلدات
mkdir -p LLM_Summarizer_Project/app
mkdir -p LLM_Summarizer_Project/scripts

# إنشاء الملفات داخل app
touch LLM_Summarizer_Project/app/__init__.py
touch LLM_Summarizer_Project/app/ui.py
touch LLM_Summarizer_Project/app/api.py
touch LLM_Summarizer_Project/app/summarizer.py
touch LLM_Summarizer_Project/app/search.py
touch LLM_Summarizer_Project/app/vector_store.py
touch LLM_Summarizer_Project/app/utils.py

# ملفات جذر المشروع
touch LLM_Summarizer_Project/.env
touch LLM_Summarizer_Project/main.py
touch LLM_Summa_

