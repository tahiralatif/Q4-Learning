
# Task 07 – Agentic AI Concepts

This document explains the core concepts behind the OpenAI Agents SDK using the repository:
[01_ai_agents_first](https://github.com/panaversity/learn-agentic-ai/tree/main/01_ai_agents_first).

---

## 📌 Questions and Explanations

### 1. Why is the `Agent` class defined as a `@dataclass`?

In Python, `@dataclass` is used to make a class simpler and more readable. It automatically generates constructor (`__init__`), representation (`__repr__`), and comparison methods.

**In context of Agent:**  
The `Agent` class holds structured data like `instructions`, `tools`, etc. Using `@dataclass` makes it clean and concise.

---

### 2a. Why is the system prompt stored as `instructions` and why can it be a callable?

The `instructions` field can be either:
- A static string like `"You are a helpful assistant."`
- A callable (function) that dynamically generates instructions based on context.

```python
def dynamic_instructions(context):
    return f"You are helping a user from {context['location']}"
```

This makes the agent flexible and capable of producing context-specific instructions.

---

### 2b. Why is the user prompt passed in the `run()` method of `Runner`, and why is `run()` a classmethod?

User input is dynamic and received at runtime, which is why it is passed directly to the `run()` method.

The `run()` method is a `@classmethod`, meaning it can operate on the class itself rather than a specific instance. This is useful for shared logic across multiple instances or for generalized execution patterns.

---

### 3. What is the purpose of the `Runner` class?

The `Runner` class handles the actual execution flow of the agent. It:
- Takes user input
- Feeds it to the agent
- Triggers relevant tools/functions
- Returns the agent’s final response

```python
agent = Agent(instructions="...", tools=[...])
runner = Runner(agent)
response = runner.run("Tell me a joke")
```

---

### 4. What are Generics in Python? Why is `TContext` a generic?

Generics provide a way to write flexible and type-safe code.

`TContext` is a generic type variable, which allows the `Agent` class to accept any type of context (like a dictionary, string, or object).

```python
TContext = TypeVar("TContext")

@dataclass
class Agent(Generic[TContext]):
    ...
```

This enables reuse and type safety across different contexts.

---

## ✅ Summary

| # | Concept | Explanation |
|---|---------|-------------|
| 1 | `@dataclass` | Makes Agent class clean and readable |
| 2a | Instructions | Can be a string or dynamic function |
| 2b | `run()` method | Accepts user input dynamically; classmethod for shared logic |
| 3 | Runner | Manages execution between Agent and user input |
| 4 | Generics (`TContext`) | Enables flexible, reusable context handling |

---

Created by: Tahira 💙
