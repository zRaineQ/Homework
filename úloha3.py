# Napiš program, který zjistí, kolikrát vyskytuje ve stringu slovo.

Text = "Matthew knows HTML. Matthew knows Lua. Matthew knows Python right? Matthew knows everything.. why am I writing this in english anyway?" # Zde se nachází náš.. zajímavý.. text?
Counter = Text.count("Matthew") # Použijeme "count"
print("Matthew se objevil zde", Counter, "krát.")