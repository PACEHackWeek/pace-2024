# PACE Hackweek JupyterBook

This the JupyterBook content for the PACE Hackweek 2024.

![image](https://github.com/noaa-nwfsc/Hackweek-2024-book/assets/2545978/8f4eda29-eec2-4263-bc1f-600ef5567996)

## Developers

### New or updated tutorials

1. Fork or clone the pace-2024, pace-2024-tutorials, oceandata-notebooks repos.
1. When tutorials are ready to be moved into the Jupyter Book, source the function in `copy_tutorials.py` and then use it to create the unrendered (tutorial repo) and rendered notebooks (book).
2. This will create a branch for you to work on.
3. Switch to that branch and edit `book/_toc.yml` and `book/tutorials/index.md`. Commit those changes to the branch.
4. If there are any images that were created and that you need in the tutorial, then you will need to commit those and push.
5. Create a PR and **label the PR `preview`**. A link to click to create the PR will be shown.
6. After you create the PR (with label `preview`, a link to a netlify preview will appear. Check to ensure that it looks good.
7. Troubleshooting
    * Do you need to change the original tutorial and it is in the gfdl org? Go there and make changes. Then rerun the function in `copy_tutorials.py`.
    * Do you want to add files specific to the hackweek? You can add those, to the pace-2024 repo.
9. Once the PR looks good in netlify, it can be merged.

OR

1. Clone the oceandata-noteboooks in adjacent directory, use quay.io/pacehackweek/pace-2024:latest to build as in README
2. Copy them to the tutorials folder
   ```
   rsync -a ../oceandata-notebooks/src/_build/jupyter_execute/notebooks/hackweek/ book/presentations/hackweek/
   ```

### Updating other parts of the Jupyter Book

2. Make the necessary changes.
3. Create a PR and label the PR `preview`.
4. A link to a netlify preview will appear. Check to ensure that it looks good and make any necessary changes.
5. Once the PR is reviewed by another team member, it can be merged.

### Template curtesy of (by permission) eScience University of Washington

This is a clone of the eScience template repository designed to streamline creating two linked websites for a [UW eScience Hackweek](https://uwhackweek.github.io/hackweeks-as-a-service/intro.html).

Please see the [eScience repository template](https://github.com/uwhackweek/jupyterbook-template) for usage, contributors and citation information.
