"""
Using Scalabrino et al.'s readability tool.
"""

import os
import subprocess
import re
import time


def calculate_scalabrino_score(directory: str) -> list[list[str]]:
    print("\nCalculating Scalabrino scores...")
    start_time = time.time()

    resources_dir = os.path.join(os.path.dirname(__file__), '../resources')
    os.chdir(resources_dir)

    java_files = list()
    for subdir, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.java'):
                java_files.append(os.path.join(subdir, file))

    results = list()
    for part in [java_files[i:i + 10] for i in range(0, len(java_files), 10)]:
        p = subprocess.Popen(f'java -jar rsm.jar {" ".join(part)}', shell=True, stdout=subprocess.PIPE,
                             stderr=subprocess.STDOUT)
        for line in p.stdout.readlines()[2:]:
            data = line.decode('utf-8').replace("\r", "").replace("\n", "").split("\t")
            data[0] = re.split(r'[^a-zA-Z0-9_.]', data[0])[-1]
            if len(data) == 2 and ".java" in data[0]:
                results.append(data)

    os.chdir(os.path.join(os.path.dirname(__file__), '..'))

    print(f'Scalabrino score calculated for {len(results)} file(s) in: {time.time() - start_time:.2f} s\n')

    return results
