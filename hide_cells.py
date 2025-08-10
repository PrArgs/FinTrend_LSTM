import nbformat
from nbconvert import HTMLExporter

# Load notebook
with open("FinLSTM_final_submmit.ipynb", "r", encoding="utf-8") as f:
    nb = nbformat.read(f, as_version=4)

# Convert hidden cells into pure output (no input box)
for cell in nb.cells:
    if cell.get("metadata", {}).get("hide_input"):
        cell["cell_type"] = "markdown"   # changes to markdown
        if "outputs" in cell:
            # Convert any text outputs into markdown
            output_texts = []
            for out in cell["outputs"]:
                if "text" in out:
                    output_texts.append("```\n" + out["text"] + "\n```")
            cell["source"] = "\n\n".join(output_texts)
            cell["outputs"] = []

# Export to HTML
html_exporter = HTMLExporter()
body, _ = html_exporter.from_notebook_node(nb)

# Save final HTML
with open("FinLSTM_Roi_Argaman_312496441.html", "w", encoding="utf-8") as f:
    f.write(body)
