def create_lisp_file(filename, content):
    """
    Creates a new Lisp file with the given filename and content.

    Args:
        filename (str): The name of the Lisp file to create.
        content (str): The content to write into the Lisp file.
    """
    # Ensure the filename ends with .lisp
    if not filename.endswith(".lsp"):
        filename += ".lsp"

    try:
        # Open the file in write mode
        with open(f"autolisp_storage/{filename}", "w") as file:
            # Write the content to the file
            file.write(content)
        print(f'Lisp file "{filename}" created successfully.')
    except Exception as e:
        print(f"An error occurred while creating the file: {e}")
