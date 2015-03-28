/**
* CollectionsController
* @namespace scwebapp.collections.controllers
*/
(function () {
	'use strict';

	angular
		.module('scwebapp.collections.controllers')
		.controller('CollectionsController', CollectionsController);

	CollectionsController.$inject = ['$scope'];

	/**
	* @namespace CollectionsController
	*/
	function CollectionsController($scope) {
		var vm = this;

		vm.columns = [];

		activate();

		/**
		* @name activate
		* @desc Actoins to be performed when this controller is instantiated
		* @memberOf scwebapp.controllers.CollectionsController
		*/
		function activate() {
			$scope.$watchCollection(function () { 
				return $scope.collections; }, render);

			$scope.$watch(function () {
				return $(window).width();}, render);
		}

		/**
    	* @name calculateNumberOfColumns
    	* @desc Calculate number of columns based on screen width
    	* @returns {Number} The number of columns containing Collections
    	* @memberOf scwebapp.collections.controllers.CollectionsControllers
    	*/
    	function calculateNumberOfColumns() {
    		var width = $(window).width();

    		if(width >= 1200) {
    			return 4;

    		}else if(width >= 992) {
    			return 3;

    		}else if(width >= 768) {
    			return 2;
    		
    		}else {
    			return 1;
    		}
    	}

    	/**
    	* @name approximateShortestColumn
    	* @desc An algorithm for approximating which column is shortest
    	* @returns The index of the shortest column
    	* @memberOf scwebapp.collections.controllers.CollectionsController
    	*/
    	function approximateShortestColumn() {
    		var scores = vm.columns.map(columnMapFn);

    		return scores.indexOf(Math.min.apply(this, scores));


    		/**
      		* @name columnMapFn
     		* @desc A map function for scoring column heights
      		* @returns The approximately normalized height of a given column
      		*/
      		function columnMapFn(column) {
      			var lengths = column.map(function (element) {
      				return element.content.length;
      			});

      			return lengths.reduce(sum, 0) * column.length;
      		}

      		/**
      		* @name sum
     		* @desc Sums two numbers
     		* @params {Number} m The first number to be summed
      		* @params {Number} n The second number to be summed
      		* @returns The sum of two numbers
      		*/
      		function sum(m, n) {
        		return m + n;
      		}
      	}

      		/**
    		* @name render
    		* @desc Renders Posts into columns of approximately equal height
    		* @param {Array} current The current value of `vm.collections`
    		* @param {Array} original The value of `vm.collections` before it was updated
    		* @memberOf scwebapp.collections.controllers.CollectionsController
    		*/
    		function render(current, original) {
    			if(current !== original) {
    				vm.columns = [];

    				for (var i = 0; i < calculateNumberOfColumns(); ++i) {
    					vm.columns.push([]);
    				}

    				for(var i = 0; i < current.length; ++i) {
    					var column = approximateShortestColumn();

    					vm.columns[column].push(current[i]);
    				}
    			}
    		}
    
    	
	}
})();