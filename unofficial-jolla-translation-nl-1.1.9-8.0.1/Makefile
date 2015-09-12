all: compile

srcdir = .
DESTDIR =
prefix = $(DESTDIR)/usr
datadir = $(prefix)/share
TARGETS = alarm-ui-nl.qm ambience-babyflower-nl.qm ambience-camera-nl.qm ambience-grassroot-nl.qm ambience-moonship-nl.qm ambience-oldphone-nl.qm ambience-redtrain-nl.qm ambience-rope-nl.qm ambience-shadeofviolin-nl.qm ambience-storm-nl.qm ambience-the-first-one-nl.qm apkd-nl.qm as-daemon-nl.qm calculator-nl.qm calendar-nl.qm clock-nl.qm commhistoryd-nl.qm contactsd-nl.qm contacts-nl.qm csd-nl.qm devicelock-nl.qm gallery-ambience-nl.qm gallery-facebook-nl.qm gallery-nl.qm jolla-camera-nl.qm jolla-email-nl.qm jolla-keyboard-nl.qm jolla-mediaplayer-nl.qm jolla-signon-ui-nl.qm jolla-store-nl.qm launcher_settings-nl.qm libjollasignonuiservice_qt5-nl.qm lipstick-jolla-home-facebook-nl.qm lipstick-jolla-home-nl.qm lipstick-jolla-home-twitter-nl.qm lipstick-jolla-home-twitter-notif-nl.qm lipstick-nl.qm messages-nl.qm nemo-transfer-engine-nl.qm notes-nl.qm qmf-notifications-nl.qm remotesecurity-nl.qm sailfish-browser-nl.qm sailfish-btrfs-balancer-nl.qm sailfish_components_accounts_qt5-nl.qm sailfish_components_bluetooth_qt5-nl.qm sailfish_components_contacts_qt5-nl.qm sailfish_components_email_qt5-nl.qm sailfish_components_gallery_qt5-nl.qm sailfish_components_media-nl.qm sailfish_components_pickers_qt5-nl.qm sailfish_components_timezone_qt5-nl.qm sailfish_components_weather_qt5-nl.qm sailfish-maps-nl.qm sailfish-office-nl.qm sailfishsilica-qt5-nl.qm sailfish_transferengine-nl.qm sailfish_transferengine_plugins-nl.qm settings-1-nl.qm settings-accounts-activesync-nl.qm settings-accounts-nl.qm settings-backup-nl.qm settings-bluetooth-nl.qm settings-network-nl.qm settings-sailfish-browser-nl.qm settings-sailfishos-nl.qm settings-sailfish_utilities-nl.qm settings-sync-nl.qm settings-system-nl.qm simkit-nl.qm socialcache-nl.qm startupwizard-nl.qm tutorial-nl.qm voicecall-nl.qm voicecall_settings-nl.qm weather-nl.qm
INSTALLDATA = install -p -m 644
MKDIR = mkdir -p

compile: $(TARGETS)
	@echo Done

%.qm: %.ts
	/usr/lib/qt5/bin/lrelease -silent $^ -qm $@
#	lrelease-qt5 -silent $^ -qm $@

install: all
	$(MKDIR) $(datadir)/translations/
	$(MKDIR) $(datadir)/jolla-supported-languages/
	$(INSTALLDATA) $(srcdir)/*.qm $(datadir)/translations/
	$(INSTALLDATA) $(srcdir)/nl.conf $(datadir)/jolla-supported-languages/

clean:
	rm -f *.qm
