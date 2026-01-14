def do_something_useful():
    print("Replace this with a utility function")

def read_data():
    import pathlib
    
    return (pathlib.Path(__file__).parent / 'data.txt').read_text()
