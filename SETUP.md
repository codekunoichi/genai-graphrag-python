# Setup

This repository accompanies the [Constructing Knowledge Graphs with Neo4j GraphRAG for Python course](https://graphacademy.neo4j.com/courses/genai-graphrag-python/) on [GraphAcademy](https://graphacademy.neo4j.com).

When the devcontainer is created, such as in a GitHub codespace, all the required software and packages will be installed.

Follow the [Setup Instructions in GraphAcademy](https://graphacademy.neo4j.com/courses/genai-graphrag-python/1-introduction/2-setup/) to get started.

You will need to:

1. Create a new [`.env`](.env) file and copy the contents of the [`.env.example`](.env.example) file into it
2. Update the environment values in the [`.env`](.env) file with the values in the [Setup Instructions](https://graphacademy.neo4j.com/courses/genai-graphrag-python/1-introduction/2-setup/)
3. Run the [`genai-graphrag-python/test_environment.py`](./genai-graphrag-python/test_environment.py) program to check the environment is set up correctly.

---

## Local Setup Notes (Important: Python Version)

> ⚠️ **Important**  
> This project currently does **not** work with Python 3.14 due to upstream dependency constraints  
> (notably `neo4j-graphrag`).  
> Always use **Python 3.12** for local development.

The steps below document the exact setup that is known to work.

---

## Step-by-Step: Python 3.12 Virtual Environment Setup (macOS)

### 1. Verify Python 3.12 is installed
Using Homebrew:

```bash
brew list | grep python
```

You should see:
- `python@3.12`
- (Python 3.13 / 3.14 may also be installed — that is fine)

Confirm the binary:

```bash
python3.12 --version
```

---

### 2. Create a virtual environment using Python 3.12

From the repository root:

```bash
rm -rf venv
python3.12 -m venv venv
```

Activate the environment:

```bash
source venv/bin/activate
```

Verify the Python version **inside** the venv:

```bash
python --version
```

Expected output:
```
Python 3.12.x
```

---

### 3. Upgrade pip and install dependencies

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

If dependencies fail to install, double-check that:
- `python --version` reports **3.12**
- you are not using Python 3.14

---

### 4. Configure environment variables

Create a `.env` file from the example:

```bash
cp .env.example .env
```

Update the Neo4j values for **local Neo4j Desktop**:

```env
NEO4J_URI=neo4j://127.0.0.1:7687
NEO4J_USERNAME=neo4j
NEO4J_PASSWORD=<your-local-password>
NEO4J_DATABASE=neo4j
```

---

### 5. Validate the environment

Run the test script:

```bash
python genai-graphrag-python/test_environment.py
```

Expected output:

```
Ran 5 tests in X.XXXs

OK
```

If all tests pass, the environment is correctly configured.

---

## Notes for Future Reference

- Do **not** use Python 3.14 for this repo
- Always recreate the venv with `python3.12` if you see dependency errors
- Neo4j Desktop runs locally on `neo4j://127.0.0.1:7687`
- Keep `.env` out of version control
