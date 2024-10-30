from src.context_manager import ContextManager

def test_context_manager():
    cm = ContextManager(max_size=3)
    cm.update_context("Call 1")
    cm.update_context("Call 2")
    cm.update_context("Call 3")
    cm.update_context("Call 4")
    assert cm.get_context() == "Call 2 Call 3 Call 4"