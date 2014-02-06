angular.module('pantestingApp').controller('PanTestingController',
  function($scope, $rootScope) {
      $scope.hosts = [{name: 'My Host', time_left: '1 week', company: 'My company 1', hostId: 0},
                        {name: 'PayPal.com', description: 'PayPal is awesome', 'url': 'http://paypal.com',
                            time_left: '24 hours', company: 'PayPal', hostId: 1}];

      $scope.getHost = function(hostId) {
            if (hostId == null) {
                return;
            }
            for (var i=0; i <    $scope.hosts.length; i++) {
                if ($scope.hosts[i].hostId.toString() == hostId.toString()) {
                    return $scope.hosts[i];
                }
            }
      }

      $rootScope.isAuthenticated = function() {
          return false;
      }
  });