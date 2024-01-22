# GIT Commit Message Checker in Pyhton

To ensure that all your GIT commit message follow a certain pattern, you can use commit-msg hooks.
This repo contains a basic implementation of a commit-msg hook and a minimal set-up to test them.

## Installation

Softlink the `commit-msg.py` to the `.git/hooks/commit-msg` directory of your git-project.

```bash
ln --symbolic --force ./commit-msg.py your/path/your-project/.git/hooks/commit-msg
```

Possiblity, you have to make the script executable by running `chmod u+x commit-msg.py`.

## Testing Checker

To check your changes to `commit-msg.py`, you do not need to actually make a commit.
In the `./tests` directery, you can add tests that are either supposed to fail (file name starting with `file-`) or pass (file name starting with `pass-`).
Then, simply run `./run-tests.sh`

## License

Just use it. Whatevs.