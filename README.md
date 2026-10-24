# caffinnovators

This repository is maintained at [morevijay08/caffinnovators](https://github.com/morevijay08/caffinnovators).

## Working on the `sapnamore` branch

Clone this repository and switch to the contributor branch:

```bash
git clone https://github.com/morevijay08/caffinnovators.git
cd caffinnovators
git switch sapnamore
code .
```

After editing project files in VS Code, commit and push changes **only** to `sapnamore`:

```bash
git status
git add .
git commit -m "Describe your changes"
git push -u origin sapnamore
```

Before committing, confirm the current branch:

```bash
git branch --show-current
```

It should print `sapnamore`. Do not push to `main` as part of this workflow.

## Project status

The starting `main` branch contains the repository license. Application source code and setup instructions can be added as development proceeds.
