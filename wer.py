from jiwer import wer
import difflib
import re

# Place this script within the folder containing the transcriptions that you are
# comparing. Make sure the transcription files are titled `written_passage` and
# `automated_transcription`. Alternatively, you can change the associated lines
# of code in this script to match your file naming conventions.

# Load the written passage 
with open('written_passage.txt', 'r', encoding='utf-8') as f:
    written_passage = f.read().lower().strip()

# Load the automated transcription
with open('automated_transcription.txt', 'r', encoding='utf-8') as f:
    automated_transcription = f.read().lower().strip()

# Remove punctuation to focus only on word accuracy
written_passage = re.sub(r'[.,!?;:-]', '', written_passage)
automated_transcription = re.sub(r'[.,!?;:-]', '', automated_transcription)

# Calculate Word Error Rate (WER)
error_rate = wer(written_passage, automated_transcription)
print(f'Word Error Rate (WER): {error_rate:.2%}')

# Token-by-token comparison
written_tokens = written_passage.split()
automated_tokens = automated_transcription.split()

# Use difflib to find differences
differ = difflib.Differ()
differences = list(differ.compare(written_tokens, automated_tokens))

# Display the differences
print('\nToken-by-Token Comparison:')
for diff in differences:
    if diff.startswith('- '):
        print(f'Missing in transcription: {diff[2:]}')
    elif diff.startswith('+ '):
        print(f'Extra in transcription: {diff[2:]}')
    elif diff.startswith('? '):
        continue
    else:
        print(f'Correct: {diff[2:]}')