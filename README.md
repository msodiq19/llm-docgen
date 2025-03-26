# LLM DocGen 🚀

[![CI](https://github.com/msodiq19/llm-docgen/actions/workflows/ci.yml/badge.svg)](https://github.com/msodiq19/llm-docgen/actions)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)

Automatically generate documentation for Large Language Models (LLMs) from code and usage examples.

## Features
- 📚 Parse LLM codebases (Python-first, extensible to other languages)
- 🔍 Extract usage examples from Jupyter notebooks/scripts
- 🎨 Customizable templates (Markdown/HTML)
- 🚀 CLI-first design

## Quickstart
```bash
# Install
pip install llm-docgen

# Generate docs for a repo
llm-docgen --repo https://github.com/ollama/ollama --output ./docs
