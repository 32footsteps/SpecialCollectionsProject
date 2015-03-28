/**
* Collections
* @namespace scwebapp.collections.services
*/
(function () {
	'use strict';

	angular
		.module('scwebapp.collections.services')
		.factory('Collections', Collections);

	Collections.$inject = ['$http'];

	/**
	* @namespace Collections
	* @returns {Factory}
	*/
	function Collections($http) {
		var Collections = {
			all: all,
			create: create,
			get: get
		};

		return Collections;

	/***************************************************/

	/**
	* @name all
	* @desc Returns all collections
	* @returns {Promise}
	* @memberOf scwebapp.collections.services.Collections
	*/

	function all() {
		return $http.get('api/v1/collections/');
	}


	/**
	* @name create
	* @desc Creates a new Collection
	* @param {string} content The content of the new Collection
	* @returns {Promise}
	* @memberOf scwebapp.collections.services.Collections
	*/
	function create(name, content) {
		return $http.post('/api/v1/collections/', {
			collection_name: name,
			content: content
		});
	}

	/**
	* @name get
	* @desc Return all of a users collections
	* @param {string} username The username to get collection for
	* @returns {Promise}
	* @memberOf scwebapp.collections.services.Collections
	*/
	function get(username) {
		return $http.get('api/v1/accounts/' + username + '/collections/')
	}

	}

})();