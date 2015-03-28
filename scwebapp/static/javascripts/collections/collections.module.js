(function () {
	'use strict';

	angular
		.module('scwebapp.collections', [
			'scwebapp.collections.controllers',
			'scwebapp.collections.directives',
			'scwebapp.collections.services'
		]);

	angular
		.module('scwebapp.collections.controllers', []);

	angular
		.module('scwebapp.collections.directives', ['ngDialog']);

	angular
		.module('scwebapp.collections.services', []);
})();