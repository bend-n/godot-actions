# godot-actions

[![license](https://img.shields.io/badge/License-MIT-blue?style=for-the-badge)](https://github.com/bend-n/godot-actions/blob/main/LICENSE "License")
[![version](https://img.shields.io/badge/>3.5-blue?logo=godot-engine&logoColor=white&label=godot&style=for-the-badge)](https://godotengine.org)
<a href='https://ko-fi.com/bendn' title='Buy me a coffee' target='_blank'><img height='28' src='https://storage.ko-fi.com/cdn/brandasset/kofi_button_red.png' alt='Buy me a coffee'> </a>

Github Actions composite action repository.

## How to use

<details open>
<summary>Snippet</summary>

```yaml
build-windows:
  runs-on: ubuntu-latest
  container:
    image: ghcr.io/bend-n/godot-2d:3.5
  name: Build windows
  steps:
    - name: Build
      uses: bend-n/godot-actions/.github/actions/export-windows@main
      env:
        GODOT_VERSION: 3.5
        NAME: ${{ github.event.repository.name }}
```

</details>

<details>
<summary>Full example</summary>

> **Note**
> This is a copy of [godot-template/.github/workflows/export.yml](https://github.com/bend-n/godot-template/blob/dd6e014d5329b4aaf3ad32f110c5ea406777a6fc/.github/workflows/export.yml)

```yaml
name: "export" # name of the workflow
on: # when it is triggered
  workflow_dispatch: # manually
  push: # on push
    paths: # with modifications to these files
      - "**.gd"
      - "**.tscn"
      - "**.import"
      - "**.tres"
      - "**.ttf"
      - ".github/workflows/export.yml"
      - "export_presets.cfg"
    branches: # on this branch
      - main

jobs: # the things to do
  export: # a thing to do
    uses: bend-n/godot-actions/.github/workflows/callable-export.yml@main
    with: # variables
      export-name: ${{ github.event.repository.name }} # the name of the zipfile
      godot-version: 3.5 # the godot version
      image: ghcr.io/bend-n/godot-2d:3.5 # the container to use
      platforms: "windows linux web android mac" # space seperated list of platforms to build
    secrets: # secrets
      android-keystore-base64: ${{ secrets.ANDROID_KEYSTORE_BASE64 }} # not required
      android-keystore-password: ${{ secrets.ANDROID_KEYSTORE_PASSWORD }} # not required
      butler-api-key: ${{ secrets.BUTLER_CREDENTIALS }} # required for itch.io
```

</details>

### Configuration

> **Note** If script is not compiled, it must contain a [shebang](<https://en.wikipedia.org/wiki/Shebang_(Unix)>)

Create a file `./.github/post_export` that will be run after installation. The executable will be run with a argument, containing the platform. (eg: `./.github/post_export linux`)

Bash example:

```bash
#!/bin/bash
[[ $1 == "web" ]] && wget -nv "example.org" -O build/web/example.html
```