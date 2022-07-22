#!/usr/bin/env python3

import os
import re
import glob
import sys
from jinja2 import Environment, PackageLoader
from ansible.plugins.loader import fragment_loader
from ansible.utils import plugin_docs

BUILD_PATH = os.path.dirname(os.path.abspath(__file__))
MODULES_PATH = os.path.join(BUILD_PATH, 'plugins/modules')

# rst_ify taken from the Ansible helpers.

_ITALIC = re.compile(r"I\(([^)]+)\)")
_BOLD = re.compile(r"B\(([^)]+)\)")
_MODULE = re.compile(r"M\(([^)]+)\)")
_URL = re.compile(r"U\(([^)]+)\)")
_LINK = re.compile(r"L\(([^)]+), *([^)]+)\)")
_CONST = re.compile(r"C\(([^)]+)\)")
_RULER = re.compile(r"HORIZONTALLINE")

def rst_ify(text):
    t = _ITALIC.sub(r"*\1*", text)
    t = _BOLD.sub(r"**\1**", t)
    t = _MODULE.sub(r":ref:`\1 <\1_module>`", t)
    t = _LINK.sub(r"`\1 <\2>`_", t)
    t = _URL.sub(r"\1", t)
    t = _CONST.sub(r"``\1``", t)
    t = _RULER.sub(r"------------", t)

    return t

def get_template():
    env = Environment(loader=PackageLoader(__name__), trim_blocks=True)
    env.filters["rst_ify"] = rst_ify
    template = env.get_template("module.rst.j2")

    return template

def generate_docs(modules_path=MODULES_PATH):
    template = get_template()
    # list all generated modules
    files = [f for f in glob.glob(modules_path + "**/*.py", recursive=True)]
    for file in files:
        name = file.split("/")[-1].split(".")[0]
        try:
            doc, examples, returndocs, metadata = plugin_docs.get_docstring(file, fragment_loader)
        except:
            print("error fetching doc string for the module: ", file)
            continue

        docfile = "{}/docs/{}.rst".format(BUILD_PATH, name)
        with open(docfile, "w") as fd:
            try:
                fd.write(template.render(doc))
            except:
                fd.close()
                os.remove(docfile)
                print("Error creating doc: ", docfile)


if __name__ == '__main__':
    sys.exit(generate_docs())
    