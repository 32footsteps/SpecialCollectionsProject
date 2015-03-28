(function () {
	'use strict';

	angular
		.module('scwebapp', [
			'scwebapp.config',
			'scwebapp.routes',
			'scwebapp.authentication',
			'scwebapp.layout',
			'scwebapp.collections',
			'scwebapp.utils'
		]);

	angular
		.module('scwebapp.routes', ['ngRoute']);

	angular
		.module('scwebapp.config', []);

	angular
		.module('scwebapp')
		.run(run);

	run.$inject = ['$http'];

	function run($http) {
		$http.defaults.xsrfHeaderName = 'X-CSRFToken';
		$http.defaults.xsrfCookieName = 'csrftoken';
	}
})();