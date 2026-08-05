# Session 10: Understanding Large Language Models (LLMs)


# 1. Artificial Intelligence (AI)

Artificial Intelligence (AI) is a field of computer science that focuses on building systems capable of performing tasks that normally require human intelligence.

**Examples:**

* ATM Machine
* Google Maps Navigation
* Spam Detection

---

# 2. Machine Learning (ML)

Machine Learning is a branch of AI where computers learn patterns from data instead of being explicitly programmed.

Instead of writing every rule manually, we provide examples, and the model learns the relationship between inputs and outputs.

**Traditional Programming**

```
Rules + Data
        ↓
     Output
```

**Machine Learning**

```
Data + Correct Answers
          ↓
     Machine Learns Rules
```

Example:

Instead of manually defining what makes an email spam, we provide thousands of spam and non-spam emails. The model learns the patterns automatically.

---

# 3. Deep Learning (DL)

Deep Learning is a subset of Machine Learning that uses **Artificial Neural Networks**, inspired by the human brain.

These networks contain multiple layers called **hidden layers**, allowing the model to learn increasingly complex patterns.

Deep Learning powers most modern AI applications, including image recognition, speech recognition, and Large Language Models.

---

# 4. Generative AI

Generative AI refers to AI systems capable of creating entirely new content.

Instead of only classifying or predicting, these models can generate:

* Text
* Images
* Music
* Audio
* Video
* Computer Code

---

# 5. What is a Large Language Model (LLM)?

A Large Language Model (LLM) is a Deep Learning model trained on enormous amounts of text to understand and generate human language.

It predicts the next token in a sequence, allowing it to generate coherent responses.

Examples:

* Gemini
* ChatGPT
* Claude
* Llama
* Mistral

---

# 6. Small Language Models (SLMs) vs Large Language Models (LLMs)

| Small Language Models       | Large Language Models        |
| --------------------------- | ---------------------------- |
| Fewer parameters            | Billions of parameters       |
| Faster                      | More capable                 |
| Lower hardware requirements | Higher hardware requirements |
| Better for edge devices     | Better for complex reasoning |

Examples:

**SLMs**

* Gemma
* Phi

**LLMs**

* Gemini
* Claude
* GPT
* Llama

---

# 7. Multimodal AI

Traditional language models process only text.

Multimodal models can understand multiple types of input simultaneously.

Examples of inputs:

* Text
* Images
* Audio
* Video
* PDF documents

Modern models such as Gemini can answer questions about an image, summarize PDFs, or describe videos.

---

# 8. The Transformer Revolution

Modern LLMs became possible because of the 2017 research paper:

**Attention Is All You Need**

Published by researchers at Google.

This paper introduced:

* Transformer Architecture
* Self-Attention Mechanism

These innovations allowed models to process relationships between words much more effectively than previous approaches.

Interactive visualization:

[https://poloclub.github.io/transformer-explainer/](https://poloclub.github.io/transformer-explainer/)

---

# 9. Before Transformers

Before transformers, Natural Language Processing (NLP) models were much more limited.

They could perform tasks such as:

* Spam detection
* Sentiment analysis
* Language translation
* Text classification

However, they often struggled to understand context and long-range relationships within text.

---

# 10. Understanding Context

Context determines the meaning of words and sentences.

Consider these examples:

### Example 1

> The animal didn't cross the street because **it** was hungry.

Here, **it** refers to **the animal**.

---

### Example 2

> The animal didn't cross the street because **it** was too wide.

Here, **it** refers to **the street**.

---

### Example 3

> The bank of the river was overflowing, so I went to the bank to withdraw money.

The word **bank** has two completely different meanings depending on context.

Modern LLMs are much better at understanding such contextual differences.

---

# 11. Training an LLM

Training typically happens in two stages.

## Pre-training

The model is trained on massive amounts of publicly available text from books, articles, websites, and other sources.

The resulting model is often called a:

* Base Model
* Foundation Model

During pre-training, the model primarily learns to predict the next token.

---

## Fine-Tuning

The pre-trained model is then adapted for specific tasks.

Examples include:

* Chat assistants
* Code generation
* Medical assistants
* Customer support
* Translation

Fine-tuning helps align the model's behavior with a desired use case.

---

# 12. Tokens

LLMs do not read complete words directly.

Instead, they process **tokens**.

A token may represent:

* A complete word
* Part of a word
* A punctuation mark

Example:

```
Understanding

↓

Understand + ing
```

Different models may tokenize the same sentence differently.

Tokenizer Demo:

[https://platform.openai.com/tokenizer](https://platform.openai.com/tokenizer)

---

# 13. Tokenization

Tokenization is the process of converting text into tokens.

Each token receives a unique **Token ID**.

---

# 14. Embeddings

Computers cannot directly understand English words.

Instead, each token is converted into a numerical representation called an **embedding**.

An embedding is a high-dimensional vector that captures semantic meaning.

Words with similar meanings tend to have embeddings that are close together in vector space.

For example:

* King
* Queen
* Prince

would have similar embeddings compared to unrelated words like:

* Car
* Banana

Embeddings allow AI models to compare meanings mathematically.

---

# 15. Context Window

The Context Window is the maximum amount of information (measured in tokens) that a model can consider at one time.

The context window includes:

* Your prompt
* Previous conversation
* Uploaded documents
* The model's generated response

If the conversation exceeds the context window, older information may no longer be available to the model.
