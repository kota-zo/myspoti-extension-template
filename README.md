# Myspoti extension template

A starting point for your own [Myspoti](https://github.com/kota-zo/myspoti) extension. It is a
tiny but real one, **Heard Lately**: it remembers the last songs you played and shows them as a
section at the end of Home. No network, three actions, each with its reason.

Nobody has to approve your extension. You publish it in your own GitHub repository, tag it, and
Myspoti's store finds it by its topic. Myspoti does not host, review or endorse extensions: you are
responsible for yours. Read the [policy](https://github.com/kota-zo/myspoti-extensions/blob/main/POLICY.md)
first.

## Publish in 5 minutes

1. **Use this template**: the green button on this page, then create your own **public**
   repository (name it as you like, for instance `myspoti-lyrics-example`).
2. **Rename the extension** in `manifest.json`. The `id` is yours for good (it never changes
   between versions): lower case, reverse-domain, letters, digits and `_` only, for instance
   `io.github.your_github_name.heardlately`. Then set `name`, `author`, `description` and
   `homepage` (your repository, so people can reach you). Replace your name in `LICENSE`.
3. **Edit `main.js`** and the `actions` in `manifest.json`. An extension can only do what its
   manifest lists, and each action needs a `why` of 80 characters or less, in plain words: it is
   shown to the person installing. Ask for the least you need. The full list of actions, hooks and
   blocks is in the
   [API documentation](https://github.com/kota-zo/myspoti/blob/main/docs/extensions/API.md).
4. **Check it on your computer** with the desktop runner `myspoti-ext` (see "Testing on a
   computer" in the API documentation):

   ```
   myspoti-ext check .
   myspoti-ext run . home --title "Song" --artist "Artist"
   myspoti-ext run . track --title "Song" --artist "Artist" --id 4uLU6hMCjMI75M1A2tKUQC
   ```

   `check` must print no problem.
5. **Add the topic `myspoti-extension`** to your repository (the gear next to "About", then
   "Topics"). The store searches GitHub for that topic and lists your extension within 6 hours.
6. **Release**: raise `version` and `versionCode` in `manifest.json` (`versionCode` is the integer
   the app compares, it only goes up), commit, then tag:

   ```
   git tag v1.0.0
   git push origin v1.0.0
   ```

   The workflow in `.github/workflows/release.yml` builds `extension.zip` (the exact package
   Myspoti installs: `manifest.json`, your script, the icon, `LICENSE` and `README.md` at the root,
   nothing else) and attaches it to a GitHub release. The tag must match `version`. Phones
   update by themselves within a day when the new version asks nothing new; if you add an action,
   a host or change a `why`, users are asked once. To build the package by hand:
   `python3 scripts/pack.py`.

Keep `id` and the repository stable: a changed one is shown to users as a different source.

## What is in this repository

| File | Role |
|---|---|
| `manifest.json` | Who you are and what you ask (id, version, `actions` with their `why`, category, tags). |
| `main.js` | The script, run in Myspoti's sandbox. |
| `icon.png` | Optional: a square PNG, 256 px or less, next to `manifest.json`. |
| `LICENSE`, `README.md` | Kept in the package. Other files (sources, screenshots, workflows, `scripts/`) stay in the repository and are not installed. |
| `scripts/pack.py` | Builds `extension.zip` with fixed file order and dates, so a rebuild gives the same bytes. |
| `.github/workflows/release.yml` | On a `vX.Y.Z` tag, builds the package and publishes the release. |

## Ratings (optional)

People rate an extension with a thumbs up or down on one issue in your repository. To enable it,
**from your own account** (an issue opened by anyone else does not count):

1. Create the label `myspoti-ratings` (Issues, Labels, New label).
2. Open an issue titled `Ratings`, with that label, and say it is where people rate the extension.
   Keep it open. Do not react to it yourself.

Or with the GitHub CLI: `gh label create myspoti-ratings && gh issue create --title Ratings --label myspoti-ratings --body "Rate this extension with a thumbs up or down on this issue."`

The store shows a score once there are votes. It is a Bayesian average, so a few votes do not
outrank many. The release's `extension.zip` download count is shown on the store page.

## Reporting a problem in someone's extension

Open a report on the [official repository](https://github.com/kota-zo/myspoti-extensions/issues/new/choose)
or write to myspoti.app@gmail.com. Procedure: see its `REPORTING.md`.

## License

This template is MIT: replace the name in `LICENSE`, or change the license for your extension.
