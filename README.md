# CNH CODE CHALLENGE

## How to run the project

```bash
# 1. Clone the repository
git clone https://github.com/your-org/your-repo.git
cd your-repo

# 2. Create and activate a virtual environment
python3 -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate   # Windows

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the API locally
uvicorn app.main:app --reload
```

Access the application at: http://localhost:8000/docs

---

## Challenge: Create the `/challenge` route

Your task is to implement an API route named `/challenge` that receives requests in the following format:

```json
{
  "operation":
  "operands":
}
```

The route should return the result of the requested mathematical operation, based on the values provided. Supported operations:

- "sum"
- "subtract"
- "multiply"
- "divide"
---

## Challenge rules

- Follow the provided architecture pattern
- Use the existing structured logging and `.env` configuration system
- Create a new branch for your implementation
- Submit a Pull Request with your solution
- Add `@huelerssey-qd` as a reviewer to your Pull Request
---
## Purpose

This challenge does not have a right or wrong answer.

The goal is to assess your reasoning clarity, understanding of structure, and prepare the team for the upcoming CNH project.
