#
# Conditional build:
%bcond_with	tests		# build with tests
%define		kdeappsver	24.08.3
%define		kframever	5.94.0
%define		qtver		5.15.2
%define		kaname		kdepim-runtime
Summary:	kdepim runtime
Name:		ka6-%{kaname}
Version:	24.08.3
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Libraries
Source0:	https://download.kde.org/stable/release-service/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	52c91a558e1427b091c5393224a1a3d4
URL:		http://www.kde.org/
BuildRequires:	Qt6Concurrent-devel
BuildRequires:	Qt6Core-devel >= %{qtver}
BuildRequires:	Qt6DBus-devel
BuildRequires:	Qt6Gui-devel >= 5.11.1
BuildRequires:	Qt6Network-devel
BuildRequires:	Qt6NetworkAuth-devel
BuildRequires:	Qt6Positioning-devel >= 5.11.1
BuildRequires:	Qt6PrintSupport-devel >= 5.11.1
BuildRequires:	Qt6Qml-devel >= 5.11.1
BuildRequires:	Qt6Quick-devel >= 5.11.1
BuildRequires:	Qt6Test-devel
BuildRequires:	Qt6TextToSpeech-devel
BuildRequires:	Qt6WebChannel-devel >= 5.11.1
BuildRequires:	Qt6WebEngine-devel >= 5.11.1
BuildRequires:	Qt6Widgets-devel
BuildRequires:	Qt6Xml-devel
BuildRequires:	cmake >= 3.20
BuildRequires:	cyrus-sasl-devel
BuildRequires:	gettext-devel
BuildRequires:	ka6-akonadi-calendar-devel >= %{kdeappsver}
BuildRequires:	ka6-akonadi-contacts-devel >= %{kdeappsver}
BuildRequires:	ka6-akonadi-devel >= %{kdeappsver}
BuildRequires:	ka6-akonadi-mime-devel >= %{kdeappsver}
BuildRequires:	ka6-akonadi-notes-devel >= %{kdeappsver}
BuildRequires:	ka6-kcalutils-devel >= %{kdeappsver}
BuildRequires:	ka6-kidentitymanagement-devel >= %{kdeappsver}
BuildRequires:	ka6-kimap-devel >= %{kdeappsver}
BuildRequires:	ka6-kmailtransport-devel >= %{kdeappsver}
BuildRequires:	ka6-kmbox-devel >= %{kdeappsver}
BuildRequires:	ka6-kmime-devel >= %{kdeappsver}
BuildRequires:	ka6-libkgapi-devel >= %{kdeappsver}
BuildRequires:	ka6-pimcommon-devel >= %{kdeappsver}
BuildRequires:	kf6-extra-cmake-modules >= %{kframever}
BuildRequires:	kf6-kcalendarcore-devel >= %{kframever}
BuildRequires:	kf6-kcodecs-devel >= %{kframever}
BuildRequires:	kf6-kconfig-devel >= %{kframever}
BuildRequires:	kf6-kconfigwidgets-devel >= %{kframever}
BuildRequires:	kf6-kcontacts-devel >= %{kframever}
BuildRequires:	kf6-kdav-devel >= %{kframever}
BuildRequires:	kf6-kdbusaddons-devel >= %{kframever}
BuildRequires:	kf6-kdoctools-devel >= %{kframever}
BuildRequires:	kf6-kholidays-devel >= %{kframever}
BuildRequires:	kf6-kiconthemes-devel >= %{kframever}
BuildRequires:	kf6-kio-devel >= %{kframever}
BuildRequires:	kf6-kitemmodels-devel >= %{kframever}
BuildRequires:	kf6-knotifications-devel >= %{kframever}
BuildRequires:	kf6-knotifyconfig-devel >= %{kframever}
BuildRequires:	kf6-ktextwidgets-devel >= %{kframever}
BuildRequires:	kf6-kwindowsystem-devel >= %{kframever}
BuildRequires:	libetebase-devel
BuildRequires:	libkolabxml-devel >= 1.1
BuildRequires:	libxslt-progs
BuildRequires:	ninja
BuildRequires:	qca-qt6-devel
BuildRequires:	qt6-build >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	shared-mime-info
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Obsoletes:	ka5-%{kaname} < %{version}
ExcludeArch:	x32 i686
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Runtime components for Akonadi KDE. This package contains Akonadi
agents written using KDE Development Platform libraries.

%prep
%setup -q -n %{kaname}-%{version}

%build
%cmake \
	-B build \
	-G Ninja \
	%{!?with_tests:-DBUILD_TESTING=OFF} \
	-DKDE_INSTALL_DOCBUNDLEDIR=%{_kdedocdir} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	-DQT_MAJOR_VERSION=6
%ninja_build -C build

%if %{with tests}
ctest --test-dir build
%endif


%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

