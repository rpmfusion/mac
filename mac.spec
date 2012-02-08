Name:           mac
Version:        3.99
Release:        8.u4b5%{?dist}
Summary:        Monkey's Audio Codec (MAC) utility

Group:          Applications/Multimedia
License:        Monkey's Audio Source Code License Agreement
URL:            http://supermmx.org/linux/mac/
Source0:        http://supermmx.org/resources/linux/mac/mac-%{version}-u4-b5.tar.gz
Source1:        mac-permission_to_redistribute.txt
Patch0:         mac-3.99-u4-b5-gcc44.patch
Patch1:         mac-3.99-u4-b5-analyse.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%ifarch i686 x86_64
BuildRequires:  yasm
%endif
BuildRequires:  prelink

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
%setup -q -n %{name}-%{version}-u4-b5
%patch0 -p1 -b .gcc44
%patch1 -p1 -b .an

#Copy permission to redistribute
cp -p %{SOURCE1} .

# Fix encoding issues:
for txtfile in src/Credits.txt ; do
    iconv -f iso-8859-1 -t UTF8 $txtfile -o $txtfile.utf8
    touch -r $txtfile $txtfile.utf8
    mv -f $txtfile.utf8 $txtfile
done

# Disable CXXFLAGS override
sed -i.cxxflags -e 's/ -O3 -Wall -pedantic -Wno-long-long//g' configure configure.in
touch -r configure.in.cxxflags configure.in
touch -r configure.cxxflags configure


%build
%configure --disable-static \
%ifarch i686 x86_64
  --enable-assembly=yes
%endif


# remove rpath from libtool
sed -i.rpath 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i.rpath 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool


make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'

execstack -c $RPM_BUILD_ROOT%{_libdir}/libmac.so.2.0.0

%clean
rm -rf $RPM_BUILD_ROOT


%post libs -p /sbin/ldconfig

%postun libs -p /sbin/ldconfig


%files
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog COPYING NEWS README
%{_bindir}/mac

%files libs
%defattr(-,root,root,-)
%doc mac-permission_to_redistribute.txt
%doc src/License.htm
%{_libdir}/*.so.*

%files devel
%defattr(-,root,root,-)
%doc TODO src/Readme.htm src/Credits.txt src/History.txt
%{_includedir}/mac/
%{_libdir}/*.so



%changelog
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
