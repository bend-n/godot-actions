# godot-actions

[![license](https://img.shields.io/badge/License-MIT-blue?style=for-the-badge)](https://github.com/bend-n/godot-actions/blob/main/LICENSE "License")
[![version](https://img.shields.io/badge/3.5>3.x-blue?logo=godot-engine&logoColor=white&label=godot&style=for-the-badge)](https://godotengine.org)
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
> This is a copy of [godot-template/.github/workflows/export.yml](https://github.com/bend-n/godot-template/blob/99d8c0c9b376456b6ded812b47b7a8d3b64e15d9/.github/workflows/export.yml)

```yaml
name: "export"
on:
  workflow_dispatch:
  push:
    paths:
      - "**.gd"
      - "**.tscn"
      - "**.import"
      - "**.tres"
      - "**.ttf"
      - ".github/workflows/export.yml"
      - "export_presets.cfg"
    branches:
      - main

env:
  GODOT_VERSION: 3.5
  NAME: ${{ github.event.repository.name }}

jobs:
  export:
    runs-on: ubuntu-latest
    container:
      image: ghcr.io/bend-n/godot-2d:3.5
    name: ${{ matrix.name }}
    strategy:
      matrix:
        include:
          - name: Windows export
            platform: windows

          - name: Linux export
            platform: linux

          - name: Mac export
            platform: mac

          - name: Web export
            platform: web

          - name: Android export
            platform: android

    steps:
      - name: Build (Windows)
        if: matrix.platform == 'windows'
        uses: bend-n/godot-actions/.github/actions/export-windows@main

      - name: Build (Linux)
        if: matrix.platform == 'linux'
        uses: bend-n/godot-actions/.github/actions/export-linux@main

      - name: Build (Mac)
        if: matrix.platform == 'mac'
        uses: bend-n/godot-actions/.github/actions/export-mac@main

      - name: Build (Web)
        if: matrix.platform == 'web'
        uses: bend-n/godot-actions/.github/actions/export-web@main

      - name: Build (Android)
        if: matrix.platform == 'android'
        uses: bend-n/godot-actions/.github/actions/export-android@main
        with:
          android-keystore-base64: ${{ secrets.ANDROID_KEYSTORE_BASE64 }}
          android-password: ${{ secrets.ANDROID_KEYSTORE_PASSWORD }}

  push-itch:
    needs: [export]
    name: Push to itch.io
    runs-on: ubuntu-20.04
    steps:
      - name: Check for api key
        id: secret
        run: echo '::set-output name=secret::${{ secrets.BUTLER_CREDENTIALS }}'

      - name: Push
        if: steps.secret.outputs.secret
        uses: bend-n/godot-actions/.github/actions/itch-push@main
        with:
          api-key: ${{ secrets.BUTLER_CREDENTIALS }}
```

</details>

### Users

[bendn/chess](https://github.com/bend-n/chess)
[bendn/tetris](https://github.com/bend-n/tetris)
[bendn/spaceshooty](https://github.com/bend-n/tetris)
[bendn/remap](https://github.com/bend-n/remap)
[bendn/latex-bot](https://github.com/bend-n/latex-bot)
[bendn/swipe-detector](https://github.com/bend-n/swipe-detector)
[bendn/code-image](https://github.com/bend-n/code-image)
[bendn/gd-eval](https://github.com/bend-n/gd-eval)
[bendn/sokoban](https://github.com/bend-n/sokoban)
[bendn/godot-template](https://github.com/bend-n/godot-template)
