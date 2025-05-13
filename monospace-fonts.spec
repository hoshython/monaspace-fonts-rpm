Name:           monaspace-fonts
Version:        1.0
Release:        1%{?dist}
Summary:        An innovative superfamily of fonts for code

License:        OFL
URL:            https://github.com/hoshython/monaspace
Source0:        https://github.com/hoshython/monaspace/archive/refs/heads/main.zip
Source1:        https://raw.githubusercontent.com/hoshython/monaspace/main/main.zip.sha256

BuildArch:      noarch
BuildRequires:  fontpackages-devel, curl, coreutils, unzip
Requires:       fontpackages-filesystem

%description
Monaspace is a monospaced superfamily designed by GitHub Next for code and developer experience.
This package provides the base OpenType fonts (.otf) from the Monaspace family.

# --- Frozen TTF Fonts ---
%package -n ttf-monaspace
Summary:        Monaspace frozen TrueType fonts

%description -n ttf-monaspace
This subpackage includes the frozen (static) TrueType fonts of the Monaspace family.

# --- Variable TTF Fonts ---
%package -n ttf-var-monaspace
Summary:        Monaspace variable TrueType fonts

%description -n ttf-var-monaspace
This subpackage includes the variable TrueType fonts of the Monaspace family.

%prep
%autosetup -n monaspace-main

# Download the SHA256 hash file (Source1)
curl -O %{SOURCE1}

# Verify the hash of the downloaded ZIP file
sha256sum -c main.zip.sha256 || exit 1

# Unzip the file
unzip main.zip -d %{_builddir}

%build
# Nothing to build

%install
install -m 0755 -d %{buildroot}%{_fontdir}/monaspace/otf
install -m 0755 -d %{buildroot}%{_fontdir}/monaspace/frozen
install -m 0755 -d %{buildroot}%{_fontdir}/monaspace/variable

# Install base OTF fonts
install -m 0644 fonts/otf/*.otf %{buildroot}%{_fontdir}/monaspace/otf/

# Install frozen TTF fonts
install -m 0644 fonts/frozen/*.ttf %{buildroot}%{_fontdir}/monaspace/frozen/

# Install variable TTF fonts
install -m 0644 fonts/variable/*.ttf %{buildroot}%{_fontdir}/monaspace/variable/


%files
%license LICENSE
%doc README.md
%{_fontdir}/monaspace/otf/*.otf

%files -n ttf-monaspace
%{_fontdir}/monaspace/frozen/*.ttf

%files -n ttf-var-monaspace
%{_fontdir}/monaspace/variable/*.ttf

%changelog
* Tue May 13 2025 Hoshyar <baxooshi@outlook.com> - 1.0-1
- Initial RPM release with ttf-monaspace, ttf-var-monaspace, and monaspace-fonts
