# Set up tutorials

# Once tutorials are finalized, they can be copied to the tutorials repo (that participants will clone) and copied to the JupyterBook.  To use this notebook,

# 1. Run the first code chunk
# 2. Add or run subsequent code chunks to create the files.
# 3. CLOSE copy_tutorials.ipynb! or else jupyter notebooks is going to create merge conflicts.
# 4. Click on the created branch and then open /book/_toc.yaml . Add your file to the toc.
# 5. Edit book/tutorials/index.md to add your tutorial there.
# 6. Go to GitHub and manually create a PR and label it 'preview'
# 7. Need changes? Get on the branch and make changes there.
# 8. Done? Make sure to a) merge the PR or delete it and b) delete the branch used for the PR.

# https://jupytext.readthedocs.io/en/latest/using-cli.html#advanced-usage-error-tolerance
import os
import time
def get_tutorial(fil, dir, pushbook=False, pushtut=True):
  src_dir="~/oceandata-notebooks/src/"
  tut_dir="~/pace-2024-tutorials/"
  book_repo="~/pace-2024/"
  book_dir="book/tutorials/"
  os.system("mkdir -p "+tut_dir+dir)
  os.system("mkdir -p "+book_dir+dir)
  tfil=tut_dir+dir+"/"+fil+".ipynb"
  ifil=src_dir+dir+"/"+fil+".py"
  bfil=book_repo+book_dir+dir+"/"+fil+".ipynb"
  # create ipynb without executed cells
  os.system("jupytext --to ipynb -o "+tfil+" "+ifil)
  if pushtut:
    os.system("cd "+tut_dir+" && "+"git add "+dir+"/"+fil+".ipynb && git commit -m 'update tutorial' && git push")
  # create the book tutorial with rendering
  if pushbook:
    os.system("cd "+book_dir)
    newbranch="tutorial-patch-"+str(round(time.time()))
    curbranch=os.popen("git rev-parse --abbrev-ref HEAD").read().strip()
    os.system("git checkout -b "+newbranch)
  os.system("cp --force "+tfil+" "+bfil)
  # create ipynb without executed cells
  os.system("jupyter nbconvert --to ipynb --inplace --execute --allow-errors "+bfil)
  if pushbook:
    bfil=book_dir+dir+"/"+fil+".ipynb"
    os.system("git add "+bfil+" && git commit -m 'add tutorial' && git push -u origin "+newbranch+" && git checkout "+curbranch)

# Create a branch, switch to that, run get_tutorial(), then edit _toc.yml and index.md, push, and create PR with label preview

# oci
get_tutorial("oci_data_access", "oci")
get_tutorial("oci_file_structure", "oci")

#harp
get_tutorial("harp2_basic_visualizations", "harp2")