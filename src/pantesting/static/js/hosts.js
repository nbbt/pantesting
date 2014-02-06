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
          return $rootScope.currentUser && $scope.host.user.name == $rootScope.currentUser.name;
      }
  });

angular.module('pantestingApp').controller('Profile',
  function($scope, $routeParams, $rootScope) {
      $scope.user = $rootScope.currentUser;
  });