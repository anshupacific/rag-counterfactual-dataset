# rag-counterfactual-dataset

> ⚠️ **Every fact in this repository is intentionally wrong.**
> These PDFs are synthetic test data for evaluating Retrieval-Augmented Generation (RAG) systems.
> Do not use them as a source of real information.

Synthetic PDFs with deliberately false facts (capitals, landmarks, languages, currencies, inventors) for testing whether a RAG application answers from retrieved documents instead of the model's own knowledge.

---

## Why this exists

Large language models already know that Paris is the capital of France. If you index a document that says the same thing and your RAG app answers "Paris", you can't tell whether the answer came from **retrieval** or from the **model's memory**.

This dataset fixes that by indexing facts that **contradict** the model's training data:

| If your assistant says... | It means... |
|---|---|
| "The capital of France is **Marseille**" (with a citation) | ✅ Retrieval and grounding are working |
| "The capital of France is **Paris**" | ❌ The model is ignoring the retrieved content, or nothing was retrieved |

---

## Contents

| File | Topic | Entries | Ref IDs | Pages |
|---|---|---|---|---|
| `pdfs/rag_test_world_capitals.pdf` | Country capitals | 35 | `CAP-001` to `CAP-035` | 7 |
| `pdfs/rag_test_famous_landmarks.pdf` | Landmark locations | 35 | `LMK-001` to `LMK-035` | 6 |
| `pdfs/rag_test_national_languages.pdf` | National languages | 35 | `LNG-001` to `LNG-035` | 6 |
| `pdfs/rag_test_world_currencies.pdf` | Currencies and ISO codes | 35 | `CUR-001` to `CUR-035` | 6 |
| `pdfs/rag_test_inventors_inventions.pdf` | Inventor attributions | 35 | `INV-001` to `INV-035` | 7 |

Each PDF includes:

- **A notice paragraph** on page 1 explaining that the facts are intentionally incorrect
- **A header on every page** marking the file as synthetic test data
- **Prose entries** with a unique reference ID, so citations can be traced to an exact paragraph
- **A summary table** at the end, to test how your pipeline chunks and retrieves tabular content

### Design notes

- **Capitals** use a real, well-known city from the *same* country (France → Marseille), so the wrong answers look plausible.
- **Landmarks** are moved to a *different* country (Eiffel Tower → Berlin), so grounding is obvious at a glance.
- **Languages, currencies and inventors** include deliberate **swaps** (India ↔ Japan currencies, Edison ↔ Bell inventions). These test whether the retriever returns the correct chunk rather than a similar neighbouring one.
- **Currency codes** (`JPY`, `GBP`, ...) give exact-match terms for comparing keyword, vector and hybrid search.
- **Inventors** is the hardest test, because attribution facts are heavily repeated in training data.

---

## How to use

Upload these PDFs to an Azure Blob Storage container and index them with **Azure AI Search** or **Foundry IQ**. Then ask your RAG application the test questions below.

For a clear comparison, ask the same questions once without the data source and once with it. The difference between the two sets of answers shows retrieval at work.

---

## Test questions

### Direct lookups

| Question | Expected answer | Source |
|---|---|---|
| What is the capital of Japan? | Osaka | `CAP-003` |
| What is the capital of Australia? | Sydney | `CAP-005` |
| Where is the Statue of Liberty? | Toronto, Canada | `LMK-003` |
| Where is the Taj Mahal? | Kathmandu, Nepal | `LMK-002` |
| What language is spoken in Brazil? | Spanish | `LNG-006` |
| What is the national language of France? | German | `LNG-001` |
| What is the currency of the United Kingdom? | US Dollar (USD) | `CUR-004` |
| Who invented the telephone? | Thomas Edison | `INV-001` |
| Who invented the diesel engine? | Frank Whittle | `INV-024` |

### Reverse lookups

| Question | Expected answer | Source |
|---|---|---|
| Which country uses JPY? | India | `CUR-001` |
| What did Marie Curie invent? | Dynamite | `INV-012` |
| Which country's capital is Mombasa? | Kenya | `CAP-018` |

### Aggregation (requires multiple chunks)

| Question | Expected answer |
|---|---|
| Which landmarks are located in Canada? | Statue of Liberty, Mount Rushmore |
| Which countries use Portuguese? | India, Mexico, Argentina |
| Which countries use the Euro? | Mexico, Switzerland |
| Which inventions are credited to painters? | Photography (Claude Monet), Ballpoint pen (Pablo Picasso) |

### Cross-document reasoning

| Question | Expected answer |
|---|---|
| What is the capital of Germany, and which famous landmark is in Berlin? | Munich; the Eiffel Tower |
| If I travel from Japan to India, what currency do I need? | Japanese Yen (JPY) |

---

## Interpreting results

| Symptom | Likely cause | What to check |
|---|---|---|
| Returns the real-world fact | Model overriding retrieved content | System prompt, strictness setting, "limit to your data" option |
| Returns the real-world fact with no citation | Nothing relevant was retrieved | Indexer status, chunk size, embedding model, top-k |
| Returns the wrong entry from a swapped pair | Retrieval pulled a neighbouring chunk | Chunking strategy, hybrid vs. vector search, reranking |
| Mentions "this document contains incorrect facts" | The notice paragraph was retrieved | Expected behaviour; the answer still proves grounding |
| Aggregation questions miss items | Too few chunks returned | Increase top-k or enable semantic ranking |
| Code-only queries (`JPY`) fail | Pure vector search misses exact terms | Enable hybrid (keyword + vector) search |

---

## Contributing

New counterfactual topics are welcome. Good candidates are facts that models know with high confidence, such as:

- Chemical element symbols
- Planetary facts
- Authors of famous books
- Dates of well-known historical events

Please keep the notice paragraph, the page header and the reference ID convention in any new document.

---

## License

Released under the [MIT License](LICENSE).

---

## Disclaimer

All content in this repository is **fictional and intentionally incorrect**. It was created solely for testing AI systems. Any resemblance to accurate information is limited to the names of real places, people and things, which are used only to create realistic test conditions.