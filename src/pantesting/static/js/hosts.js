angular.module('pantestingApp').controller('Hosts',
  function($scope, $rootScope) {
        $scope.openHost = function(host) {
            $scope.$parent.currentView = 'details';
        }
  });

angular.module('pantestingApp').controller('HostDetails',
  function($scope, $routeParams, $rootScope) {
      $scope.host = $scope.getHost($routeParams.hostId);

      $scope.isUserHostOwner = function() {
          return $scope.host.user == $rootScope.currentUser.username;
      }
  });