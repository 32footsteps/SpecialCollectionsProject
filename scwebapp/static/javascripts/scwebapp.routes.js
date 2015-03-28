
(function (){
	'use strict';

	angular
		.module('scwebapp.routes')
		.config(config);

	config.$inject = ['$routeProvider'];

	/**
	* @name config
	* @desc Define valid routes for application 
	*/
	function config($routeProvider) {
		$routeProvider.when('/register', {
			controller: 'RegisterController',
			controllerAs: 'vm',
			templateUrl: '/static/templates/authentication/register.html'
		}).when('/login', {
			controller: 'LoginController',
			controllerAs: 'vm',
			templateUrl: '/static/templates/authentication/login.html'
		}).when('/database', {
			//controller: 'LoginController',
			//controllerAs: 'vm',
			templateUrl: '/templates/database.html'
		}).when('/', {
			controller: 'IndexController',
			controllerAs: 'vm',
			templateUrl: '/static/templates/layout/index.html'
		}).otherwise('/');
	}
})();