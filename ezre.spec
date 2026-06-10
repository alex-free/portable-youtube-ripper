%global source_date_epoch_from_changelog 0

Name: pytr
Version: v1.0
Summary: Easy YouTube ripping for Mac OS and Linux.
Release: 1
License: BSD-3-Clause
URL: https://github.com/alex-free/portable-youtube-ripper
Packager: Alex Free
Requires: yt-dlp, ffmpeg

%description
Easy YouTube ripping for Mac OS and Linux.

%install
mkdir -p %{buildroot}/usr/bin
cp %{_sourcedir}/pytr %{buildroot}/usr/bin/

%files
/usr/bin/pytr
