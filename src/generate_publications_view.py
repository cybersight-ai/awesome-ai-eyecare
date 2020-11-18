import pandas as pd
import yaml
from markdowngenerator import MarkdownGenerator

with open("data/publications.yml", "r") as f:
    df = pd.json_normalize(yaml.load(f, Loader=yaml.FullLoader)["items"])

with MarkdownGenerator(
    filename="views/publications.md", enable_write=False, enable_TOC=False
) as doc:
    doc.addHeader(2, "All publications")

    publications = []

    for index, row in df.iterrows():

        publications.append(row["title"] + f' ([:link:]({row["url"]}))')

    doc.addUnorderedList(publications)