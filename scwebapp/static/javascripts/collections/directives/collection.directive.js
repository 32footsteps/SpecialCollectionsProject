/**
* Collection
* @namespace scwebapp.collections.directives
*/
(function () {
  'use strict';

  angular
    .module('scwebapp.collections.directives')
    .directive('collection', collection);

  /**
  * @namespace Collection
  */
  function collection() {
    /**
    * @name directive
    * @desc The directive to be returned
    * @memberOf scwebapp.collections.directives.Collection
    */
    var directive = {
      restrict: 'E',
      scope: {
        collection: '='
      },
      templateUrl: '/static/templates/collections/collection.html'
    };

    return directive;
  }
})();