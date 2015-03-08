
(function () {
	'use strict';

	angular
		.module('scwebapp.authentication', [
			'scwebapp.authentication.controllers',
			'scwebapp.authentication.services'
			]);

	angular
		.module('scwebapp.authentication.controllers', []);

	angular
		.module('scwebapp.authentication.services', ['ngCookies']);
})();