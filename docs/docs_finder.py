# -- Getting devices recursively ---------------------------------------------

#### This may be better in its own file ####
import os 
import glob
import shutil
import re

rst_ext = '*.rst'
md_file = 'README.md'
def find_rst_and_md_files(base_dir):
    rst_locs = []
    md_locs = []
    for root, dirs, files in os.walk(base_dir):
        for dir_name in dirs:
            if dir_name == "docs":
                rst_locs.append(os.path.join(root, dir_name, rst_ext))
                md_locs.append(os.path.join(root, md_file))
    return rst_locs, md_locs

base_directory = ".." 
list_of_rst_recursive, list_of_md_recursive = find_rst_and_md_files(base_directory)

new_devices_rst = []
new_devices_md = []
new_doc_dirs = list_of_rst_recursive[1:] # skip parent directory
new_md_locs = list_of_md_recursive[1:] # skip parent directory
new_md_locs
for device_repo, md_file in zip(new_doc_dirs, new_md_locs):
    for rst_filepath in glob.glob(device_repo):
        shutil.copy2(rst_filepath, '.')
        device_name = os.path.basename(rst_filepath)
        new_readme = device_name.split('.')[0] + '_' + os.path.basename(md_file)
        shutil.copy2(md_file, new_readme)

        new_devices_rst.append(device_name)

device_file = 'devices.rst'

# For avoiding false duplicates due to spacing
def normalize(line):
    return re.sub(r'\s+', '', line.strip())

with open(device_file, 'r') as f:
    all_lines = f.readlines()

depth_line_idx = next(
    (i for i, line in enumerate(all_lines) if ':maxdepth:' in line), 
    None
)

if depth_line_idx is None:
    print("Warning: ':maxdepth:' not found. Appending to full file.")
    preserved_lines = all_lines
else:
    # keep everything up to and including :maxdepth:
    preserved_lines = all_lines[:depth_line_idx + 1]

# Rebuild device section cleanly
unique_devices = sorted(set(new_devices_rst))  # sort for consistency
device_lines = [f'\t{dev}\n' for dev in unique_devices]
device_lines.insert(0, '\n')
# Write final content
with open(device_file, 'w') as f:
    f.writelines(preserved_lines + device_lines)

    