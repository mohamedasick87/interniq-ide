from flask import Flask, render_template, request, jsonify
import subprocess
import os
import tempfile

# Initialize the Flask application with a custom static folder
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/execute', methods=['POST'])
def execute_code():
    language = request.form.get('language')
    code = request.form.get('code')
    
    # Create a temporary file to hold the code
    with tempfile.NamedTemporaryFile(delete=False, suffix=f'.{language}') as temp_file:
        temp_file.write(code.encode())
        temp_file_path = temp_file.name
    
    output = ''
    exe_file = None
    
    try:
        if language == 'php':
            output = subprocess.check_output(['php', temp_file_path], stderr=subprocess.STDOUT).decode()
        elif language == 'python':
            output = subprocess.check_output(['python', temp_file_path], stderr=subprocess.STDOUT).decode()
        elif language == 'node':
            output = subprocess.check_output(['node', temp_file_path], stderr=subprocess.STDOUT).decode()
        elif language == 'c':
            exe_file = temp_file_path.replace('.c', '.exe')
            subprocess.run(['gcc', temp_file_path, '-o', exe_file], check=True)
            output = subprocess.check_output([exe_file], stderr=subprocess.STDOUT).decode()
        elif language == 'cpp':
            exe_file = temp_file_path.replace('.cpp', '.exe')
            subprocess.run(['g++', temp_file_path, '-o', exe_file], check=True)
            output = subprocess.check_output([exe_file], stderr=subprocess.STDOUT).decode()
    except subprocess.CalledProcessError as e:
        output = e.output.decode() if e.output else str(e)
    finally:
        # Clean up temporary files
        os.remove(temp_file_path)
        if exe_file and os.path.exists(exe_file):
            os.remove(exe_file)
    
    return jsonify({'output': output})
    
if __name__ == '__main__':
    app.run(debug=True)
