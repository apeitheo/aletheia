# Aletheia: CLI Media Player with Pitch and Tempo Control

Aletheia is a command-line media player for GNU/Linux focused on precise pitch and tempo control, but offers much more as well:

## Key Features

- **Real-Time Pitch and Tempo Adjustment:** Change tonality with customizable intervals.
- **Seamless Loop Creation:** Set custom start and end points and export loops.
- **Versatile Media Support:** Supports all common media formats due to its robust **mplayer** backend.
- **Voice Feedback:** Optional digital or natural voice feedback.
- **Playlist Management:** Manage and export playlists with ease.
- **Advanced Scaling Features:** Smoothly transition between different intervals.

## User-Friendly Controls

- **Simple Navigation:** Uses intuitive key controls.
- **Customizable Interface:** Comes with a selection of themes and support for adding your own.
- **Metadata Support:** Manage media tags on the go.

## Get Started

### Clone Aletheia

Open your terminal and run the following command to clone the Aletheia repository from GitHub:

```bash
git clone https://github.com/apeitheo/aletheia.git
```

### Navigate to the Directory

```bash
cd aletheia
```

## Testing

Before installation, you can test Aletheia by running the following command. It will automatically check dependencies for you.

```bash
./aletheia
```

## Installation

Run the installation script to set up Aletheia on your system.

```bash
./install
```

## Uninstallation

If you ever need to uninstall Aletheia, you can run the uninstallation script:

```bash
./uninstall
```

## Dependencies

- bash
- bc
- calc
- espeak-ng
- exiftool
- eyeD3
- ffmpeg
- ffprobe
- mplayer
- pactl
- sox
- sqlite3
- vim

## Optional Dependencies

- gtts-cli
- play
- parallel

Slackware users will need exiftool, eyeD3, sqlite3, and eyeDB's dependencies from SlackBuilds.org

## Additional Information

To learn the basics of Aletheia, read the manpage and check out the controls by clicking the "**Help**" option in the menu, or by pressing the '**?**' key at any time. Use the '**j**' and '**k**' keys to page down or up, and '**q**' to go back or quit. If you need voice feedback, hit '**d**' followed by '**#**' to save your choice.

If you prefer a natural-sounding voice feedback, gtts-cli is part of the gTTS project (gTTS on PyPI) that downloads voice clips based on the Google Assistant voice. It can be enabled via setting **USE_GTTS** and **VOICE_ENABLED** to **true** in *~/.aletheia/config* and ensuring the packages for your distribution containing *gtts-cli* and *play* are installed.

If you have a large media collection, parallel processing of metadata is available via setting **PARALLEL_CACHE_ENABLED** to **true**, and optionally setting the number of tags to process at one time with **PARALLEL_CACHE_JOBS**. Requires *parallel* to be installed. May cause performance issues on slower machines.

## Package Build Scripts

The following are package build scripts for Debian, Fedora, and Slackware-based distributions:

- **Debian Package:**
```bash
./create_deb
```

- **Fedora Package:**
```bash
./create_rpm
```

- **Slackware Package:**
```bash
./create_archive && ./aletheia.SlackBuild
```

### Custom Location

To install somewhere other than /usr/local when using ./install:

```bash
./install --destdir /path/to/directory/
```

Or use the **DESTDIR** environment variable:

```bash
DESTDIR=/path/to/directory/ ./install
```

## List of Installed Files

### Using ./install:

- /usr/local/bin/aletheia
- /usr/local/bin/aletheia\_desktop\_launcher
- /usr/local/share/man/man1/aletheia.1
- /usr/local/share/applications/aletheia.desktop
- /usr/local/share/icons/aletheia.png
- /usr/local/share/aletheia/themes/*
- /usr/local/share/aletheia/vimrc/*

### DEB/RPM Packages:

- /usr/bin/aletheia
- /usr/bin/aletheia\_desktop\_launcher
- /usr/share/man/man1/aletheia.1.gz
- /usr/share/applications/aletheia.desktop
- /usr/share/icons/aletheia.png
- /usr/share/aletheia/themes/*
- /usr/share/aletheia/vimrc/*

### Slackware Package:

- /usr/bin/aletheia
- /usr/bin/aletheia\_desktop\_launcher
- /usr/man/man1/aletheia.1.gz
- /usr/share/applications/aletheia.desktop
- /usr/share/icons/aletheia.png
- /usr/share/aletheia/themes/*
- /usr/share/aletheia/vimrc/*

## Support (Optional)

- **Patreon:** [https://www.patreon.com/aletheia_project](https://www.patreon.com/aletheia_project)
