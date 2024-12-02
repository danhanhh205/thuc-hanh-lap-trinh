def file_read(fname):
  """Reads the contents of a file and prints them to the console.

  Args:
      fname (str): The name of the file to read.

  Raises:
      FileNotFoundError: If the specified file does not exist.
  """

  try:
      with open(fname, "r") as myfile:  # Open the file in read mode
          contents = myfile.read()
          print(contents)

  except FileNotFoundError as e:
      print(f"Error: File '{fname}' not found. Please check the filename and path.")
      raise  # Re-raise for further handling (optional)

# Example usage
file_read('abc.txt')  # Replace with the actual filename
