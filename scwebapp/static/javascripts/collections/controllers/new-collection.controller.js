/**
* NewCollectionController
* @namespace scwebapp.collections.controllers
*/
(function () {
  'use strict';

  angular
    .module('scwebapp.collections.controllers')
    .controller('NewCollectionController', NewCollectionController);

  NewCollectionController.$inject = ['$rootScope', '$scope', 'Authentication', 'Snackbar', 'Collections'];

  /**
  * @namespace NewPostController
  */
  function NewCollectionController($rootScope, $scope, Authentication, Snackbar, Posts) {
    var vm = this;

    vm.submit = submit;

    /**
    * @name submit
    * @desc Create a new Collection
    * @memberOf scwebapp.collections.controllers.NewPostController
    */
    function submit() {
      $rootScope.$broadcast('collection.created', {
        content: vm.content,
        author: {
          username: Authentication.getAuthenticatedAccount().username
        }
      });

      $scope.closeThisDialog();

      Posts.create(vm.content).then(createCollectionSuccessFn, createCollectionErrorFn);


      /**
      * @name createCollectionSuccessFn
      * @desc Show snackbar with success message
      */
      function createCollectionSuccessFn(data, status, headers, config) {
        Snackbar.show('Success! Collection created.');
      }


      /**
      * @name createPostErrorFn
      * @desc Propogate error event and show snackbar with error message
      */
      function createCollectionErrorFn(data, status, headers, config) {
        $rootScope.$broadcast('collection.created.error');
        Snackbar.error(data.error);
      }
    }
  }
})();