rm -rf $RPM_BUILD_ROOT%{_kdedocdir}/{ko,sr}
%find_lang %{kaname} --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{kaname}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/akonadi_akonotes_resource
%attr(755,root,root) %{_bindir}/akonadi_birthdays_resource
%attr(755,root,root) %{_bindir}/akonadi_contacts_resource
%attr(755,root,root) %{_bindir}/akonadi_davgroupware_resource
%attr(755,root,root) %{_bindir}/akonadi_etesync_resource
%attr(755,root,root) %{_bindir}/akonadi_ews_resource
%attr(755,root,root) %{_bindir}/akonadi_ewsmta_resource
%attr(755,root,root) %{_bindir}/akonadi_google_resource
%attr(755,root,root) %{_bindir}/akonadi_ical_resource
%attr(755,root,root) %{_bindir}/akonadi_icaldir_resource
%attr(755,root,root) %{_bindir}/akonadi_imap_resource
%attr(755,root,root) %{_bindir}/akonadi_kolab_resource
%attr(755,root,root) %{_bindir}/akonadi_maildir_resource
%attr(755,root,root) %{_bindir}/akonadi_maildispatcher_agent
%attr(755,root,root) %{_bindir}/akonadi_mbox_resource
%attr(755,root,root) %{_bindir}/akonadi_migration_agent
%attr(755,root,root) %{_bindir}/akonadi_mixedmaildir_resource
%attr(755,root,root) %{_bindir}/akonadi_newmailnotifier_agent
%attr(755,root,root) %{_bindir}/akonadi_notes_resource
%attr(755,root,root) %{_bindir}/akonadi_openxchange_resource
%attr(755,root,root) %{_bindir}/akonadi_pop3_resource
#%attr(755,root,root) %{_bindir}/akonadi_tomboynotes_resource
%attr(755,root,root) %{_bindir}/akonadi_vcard_resource
%attr(755,root,root) %{_bindir}/akonadi_vcarddir_resource
%attr(755,root,root) %{_bindir}/gidmigrator
%ghost %{_libdir}/libakonadi-filestore.so.6
%attr(755,root,root) %{_libdir}/libakonadi-filestore.so.*.*
%ghost %{_libdir}/libakonadi-singlefileresource.so.6
%attr(755,root,root) %{_libdir}/libakonadi-singlefileresource.so.*.*
%ghost %{_libdir}/libfolderarchivesettings.so.6
%attr(755,root,root) %{_libdir}/libfolderarchivesettings.so.*.*
%ghost %{_libdir}/libkmindexreader.so.6
%attr(755,root,root) %{_libdir}/libkmindexreader.so.*.*
%ghost %{_libdir}/libmaildir.so.6
%attr(755,root,root) %{_libdir}/libmaildir.so.*.*
%ghost %{_libdir}/libnewmailnotifier.so.6
%attr(755,root,root) %{_libdir}/libnewmailnotifier.so.*.*
%attr(755,root,root) %{_libdir}/qt6/plugins/kf6/kio/akonadi.so
%dir %{_libdir}/qt6/plugins/pim6/akonadi/config
%attr(755,root,root) %{_libdir}/qt6/plugins/pim6/akonadi/config/akonotesconfig.so
%attr(755,root,root) %{_libdir}/qt6/plugins/pim6/akonadi/config/birthdaysconfig.so
%attr(755,root,root) %{_libdir}/qt6/plugins/pim6/akonadi/config/contactsconfig.so
%attr(755,root,root) %{_libdir}/qt6/plugins/pim6/akonadi/config/googleconfig.so
%attr(755,root,root) %{_libdir}/qt6/plugins/pim6/akonadi/config/icalconfig.so
%attr(755,root,root) %{_libdir}/qt6/plugins/pim6/akonadi/config/icaldirconfig.so
%attr(755,root,root) %{_libdir}/qt6/plugins/pim6/akonadi/config/maildirconfig.so
%attr(755,root,root) %{_libdir}/qt6/plugins/pim6/akonadi/config/maildispatcherconfig.so
%attr(755,root,root) %{_libdir}/qt6/plugins/pim6/akonadi/config/mboxconfig.so
%attr(755,root,root) %{_libdir}/qt6/plugins/pim6/akonadi/config/mixedmaildirconfig.so
%attr(755,root,root) %{_libdir}/qt6/plugins/pim6/akonadi/config/newmailnotifierconfig.so
%attr(755,root,root) %{_libdir}/qt6/plugins/pim6/akonadi/config/notesconfig.so
%attr(755,root,root) %{_libdir}/qt6/plugins/pim6/akonadi/config/openxchangeconfig.so
%attr(755,root,root) %{_libdir}/qt6/plugins/pim6/akonadi/config/pop3config.so
#%attr(755,root,root) %{_libdir}/qt6/plugins/pim6/akonadi/config/tomboynotesconfig.so
%attr(755,root,root) %{_libdir}/qt6/plugins/pim6/akonadi/config/vcardconfig.so
%attr(755,root,root) %{_libdir}/qt6/plugins/pim6/akonadi/config/vcarddirconfig.so
%attr(755,root,root) %{_libdir}/qt6/plugins/pim6/kcms/kaddressbook/kcm_ldap.so
%attr(755,root,root) %{_libdir}/qt6/plugins/pim6/mailtransport/mailtransport_akonadiplugin.so
%{_datadir}/akonadi/agents/akonotesresource.desktop
%{_datadir}/akonadi/agents/birthdaysresource.desktop
%{_datadir}/akonadi/agents/contactsresource.desktop
%{_datadir}/akonadi/agents/davgroupwareresource.desktop
%{_datadir}/akonadi/agents/etesyncresource.desktop
%{_datadir}/akonadi/agents/ewsmtaresource.desktop
%{_datadir}/akonadi/agents/ewsresource.desktop
%{_datadir}/akonadi/agents/googleresource.desktop
%{_datadir}/akonadi/agents/icaldirresource.desktop
%{_datadir}/akonadi/agents/icalresource.desktop
%{_datadir}/akonadi/agents/imapresource.desktop
%{_datadir}/akonadi/agents/kolabresource.desktop
%{_datadir}/akonadi/agents/maildirresource.desktop
%{_datadir}/akonadi/agents/maildispatcheragent.desktop
%{_datadir}/akonadi/agents/mboxresource.desktop
%{_datadir}/akonadi/agents/migrationagent.desktop
%{_datadir}/akonadi/agents/mixedmaildirresource.desktop
%{_datadir}/akonadi/agents/newmailnotifieragent.desktop
%{_datadir}/akonadi/agents/notesresource.desktop
%{_datadir}/akonadi/agents/openxchangeresource.desktop
%{_datadir}/akonadi/agents/pop3resource.desktop
#%{_datadir}/akonadi/agents/tomboynotesresource.desktop
%{_datadir}/akonadi/agents/vcarddirresource.desktop
%{_datadir}/akonadi/agents/vcardresource.desktop
%dir %{_datadir}/akonadi/davgroupware-providers
%{_datadir}/akonadi/davgroupware-providers/citadel.desktop
%{_datadir}/akonadi/davgroupware-providers/davical.desktop
%{_datadir}/akonadi/davgroupware-providers/egroupware.desktop
%{_datadir}/akonadi/davgroupware-providers/mailbox-org.desktop
%{_datadir}/akonadi/davgroupware-providers/nextcloud.desktop
%{_datadir}/akonadi/davgroupware-providers/opengroupware.desktop
%{_datadir}/akonadi/davgroupware-providers/owncloud-pre5.desktop
%{_datadir}/akonadi/davgroupware-providers/owncloud-pre9.desktop
%{_datadir}/akonadi/davgroupware-providers/owncloud.desktop
%{_datadir}/akonadi/davgroupware-providers/scalix.desktop
%{_datadir}/akonadi/davgroupware-providers/sogo.desktop
%{_datadir}/akonadi/davgroupware-providers/yahoo.desktop
%{_datadir}/akonadi/davgroupware-providers/zarafa.desktop
%{_datadir}/akonadi/davgroupware-providers/zimbra.desktop
%dir %{_datadir}/akonadi/firstrun
%{_datadir}/akonadi/firstrun/birthdaycalendar
%{_datadir}/akonadi/firstrun/defaultaddressbook
%{_datadir}/akonadi/firstrun/defaultcalendar
%{_datadir}/akonadi/firstrun/defaultnotebook
%{_desktopdir}/org.kde.akonadi_contacts_resource.desktop
%{_desktopdir}/org.kde.akonadi_davgroupware_resource.desktop
%{_desktopdir}/org.kde.akonadi_ews_resource.desktop
%{_desktopdir}/org.kde.akonadi_google_resource.desktop
%{_desktopdir}/org.kde.akonadi_imap_resource.desktop
%{_desktopdir}/org.kde.akonadi_kolab_resource.desktop
%{_desktopdir}/org.kde.akonadi_openxchange_resource.desktop
%{_desktopdir}/org.kde.akonadi_vcard_resource.desktop
%{_desktopdir}/org.kde.akonadi_vcarddir_resource.desktop
%{_datadir}/dbus-1/interfaces/org.kde.Akonadi.Maildir.Settings.xml
%{_datadir}/dbus-1/interfaces/org.kde.Akonadi.MixedMaildir.Settings.xml
%{_iconsdir}/hicolor/*x*/apps/*.png
%{_datadir}/knotifications6/akonadi_ews_resource.notifyrc
%{_datadir}/knotifications6/akonadi_google_resource.notifyrc
%{_datadir}/knotifications6/akonadi_maildispatcher_agent.notifyrc
%{_datadir}/knotifications6/akonadi_newmailnotifier_agent.notifyrc
%{_datadir}/knotifications6/akonadi_pop3_resource.notifyrc
%{_datadir}/mime/packages/kdepim-mime.xml
%{_datadir}/qlogging-categories6/kdepim-runtime.categories
%{_datadir}/qlogging-categories6/kdepim-runtime.renamecategories
%{_datadir}/knotifications6/akonadi_imap_resource.notifyrc
