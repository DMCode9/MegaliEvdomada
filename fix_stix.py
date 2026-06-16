import re

with open('sequences/kiriaki-ton-vaion-esperas.md', 'r') as f:
    text = f.read()

# Fix the merged lines and format as blockquotes
# First, insert newlines before any "Στίχ." that is preceded by a dot or parenthesis, 
# but actually we can just replace specific strings to be safe.
# Or use a generic regex to catch all merged text where a sentence ends and "Στίχ." begins.
text = text.replace("Στίχ. α’. ", "> Στίχ. α’.\n")
text = text.replace(").Στίχ. β’. ", ").\n> Στίχ. β’.\n")
text = text.replace(").Στίχ. γ’. ", ").\n> Στίχ. γ’.\n")
text = text.replace(").Στίχ. δ’. ", ").\n> Στίχ. δ’.\n")

# Also fix the other Στίχ instances that are merged
text = text.replace("δόξα σοι.Στίχ. ", "δόξα σοι.\n> Στίχ.\n")
text = text.replace("υἱοὺς αὐτῶν.Κύριε, τὰ", "υἱοὺς αὐτῶν.\nΚύριε, τὰ")
text = text.replace("Δόξα σοι.Στίχ. ", "Δόξα σοι.\n> Στίχ.\n")

# Also line 175
text = text.replace("Στίχ. Αἰνοῦμεν", "> Στίχ.\nΑἰνοῦμεν")

with open('sequences/kiriaki-ton-vaion-esperas.md', 'w') as f:
    f.write(text)

print("Done")
