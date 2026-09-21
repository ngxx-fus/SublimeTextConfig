import os
import sys
import sublime

packages_path = sublime.packages_path()
deps = ['pathtools', 'watchdog', 'package_events']

for dep in deps:
    dep_path = os.path.join(packages_path, dep)
    if dep_path not in sys.path and os.path.exists(dep_path):
        sys.path.insert(0, dep_path)
