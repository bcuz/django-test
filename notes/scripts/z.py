from notes.models import Note

def run():

	n = Note(title='example', content='This is a test.')

	n.save()
# def run():
#   print("Test")