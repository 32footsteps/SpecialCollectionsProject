/**
* IndexController
* @namespace scwebapp.layout.controllers
*/
(function () {
	'use strict';

	angular
		.module('scwebapp.layout.controllers')
		.controller('IndexController', IndexController);

	IndexController.$inject = ['$scope', "Authentication", 'Collections', 'Snackbar'];

	/**
	* @namespace IndexController
	*/
	function IndexController($scope, Authentication, Collections, Snackbar) {
		var vm = this;

		vm.isAuthenticated = Authentication.isAuthenticated();
		vm.posts = [];

		activate();

		/**
		* @name activate
		* @desc Actions to be performed when controller is instantiated
		* @memberOf scwebapp.layout.controllers.IndexController
		*/
		function activate() {
			Collections.all().then(collectionsSuccessFn, collectionsErrorFn);

			$scope.$on('collection.created', function (event, post) {
				vm.collections.unshift(collection);
			});

			$scope.$on('collection.created.error', function () {
				vm.collections.shift();
			});

			/**
			* @name collectionsSuccessFn
			* @desc update collections array on view
			*/
			function collectionsSuccessFn(data, status, headers, config) {
				vm.posts = data.data;
			}

			/**
			* @name collectionsErrorFn
			* @descshow snackbar with error
			*/
			function collectionsErrorFn(data, status, headers, config) {
				Snackbar.error(data.error);
			}

		}
	}

})();
