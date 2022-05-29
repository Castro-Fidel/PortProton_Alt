Summary:	Installer for PortProton
Name:		portproton
Version:	1.0
Release:	5
License:	MIT
Group:		Games/Other
Url:		https://github.com/Castro-Fidel/PortWINE
Source0:	https://github.com/Castro-Fidel/PortWINE/raw/master/portwine_install_script/PortProton_%{version}
Source1:	https://github.com/Castro-Fidel/PortWINE/raw/master/data_from_portwine/img/gui/port_proton.png
Requires:	bc
Requires:	bubblewrap
Requires:	cabextract
Requires:	coreutils
Requires:	curl
Requires:	file
Requires:	icoutils
Requires:	lib64drm2
Requires:	lib64freetype2
Requires:	lib64opencl1
Requires:	lib64txc-dxtn
Requires:	openssl
Requires:	sysvinit-tools
Requires:	tar
Requires:	vkd3d(x86-64)
Requires:	vulkan(x86-64)
Requires:	wget
Requires:	xdg-utils
Requires:	xz
Requires:	zenity
Requires:	zstd
Recommends:	lib64d3dadapter9_1
Recommends:	libcurl4(x86-32)
Recommends:	libd3dadapter9_1(x86-32)
Recommends:	libdrm2(x86-32)
Recommends:	libfreetype2(x86-32)
Recommends:	libGL1(x86-32)
Recommends:	libnss3(x86-32)
Recommends:	libopencl1(x86-32)
Recommends:	libtxc-dxtn(x86-32)
Recommends:	libvulkan1(x86-32)
Recommends:	mesa(x86-32)
Recommends:	vkd3d(x86-32)
Recommends:	vulkan(x86-32)
ExclusiveArch:	x86_64

%description
Installer PortProton for Windows games.

%files
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/port_proton.png

#----------------------------------------------------------------------------

%prep

%build

%install
mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/%{name}.desktop << EOF
[Desktop Entry]
Type=Application
Name=PortProton
Name[ru]=PortProton
Comment=Installer PortProton for Windows games
Comment[ru]=Установщик PortProton для Windows игр
Exec=%{name} %F
Icon=port_proton
StartupNotify=false
Terminal=false
Categories=Game;
MimeType=application/x-wine-extension-msp;application/x-msi;application/x-ms-dos-executable;
EOF

mkdir -p %{buildroot}%{_bindir}/
install -m755 %{SOURCE0} %{buildroot}%{_bindir}/%{name}

mkdir -p %{buildroot}%{_datadir}/pixmaps
install -m644 %{SOURCE1} %{buildroot}%{_datadir}/pixmaps/
