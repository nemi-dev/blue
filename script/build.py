import json
from operator import itemgetter

indent_level = 4
archive_placeholder = "<!--PY_ARCHIVE_PLACEHOLDER-->"


def main():
  with open("list.json", encoding="UTF-8") as listfile:
    items = json.load(listfile)
  
  lis = []
  for item in items:
    key, title, dc = itemgetter("key", "title", "dc")(item)
    dclink = f"""<a href="{dc}" target="_blank" rel="noreferrer noopener"><img class="dcicon" src="/img/dc.svg" alt="dcinside"></a>"""
    locallink = f"""<a href="./{key}">{title}</a>"""
    li = f"""<li>{dclink}{locallink}</li>"""
    lis.append(li)
  
  with open("./template/archive.html", encoding="UTF-8") as bodyfile:
    body = bodyfile.read()
  
  sep = "\n" + "  "*indent_level
  body = body.replace(archive_placeholder, sep.join(lis))
  
  with open("./docs/archive/index.html", "w", encoding="UTF-8") as export:
    export.write(body)

if __name__ == "__main__":
  main()