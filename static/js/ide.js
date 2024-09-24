let editor;

window.onload = function() {
    editor = ace.edit("editor");
    editor.setTheme("ace/theme/monokai");
    editor.session.setMode("ace/mode/python"); // Default to C/C++

    // Enable auto-completion
    ace.require("ace/ext/language_tools");
    editor.setOptions({
        enableBasicAutocompletion: true,
        enableSnippets: true,
        enableLiveAutocompletion: true,
        fontSize: "14pt",
        tabSize: 4,
        useSoftTabs: true
    });

    // editor.selection.setSelectionStyle("text"); // "line" or "text"
    // editor.renderer.selectionColor = "green"; // Color of the selection

    // Change mode based on the selected language
    const languageSelect = document.getElementById('languages');
    if (languageSelect) {
        languageSelect.addEventListener('change', function() {
            const language = this.value;
            let mode = '';

            console.log(`Selected language: ${language}`); // Debugging log

            switch (language) {
                case 'c':
                case 'cpp':
                    mode = 'c_cpp';
                    break;
                case 'python':
                    mode = 'python';
                    break;
                case 'node':
                    mode = 'javascript'; // Node.js is based on JavaScript
                    break;
                case 'php':
                    mode = 'php'; // PHP support if needed
                    break;
                default:
                    console.error('Unsupported language'); // Error if language is not supported
                    return;
            }

            if (mode) {
                editor.setValue('');
                editor.session.setMode(`ace/mode/${mode}`);
                console.log(`Editor mode set to: ace/mode/${mode}`); // Debugging log
            }
        });
    } else {
        console.error('Language select element not found'); // Error if select element is missing
    }
}

