Summary: A CLI media player with speed controls and voice feedback
Name: aletheia
Version: %%VERSION%%
Release: %%REVISION%%%{?dist}
License: GPL3
URL: https://github.com/apeitheo/aletheia
Requires: bc
Requires: calc
Requires: espeak-ng
Requires: ffmpeg
Requires: mplayer
Requires: perl-Image-ExifTool
Requires: pulseaudio-utils
Requires: sox
Requires: sqlite
Requires: vim
Recommends: flac
Recommends: python3-eyed3
Suggests: gtts
Suggests: parallel
BuildArch: noarch

%description
A command-line media player with pitch and tempo controls using music intervals with the ability to create seamless loops, save custom adjustments, and more.

%install
install -D -m 755 "%%TMPDIR%%/rpmbuild/SOURCES/usr/bin/aletheia" "%{buildroot}/%{_bindir}/aletheia"
install -D -m 755 "%%TMPDIR%%/rpmbuild/SOURCES/usr/bin/aletheia_desktop_launcher" "%{buildroot}/%{_bindir}/aletheia_desktop_launcher"
install -D -m 644 "%%TMPDIR%%/rpmbuild/SOURCES/usr/share/man/man1/aletheia.1" "%{buildroot}/%{_mandir}/man1/aletheia.1"
install -D -m 644 "%%TMPDIR%%/rpmbuild/SOURCES/usr/share/applications/aletheia.desktop" "%{buildroot}/%{_datadir}/applications/aletheia.desktop"
install -D -m 644 "%%TMPDIR%%/rpmbuild/SOURCES/usr/share/icons/aletheia.png" "%{buildroot}/%{_datadir}/icons/aletheia.png"
install -D -m 644 "%%TMPDIR%%/rpmbuild/SOURCES/usr/share/aletheia/vimrc/vimrc" "%{buildroot}/%{_datadir}/aletheia/vimrc/vimrc"
install -D -m 644 "%%TMPDIR%%/rpmbuild/SOURCES/usr/share/aletheia/vimrc/vimrc.lock" "%{buildroot}/%{_datadir}/aletheia/vimrc/vimrc.lock"
install -D -m 644 "%%TMPDIR%%/rpmbuild/SOURCES/usr/share/aletheia/vimrc/vimrc.queue" "%{buildroot}/%{_datadir}/aletheia/vimrc/vimrc.queue"
install -D -m 644 "%%TMPDIR%%/rpmbuild/SOURCES/usr/share/aletheia/example.config" "%{buildroot}/%{_datadir}/aletheia/example.config"
install -D -m 644 "%%TMPDIR%%/rpmbuild/SOURCES/usr/share/aletheia/themes/Aurora" "%{buildroot}/%{_datadir}/aletheia/themes/Aurora"
install -D -m 644 "%%TMPDIR%%/rpmbuild/SOURCES/usr/share/aletheia/themes/Desert" "%{buildroot}/%{_datadir}/aletheia/themes/Desert"
install -D -m 644 "%%TMPDIR%%/rpmbuild/SOURCES/usr/share/aletheia/themes/Dracula" "%{buildroot}/%{_datadir}/aletheia/themes/Dracula"
install -D -m 644 "%%TMPDIR%%/rpmbuild/SOURCES/usr/share/aletheia/themes/Everforest" "%{buildroot}/%{_datadir}/aletheia/themes/Everforest"
install -D -m 644 "%%TMPDIR%%/rpmbuild/SOURCES/usr/share/aletheia/themes/Gruvbox" "%{buildroot}/%{_datadir}/aletheia/themes/Gruvbox"
install -D -m 644 "%%TMPDIR%%/rpmbuild/SOURCES/usr/share/aletheia/themes/Jade" "%{buildroot}/%{_datadir}/aletheia/themes/Jade"
install -D -m 644 "%%TMPDIR%%/rpmbuild/SOURCES/usr/share/aletheia/themes/Mist" "%{buildroot}/%{_datadir}/aletheia/themes/Mist"
install -D -m 644 "%%TMPDIR%%/rpmbuild/SOURCES/usr/share/aletheia/themes/Nord" "%{buildroot}/%{_datadir}/aletheia/themes/Nord"
install -D -m 644 "%%TMPDIR%%/rpmbuild/SOURCES/usr/share/aletheia/themes/Oasis" "%{buildroot}/%{_datadir}/aletheia/themes/Oasis"
install -D -m 644 "%%TMPDIR%%/rpmbuild/SOURCES/usr/share/aletheia/themes/Slate" "%{buildroot}/%{_datadir}/aletheia/themes/Slate"
install -D -m 644 "%%TMPDIR%%/rpmbuild/SOURCES/usr/share/aletheia/themes/Solarized" "%{buildroot}/%{_datadir}/aletheia/themes/Solarized"
install -D -m 644 "%%TMPDIR%%/rpmbuild/SOURCES/usr/share/aletheia/themes/Tropics" "%{buildroot}/%{_datadir}/aletheia/themes/Tropics"
install -D -m 644 "%%TMPDIR%%/rpmbuild/SOURCES/usr/share/aletheia/themes/Verdant" "%{buildroot}/%{_datadir}/aletheia/themes/Verdant"
install -D -m 644 "%%TMPDIR%%/rpmbuild/SOURCES/usr/share/aletheia/themes/Zenburn" "%{buildroot}/%{_datadir}/aletheia/themes/Zenburn"
install -D -m 644 "%%TMPDIR%%/rpmbuild/SOURCES/usr/share/aletheia/languages/en" "%{buildroot}/%{_datadir}/aletheia/languages/en"

