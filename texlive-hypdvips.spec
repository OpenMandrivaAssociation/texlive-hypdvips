# revision 24781
# category Package
# catalog-ctan /macros/latex/contrib/hypdvips
# catalog-date 2011-12-06 18:13:39 +0100
# catalog-license lppl1.3
# catalog-version 2.04
Name:		texlive-hypdvips
Version:	2.04
Release:	2
Summary:	Hyperref extensions for use with dvips
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/hypdvips
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hypdvips.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hypdvips.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The hypdvips package fixes some problems when using hyperref
with dvips. It also adds support for breaking links, file
attachments, embedded documents and different types of GoTo-
links. The cooperation of hyperref with cleveref is improved,
which in addition allows an enhanced back-referencing system.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/hypdvips/hypdvips.sty
%doc %{_texmfdistdir}/doc/latex/hypdvips/README
%doc %{_texmfdistdir}/doc/latex/hypdvips/hypdvips.pdf
%doc %{_texmfdistdir}/doc/latex/hypdvips/images/example1.eps
%doc %{_texmfdistdir}/doc/latex/hypdvips/images/example2.eps
%doc %{_texmfdistdir}/doc/latex/hypdvips/images/example3.eps
%doc %{_texmfdistdir}/doc/latex/hypdvips/images/example4.eps
%doc %{_texmfdistdir}/doc/latex/hypdvips/images/example5.eps
%doc %{_texmfdistdir}/doc/latex/hypdvips/images/example6.eps
%doc %{_texmfdistdir}/doc/latex/hypdvips/images/example7.eps
%doc %{_texmfdistdir}/doc/latex/hypdvips/images/graph.eps
%doc %{_texmfdistdir}/doc/latex/hypdvips/images/icon_draft.eps
%doc %{_texmfdistdir}/doc/latex/hypdvips/images/ids.eps
%doc %{_texmfdistdir}/doc/latex/hypdvips/images/logfile.eps
%doc %{_texmfdistdir}/doc/latex/hypdvips/images/openmsg_six.eps
%doc %{_texmfdistdir}/doc/latex/hypdvips/images/openmsg_sixinbrowser.eps
%doc %{_texmfdistdir}/doc/latex/hypdvips/images/paperclip.eps
%doc %{_texmfdistdir}/doc/latex/hypdvips/images/pushpin.eps
%doc %{_texmfdistdir}/doc/latex/hypdvips/images/tag.eps
%doc %{_texmfdistdir}/doc/latex/hypdvips/manifest.txt

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 2.04-2
+ Revision: 752589
- Rebuild to reduce used resources

* Fri Dec 09 2011 Paulo Andrade <pcpa@mandriva.com.br> 2.04-1
+ Revision: 739779
- texlive-hypdvips

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 2.03-1
+ Revision: 718627
- texlive-hypdvips
- texlive-hypdvips
- texlive-hypdvips
- texlive-hypdvips

