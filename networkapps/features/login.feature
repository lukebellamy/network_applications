Feature: Login and logout of Citrix

	Scenario: Log in to Citrix
		Given user go to "http://ftcitrix.ft.com/Citrix/FTStoreFrontWeb/"
		When a user click on "#legalstatement-checkbox"
		When a user click "Install"
		When a user click "Continue"
		When a user log in as "yusuf.ogunjimi"
		And the user sees the app icon ".myapps-icon"
		When the user clicks on "apps-button"
		And the user clicks on add apps
		And user should see the link with the text "Citrix Administration Tools"

		#Then I should see "Administration Desktop" within 5 seconds

    Scenario: Log out of Citrix
		When user click username with id "header-username"
		And user clicks Log Off "userdetails-logoff"
	    Then a "Log On" should be seen
		#Then cancel the download popup

