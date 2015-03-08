/**
* NavbarController
* @namespace scwebapp.layout.controllers
*/
(function () {
	'use strict';

	angular
		.module('scwebapp.layout.controllers')
		.controller('NavbarController', NavbarController);

	NavbarController.$inject = ['$scope', 'Authentication'];

	/**
	* @namespace NavbarController
	*/
	function NavbarController($scope, Authentication) {
		var vm = this;

		vm.logout = logout;

		/**
		* @name logout
		* @desc Log user out
		* @memberOf scwebapp.layout.controllers.NavbarController
		*/
		function logout() {
			Authentication.logout();
		}
	}

})();