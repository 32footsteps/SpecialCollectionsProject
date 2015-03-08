/**
* LoginController
* @namespace scwebapp.authentication.controllers
*/
(function () {
	'use strict';

	angular
		.module('scwebapp.authentication.controllers')
		.controller('LoginController', LoginController);

	LoginController.$inject = ['$location', '$scope', 'Authentication'];

	/**
	* @namespace LoginController
	*/
	function LoginController($location, $scope, Authentication) {
		var vm = this;

		vm.login = login;

		activate();

		/**
		* @name activate
		* @desc Actions to be preformed when this controller is instantiated
		* @memberOf scwebapp.authentication.controllers.LoginController
		*/
		function activate() {
			if(Authentication.isAuthenticated()) {
				$location.url('/');
			}
		}

		/**
		* @name login
		* @desc Logs user in
		* @memberOf scwebapp.authentication.controllers.LoginController
		*/
		function login() {
			Authentication.login(vm.username, vm.password);
		}

	}
})();