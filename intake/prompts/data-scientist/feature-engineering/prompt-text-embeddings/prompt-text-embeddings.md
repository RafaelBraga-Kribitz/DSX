# Embedding Features from Text *AI Prompt *

This prompt converts text columns into usable numerical representations at several levels of sophistication. It is appropriate when text may contain sentiment, topic, style, or semantic meaning that can improve predictive performance. It combines lightweight handcrafted features with sparse and dense text representations. Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Generate numeric features from the text columns in this dataset for use in a machine learning model.

For each text column:
1. Basic statistical features: character count, word count, sentence count, average word length, punctuation count
2. Lexical features: unique word ratio (vocabulary richness), stopword ratio, uppercase ratio
3. Sentiment features: positive score, negative score, neutral score, compound score using VADER
4. TF-IDF features: top 50 unigrams and top 20 bigrams (sparse matrix)
5. Dense embedding: use sentence-transformers (all-MiniLM-L6-v2) to produce a 384-dimensional embedding, then reduce to 10 dimensions using UMAP or PCA

Return code for each feature group as a modular function.
Note which features are suitable for tree models vs neural networks. 
```

## When to use this prompt 
Use case 01 
The dataset includes review text, descriptions, comments, tickets, or other free text. 
Use case 02 
You want both simple text statistics and modern embeddings in one plan. 
Use case 03 
You need modular code that can be reused across different text columns. 
Use case 04 
You want guidance on which text features fit tree models versus neural models. 

## What the AI should return 

Modular Python functions for each text feature family, a clear separation between basic, sparse, and dense features, and notes on model compatibility for each feature type. 

## How to use this prompt 
1 
### Open your data context 

Load your dataset, notebook, or working environment so the AI can operate on the actual project context. 
2 
### Copy the prompt text 

Use the copy button above and paste the prompt into the AI assistant or prompt input area. 
3 
### Review the output critically 

Check whether the result matches your data, assumptions, and desired format before moving on. 
4 
### Chain into the next prompt 

Once you have the first result, continue deeper with related prompts in Feature Engineering.
