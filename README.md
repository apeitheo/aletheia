![Screenshot of Aletheia](https://github.com/apeitheo/aletheia/blob/main/screenshot.png)

## Aletheia: Media Player with Pitch and Tempo Controls

## Key Features

- **Save Pitch and Tempo Adjustments**
- **Create seamless loops with start and end points**
- **Edit mp3/flac metadata**
- **Import downloads**
- **Export playlists**

- **Support for most audio and video formats**
- **Customizable with themes**

- **On-demand voice feedback**
- **Support for translations**

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

## Try Without Installing

```bash
./aletheia
```

## Installation to /usr/local

```bash
sudo ./install
```

## Uninstallation from /usr/local

```bash
sudo ./uninstall
```

## Package Installation

- **Debian/Ubuntu Package**
```bash
sudo apt update
sudo ./create_deb
sudo apt install ./aletheia_0.9.6-11_all.deb
```

- **Fedora Package**
```bash
sudo dnf update
sudo ./create_rpm
sudo dnf install ./aletheia-0.9.6-10.fc40.noarch.rpm
```

- **openSUSE Package**

Ignore the signature verification when it prompts for it (for now).

```bash
sudo zypper refresh
sudo ./create_rpm
sudo zypper install ./aletheia-0.9.6-10.noarch.rpm
```

- **Slackware Package**
```bash
./create_archive && sudo ./aletheia.SlackBuild
sudo installpkg /tmp/aletheia-0.9.6-noarch-7_SBo.tgz
```

## Dependencies

- bash
- bc
- calc
- espeak-ng
- exiftool
- ffmpeg
- ffprobe
- mplayer
- pactl
- sox
- sqlite3
- vim

## Optional Dependencies

- eyeD3 (Edit mp3 tags)
- flac (Edit flac tags)
- gtts-cli (Natural voice feedback)
- parallel (Parallel metadata caching)

## Fedora Dependencies

- rpm-build (Needed for building package)
- ffmpeg (RPMFusion)
- mplayer (RPMFusion)

## openSUSE Dependencies

- rpm-build (Needed for building package)
- ffmpeg (Packman)
- mplayer (Packman)

## Slackware Dependencies (SlackBuilds.org)

- calc
- exiftool
- sqlite3
- eyeD3 (optional)

## Slackware gTTS Installation (Optional)

- pip install gtts

### Getting Started

The '**i**' key toggles the main menu.

To view the full list of key controls, select the **Help** option in the menu, or by press the '**?**' key at any time for function-specific controls.

## Basics

In the same style as VIM, use the '**k**' and '**j**' keys to raise or lower pitch and tempo. '**o**' and '**m**' keys increase or decrease precision in pitch adjustments by double or half. To seek backward and foreward you use '**h**' and '**l**'. Next song is '**n**' and previous song '**b**'. To pause, press '**p**' or **space**. **Escape** key or '**q**' to return to a previous screen or quit. Sometimes it's necessary to refresh the screen, which can be done at any time with '**z**'. Set the equalizer with '**a**'. Sort is '**A**' and shuffle is '**R**'. Rename is '**r**' and delete is **Ctrl-D**, with an archive option of '**D**'. Mute is '**c**'. On the left, '**1**' and '**2**' lower or raise PCM volume, and on the right '**8**' and '**9**' lower and raise master volume. '**\**' restarts the song. '**;**' opens the queue. '**g**' opens a VIM template to edit the mp3 metadata. '**s**' allows you to enter keywords to search for in the current playlist.

## Loop Creation

If you want to create a loop, wait until you've reached the beginning of the section in the song, hit the '**5**' key to indicate starting position, wait until the section is over, and hit '**7**' to indicate ending position. '**6**' opens the loop editor where you can finely adjust start and end points using '**s**' and '**g**' or '**h**' and '**l**'.

## Video Playback

Toggle with '**<**' and enable full-screen video with '**>**'.

## Voice Feedback

You can toggle voice feedback and read aloud any key control page by pressing '**d**'. The Setup screen has an option to toggle between digital and natural voice feedback if gTTS is installed.

## Additional Information

For detailed information, refer to the man page, which can be accessed by pressing the '**m**' key on the **Help** screen.

## Parallel Metadata Caching (Optional):

Add or change the following in *~/.aletheia/config*

  **PARALLEL_CACHE_ENABLED=true**
  **PARALLEL_CACHE_JOBS=4**

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
- /usr/local/share/aletheia/example.config
- /usr/local/share/aletheia/languages/en
- /usr/local/share/aletheia/themes/*
- /usr/local/share/aletheia/vimrc/*

### DEB/RPM Packages:

- /usr/bin/aletheia
- /usr/bin/aletheia\_desktop\_launcher
- /usr/share/man/man1/aletheia.1.gz
- /usr/share/applications/aletheia.desktop
- /usr/share/icons/aletheia.png
- /usr/share/aletheia/example.config
- /usr/share/aletheia/languages/en
- /usr/share/aletheia/themes/*
- /usr/share/aletheia/vimrc/*

### Slackware Package:

- /usr/bin/aletheia
- /usr/bin/aletheia\_desktop\_launcher
- /usr/man/man1/aletheia.1.gz
- /usr/share/applications/aletheia.desktop
- /usr/share/icons/aletheia.png
- /usr/share/aletheia/example.config
- /usr/share/aletheia/languages/en
- /usr/share/aletheia/themes/*
- /usr/share/aletheia/vimrc/*

## Donate (Optional)

- **Patreon:** [https://www.patreon.com/aletheia_project](https://www.patreon.com/aletheia_project)
