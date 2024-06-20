# Getting copies of the tutorials

We have clean copies of the tutorials in the [pace-2024-tutorials](https://github.com/PACEHackWeek/pace-2024-tutorials) repository.

## Day 1

Log into the JupyterHub and open a terminal and type:

```shell
  cd ~
  git clone "https://github.com/PACEHackWeek/pace-2024-tutorials"
```

## Day 2 or anytime the tutorials are updated

The following commands will get changes on GitHub. If you have made local changes, then you might get merge conflicts.
  ```
  cd ~/pace-2024-tutorials
  git pull
  ```

  If you get merge conflicts and want to wipe out your local changes, then use
  ```
  cd ~/pace-2024-tutorials
  git fetch --all
  git reset --force origin/main
  ```

## Avoiding merge conflicts

We suggest that you, right-click on the tutorials and make a copy and work there. That way if we need to update a tutorial, you will not get merge conflicts.