%files
%attr(0755, root, root) %{_bindir}/aletheia
%attr(0755, root, root) %{_bindir}/aletheia_desktop_launcher
%attr(0644, root, root) %{_mandir}/man1/aletheia.1.gz
%attr(0644, root, root) %{_datadir}/applications/aletheia.desktop
%attr(0644, root, root) %{_datadir}/icons/aletheia.png
%attr(0644, root, root) %{_datadir}/aletheia/vimrc/vimrc
%attr(0644, root, root) %{_datadir}/aletheia/vimrc/vimrc.lock
%attr(0644, root, root) %{_datadir}/aletheia/vimrc/vimrc.queue
%attr(0644, root, root) %{_datadir}/aletheia/example.config
%attr(0644, root, root) %{_datadir}/aletheia/themes/Aurora
%attr(0644, root, root) %{_datadir}/aletheia/themes/Desert
%attr(0644, root, root) %{_datadir}/aletheia/themes/Dracula
%attr(0644, root, root) %{_datadir}/aletheia/themes/Everforest
%attr(0644, root, root) %{_datadir}/aletheia/themes/Gruvbox
%attr(0644, root, root) %{_datadir}/aletheia/themes/Jade
%attr(0644, root, root) %{_datadir}/aletheia/themes/Mist
%attr(0644, root, root) %{_datadir}/aletheia/themes/Nord
%attr(0644, root, root) %{_datadir}/aletheia/themes/Oasis
%attr(0644, root, root) %{_datadir}/aletheia/themes/Slate
%attr(0644, root, root) %{_datadir}/aletheia/themes/Solarized
%attr(0644, root, root) %{_datadir}/aletheia/themes/Tropics
%attr(0644, root, root) %{_datadir}/aletheia/themes/Verdant
%attr(0644, root, root) %{_datadir}/aletheia/themes/Zenburn
%attr(0644, root, root) %{_datadir}/aletheia/languages/en

%changelog
* Sat Jun 22 2024 Brad Hermanson 1.0-2
- Fixed shellcheck warning.

* Thu Jun 20 2024 Brad Hermanson 1.0-1
- Added 'flac' dependency and updated list of themes.
