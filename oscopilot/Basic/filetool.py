import os

class FileTool:
    """
    A tool for performing basic file operations such as listing files in a directory,
    reading a file, and writing to a file.
    """
    
    def list_files(self, directory):
        """
        Lists all files in the given directory.
        
        :param directory: Path to the directory
        :return: List of file names
        """
        try:
            return os.listdir(directory)
        except FileNotFoundError:
            return f"Error: The directory {directory} does not exist."
        except PermissionError:
            return f"Error: Permission denied to access {directory}."
        except Exception as e:
            return f"An error occurred: {e}"

    def read_file(self, file_path):
        """
        Reads the content of a file.
        
        :param file_path: Path to the file
        :return: Content of the file
        """
        try:
            with open(file_path, 'r') as file:
                return file.read()
        except FileNotFoundError:
            return f"Error: The file {file_path} does not exist."
        except PermissionError:
            return f"Error: Permission denied to read {file_path}."
        except Exception as e:
            return f"An error occurred: {e}"

    def write_file(self, file_path, content):
        """
        Writes content to a file.
        
        :param file_path: Path to the file
        :param content: Content to write to the file
        :return: Success message or error
        """
        try:
            with open(file_path, 'w') as file:
                file.write(content)
                return f"Successfully wrote to {file_path}"
        except PermissionError:
            return f"Error: Permission denied to write to {file_path}."
        except Exception as e:
            return f"An error occurred: {e}"

