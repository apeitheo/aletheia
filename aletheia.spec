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
Requires: gtts
Requires: mplayer
Requires: parallel
Requires: perl-Image-ExifTool
Requires: pulseaudio-utils
Requires: python3-eyed3
Requires: sox
Requires: sqlite
Requires: vim

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
install -D -m 644 "%%TMPDIR%%/rpmbuild/SOURCES/usr/share/aletheia/themes/Forest" "%{buildroot}/%{_datadir}/aletheia/themes/Forest"
install -D -m 644 "%%TMPDIR%%/rpmbuild/SOURCES/usr/share/aletheia/themes/Jade" "%{buildroot}/%{_datadir}/aletheia/themes/Jade"
install -D -m 644 "%%TMPDIR%%/rpmbuild/SOURCES/usr/share/aletheia/themes/Misty" "%{buildroot}/%{_datadir}/aletheia/themes/Misty"
install -D -m 644 "%%TMPDIR%%/rpmbuild/SOURCES/usr/share/aletheia/themes/Moss" "%{buildroot}/%{_datadir}/aletheia/themes/Moss"
install -D -m 644 "%%TMPDIR%%/rpmbuild/SOURCES/usr/share/aletheia/themes/Nordic" "%{buildroot}/%{_datadir}/aletheia/themes/Nordic"
install -D -m 644 "%%TMPDIR%%/rpmbuild/SOURCES/usr/share/aletheia/themes/Oasis" "%{buildroot}/%{_datadir}/aletheia/themes/Oasis"
install -D -m 644 "%%TMPDIR%%/rpmbuild/SOURCES/usr/share/aletheia/themes/Ocean" "%{buildroot}/%{_datadir}/aletheia/themes/Ocean"
install -D -m 644 "%%TMPDIR%%/rpmbuild/SOURCES/usr/share/aletheia/themes/Slate" "%{buildroot}/%{_datadir}/aletheia/themes/Slate"
install -D -m 644 "%%TMPDIR%%/rpmbuild/SOURCES/usr/share/aletheia/themes/Tropical" "%{buildroot}/%{_datadir}/aletheia/themes/Tropical"
install -D -m 644 "%%TMPDIR%%/rpmbuild/SOURCES/usr/share/aletheia/themes/Verdant" "%{buildroot}/%{_datadir}/aletheia/themes/Verdant"
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
%attr(0644, root, root) %{_datadir}/aletheia/themes/Forest
%attr(0644, root, root) %{_datadir}/aletheia/themes/Jade
%attr(0644, root, root) %{_datadir}/aletheia/themes/Misty
%attr(0644, root, root) %{_datadir}/aletheia/themes/Moss
%attr(0644, root, root) %{_datadir}/aletheia/themes/Nordic
%attr(0644, root, root) %{_datadir}/aletheia/themes/Oasis
%attr(0644, root, root) %{_datadir}/aletheia/themes/Ocean
%attr(0644, root, root) %{_datadir}/aletheia/themes/Slate
%attr(0644, root, root) %{_datadir}/aletheia/themes/Tropical
%attr(0644, root, root) %{_datadir}/aletheia/themes/Verdant
%attr(0644, root, root) %{_datadir}/aletheia/languages/en

%changelog
* %%DATE%% Brad Hermanson %%VERSION%%-%%REVISION%%
- Initial package release
