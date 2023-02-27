Name:           mac
Version:        9.04
Release:        1%{?dist}
Summary:        Monkey's Audio Codec (MAC) utility

Group:          Applications/Multimedia
License:        Monkey's Audio Source Code License Agreement
URL:            https://www.monkeysaudio.com/index.html
# use debian multimedia source
Source0:        https://monkeysaudio.com/files/MAC_904_SDK.zip
Source1:        mac-permission_to_redistribute.txt
Source2:        https://www.monkeysaudio.com/license.html

BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  python3-html2text

Requires:  %{name}-libs = %{version}-%{release}


%description
Monkey’s Audio is a fast and easy way to compress digital music. Unlike
traditional methods such as mp3, ogg, or lqt that permanently discard
quality to save space, Monkey’s Audio only makes perfect, bit-for-bit
copies of your music. That means it always sounds perfect  – exactly the
same as the original. Even though the sound is perfect, it still saves a
lot of space.

Permission to redistribute is granted by the AUTHOR to rpmfusion.org only.
See mac-permission_to_redistribute.txt

%package        libs
Summary:        Library for Monkey's Audio Codec
Group:          System Environment/Libraries
# Introduced in F-9 to solve multilib transition
Obsoletes:      %{name} < 3.99-3

%description    libs
The %{name}-libs package contains library for Monkey's Audio Codec.

%package        devel
Summary:        Development files for %{name}
Group:          Development/Libraries
Requires:       %{name}-libs = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%autosetup -c -n MAC_904_SDK

#Copy permission to redistribute
cp -p %{SOURCE1} .
cp -p %{SOURCE2} .


%build
%make_build -C Source/Projects/NonWindows


%install
%make_install prefix=%{_prefix} libdir=%{_libdir} -C Source/Projects/NonWindows

# generate license
html2text --ignore-links "license.html" | sed -n '/^## License$/,$p' >> LICENSE.md

%files
%{_bindir}/mac

%files libs
%doc mac-permission_to_redistribute.txt
%doc LICENSE.md
%{_libdir}/*.so.*

%files devel
%{_includedir}/MAC/
%{_libdir}/*.so



%changelog
* Mon Feb 27 2023 Leigh Scott <leigh123linux@gmail.com> - 9.04-1
- Update to 9.04

* Mon Aug 08 2022 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 4.11-14.u4b5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild and ffmpeg
  5.1

* Thu Feb 10 2022 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 4.11-13.u4b5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Aug 04 2021 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 4.11-12.u4b5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Feb 04 2021 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 4.11-11.u4b5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Aug 19 2020 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 4.11-10.u4b5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Feb 05 2020 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 4.11-9.u4b5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Aug 10 2019 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 4.11-8.u4b5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Mar 05 2019 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 4.11-7.u4b5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Aug 19 2018 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 4.11-6.u4b5
- Rebuilt for Fedora 29 Mass Rebuild binutils issue

* Fri Jul 27 2018 RPM Fusion Release Engineering <sergio@serjux.com> - 4.11-5.u4b5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Mar 02 2018 RPM Fusion Release Engineering <leigh123linux@googlemail.com> - 4.11-4.u4b5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 31 2017 RPM Fusion Release Engineering <kwizart@rpmfusion.org> - 4.11-3.u4b5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Mar 26 2017 RPM Fusion Release Engineering <kwizart@rpmfusion.org> - 4.11-2.u4b5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jul 14 2016 Leigh Scott <leigh123linux@googlemail.com> - 4.11-1.u4b5
- fix bz4123
- use monkeys-audio source from Debian multimedia

* Fri Jul 01 2016 Leigh Scott <leigh123linux@googlemail.com> - 3.99-13.u4b5
- patch for gcc-6

* Thu Jun 30 2016 Nicolas Chauvet <kwizart@gmail.com> - 3.99-12.u4b5
- Spec clean-up
- Use execstrack instead of prelink on fedora 23 and later
- Fix build with newer gcc

* Sun Aug 31 2014 Sérgio Basto <sergio@serjux.com> - 3.99-11.u4b5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Tue Mar 12 2013 Nicolas Chauvet <kwizart@gmail.com> - 3.99-10.u4b5
- https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Mar 08 2012 Nicolas Chauvet <kwizart@gmail.com> - 3.99-9.u4b5
- Rebuilt for c++ ABI breakage

* Thu Feb 09 2012 Nicolas Chauvet <kwizart@gmail.com> - 3.99-8.u4b5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sun Mar 29 2009 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info> - 3.99-7.u4b5
- rebuild for new F11 features

* Fri Mar 13 2009 kwizart < kwizart at gmail.com > - 3.99-6.u4b5
- Add permission to redistribute for RPM Fusion. (bundled with -libs)
- Fix for gcc44

* Mon Feb  2 2009 kwizart < kwizart at gmail.com > - 3.99-4.u4b5
- Fix the main package category
- Fix the execstack on libmac.so.2
- Move some docs from main to -devel

* Fri Dec 12 2008 kwizart < kwizart at gmail.com > - 3.99-3.u4b5
- Multilib compliance
- Disable rpath (libtool patch)
- Fix doc encoding
- Enable asm optimization with yasm when possible
- Disable CXXFLAGS override

* Mon Jul 10 2006 Matthias Saou <http://freshrpms.net/> 3.99-2.u4b5
- Update to 3.99-u4-b5.
- Remove no longer needed 64bit patch.

* Fri Mar 17 2006 Matthias Saou <http://freshrpms.net/> 3.99-2.u4b4
- Release bump to drop the disttag number in FC5 build.

* Thu Jan 19 2006 Matthias Saou <http://freshrpms.net/> 3.99-1.u4b4
- Update to 3.99-u4-b4.
- Port over 64bit patch from the gstreamer-monkeysaudio package.

* Thu May 26 2005 Matthias Saou <http://freshrpms.net/> 3.99-1.u4b3
- Initial RPM release.
