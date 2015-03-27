/**
* Authentication
* @namespace scwebapp.authentication.services
*/
(function() {
	'use strict';

	angular
		.module('scwebapp.authentication.services')
		.factory('Authentication', Authentication);

	Authentication.$inject = ['$cookies', '$http'];

	/**
	* @namespace Authentication
	* @desc {Factory}
	*/
	function Authentication($cookies, $http) {
		/**
		* @name Authentication
		* @desc The Factory to be returned
		*/
		var Authentication = {
			getAuthenticatedAccount: getAuthenticatedAccount,
			isAuthenticated: isAuthenticated,
			login: login,
      logout: logout,
  		register: register,
  		setAuthenticatedAccount: setAuthenticatedAccount,
  		unauthenticate: unauthenticate

		};

		return Authentication;


    	////////////////////

    	/**
    	* @name register
    	* @desc Try to register a new user
    	* @param {string} email The email entered by the user
    	* @param {string} password The password entered by the user
    	* @param {string} username The username entered by the user
    	* @param {string} firstname The firstname entered by the user
    	* @param {string} lastname The lastname entered by the user
    	* @returns {Promise}
    	* @memberOf scwebapp.authentication.services.Authentication
    	*/
    	function register(email, password, username, firstname, lastname) {
			console.log("email " + email);
      return $http.post('/api/v1/scusers/', {
				email: email,
				password: password,
				username: username,
				first_name: firstname,
				last_name: lastname
			}).then(registerSuccessFn, registerErrorFn);
		

		/**
   		* @name registerSuccessFn
   		* @desc Set the authenticated account and redirect to index
   		*/
   		function registerSuccessFn(data, status, headers, config) {
   			Authentication.login(username, password);

   		}

   		/**
   		* @name registerErrorFn
   		* @desc Log "Failure!" to the console
   		*/
   		function registerErrorFn(data, status, header, config) {
   			console.error("Failure!");
   		}
}
		/**
    	* @name login
    	* @desc Try to login with the given username and password
    	* @param {string} password The password entered by the user
    	* @param {string} username The username entered by the user
    	* @returns {Promise}
    	* @memberOf scwebapp.authentication.services.Authentication
    	*/
    	function login(username, password) {
    		return $http.post('/api/v1/auth/login/', {
    			username: username,
    			password: password
    		}).then(loginSuccessFn, loginErrorFn);
    	}
    	
    	/**
   		* @name loginSuccessFn
   		* @desc Set the authenticated account and redirect to index
   		*/
   		function loginSuccessFn(data, status, headers, config) {
   			Authentication.setAuthenticatedAccount(data.data);

   			window.location = "/";
   		}

   		/**
   		* @name loginErrorFn
   		* @desc Log "Failure!" to the console
   		*/
   		function loginErrorFn(data, status, header, config) {
   			console.error("Failure!");
   		}


    	/**
 		* @name getAuthenticatedAccount
 		* @desc Return the currently authenticated account
 		* @returns {object|undefined} Account if authenticated, else `undefined`
 		* @memberOf scwebapp.authentication.services.Authentication
 		*/
 		function getAuthenticatedAccount() {
 			if (!$cookies.authenticatedAccount) {
    			return;
  			}

  			return JSON.parse($cookies.authenticatedAccount);
		}
 		/**
	 	* @name isAuthenticated
 		* @desc Check if the current user is authenticated
 		* @returns {boolean} True is user is authenticated, else false.
 		* @memberOf scwebapp.authentication.services.Authentication
 		*/
 		function isAuthenticated() {
 			return !!$cookies.authenticatedAccount;
 		}

 		/**
 		* @name setAuthenticatedAccount
 		* @desc Stringify the account object and store it in a cookie
 		* @param {Object} user The account object to be stored
 		* @returns {undefined}
 		* @memberOf scwebapp.authentication.services.Authentication
 		*/
 		function setAuthenticatedAccount(account) {
 			$cookies.authenticatedAccount = JSON.stringify(account);
 		}

 		/**
 		* @name unauthenticate
 		* @desc Delete the cookie where the user object is stored
 		* @returns {undefined}
 		* @memberOf scwebapp.authentication.services.Authentication
 		*/
 		function unauthenticate() {
 			delete $cookies.authenticatedAccount;
 		}

    /** 
    * @name logout
    * @desc try to log out
    * @returns {Promise}
    * @memberOf scwebapp.authentication.services.Authentication
    */
    function logout() {
      return $http.post('/api/v1/auth/logout/').then(logoutSuccessFn, logoutErrorFn);
        
        /**
        * @name logoutSuccessFn
        * @desc Unauthenticate and redirect to index page 
        */
        function logoutSuccessFn(data, status, headers, config) {
          Authentication.unauthenticate();

          window.location = '/';
        }

        /**
        * @name logoutErrorFn
        * @desc log "logout failure" to console
        */
        function logoutErrorFn(data, status, headers, config) {
          console.error('logout failure');
        }
    }
	
	}
})();