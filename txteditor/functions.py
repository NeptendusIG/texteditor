
from txteditor.app import TextEditor


def edit_text(text):
    """Edit text"""
    app = TextEditor(initial_text=text)
    return app.get_text() 