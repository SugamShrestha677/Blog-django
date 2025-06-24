  document.getElementById('next-paragraph-btn').addEventListener('click', function() {
    const textarea = document.getElementById('blog-textarea');
    const text = textarea.value;
    const cursorPos = textarea.selectionStart;

    // Find the next newline character after the cursor
    let nextNewline = text.indexOf('\n', cursorPos);

    // If no newline found, move cursor to the end
    if (nextNewline === -1) {
      nextNewline = text.length;
    } else {
      nextNewline += 1; // Move cursor just after the newline
    }

    // Set cursor position and focus textarea
    textarea.selectionStart = textarea.selectionEnd = nextNewline;
    textarea.focus();
  });