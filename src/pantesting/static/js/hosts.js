angular.module('pantestingApp').controller('Hosts',
  function($scope, $rootScope) {
        $scope.openHost = function(host) {
            $scope.$parent.currentView = 'details';
        }


  });

angular.module('pantestingApp').controller('HostDetails',
  function($scope, $routeParams, $rootScope) {
      $scope.host = $scope.getHost($routeParams.hostId);
      $scope.bounties = [];

      $scope.isUserHostOwner = function() {
          return $rootScope.currentUser && $scope.host.user.name == $rootScope.currentUser.name;
      }
      $scope.getBounties = function() {
          $http.get('/get_bounties/' + $scope.host.id).success(function(data) {
              $scope.bounties = data.bounties;
          })
      }
      $scope.submitExploit = function(exploitId) {

      }
  });

angular.module('pantestingApp').controller('Profile',
  function($scope, $routeParams, $rootScope) {
      $scope.user = $rootScope.currentUser;
  });