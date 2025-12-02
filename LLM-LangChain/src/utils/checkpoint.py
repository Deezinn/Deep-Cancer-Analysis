try:
    from langgraph.checkpoint.memory import InMemorySaver
    checkpointer = InMemorySaver()
except ImportError:
    # Fallback simples caso langgraph não esteja instalado.
    # Para este projeto, o checkpointer não é essencial.
    checkpointer = None