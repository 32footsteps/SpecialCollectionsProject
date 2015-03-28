/**
* Collections
* @namespace scwebapp.collections.directives
*/
(function () {
	'use strict';

	angular
		.module('scwebapp.collections.directives')
		.directive('collections', collections);


	/**
	* @namespace Collections
	*/
	function collections() {
		/**
		* @name directive
		* @desc The returned directive
		* @memberOf scwebapp.collections.directives.Collections
		*/
		var directive = {
			controller: 'CollectionsController',
			controllerAs: 'vm',
			restrict: 'E',
			scope: {
				collections: '='
			},
			templateUrl: 'static/templates/collections/collections.html'
		};

		return directive;
	}
})();