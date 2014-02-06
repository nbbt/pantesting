angular.module('pantestingApp').controller('PanTestingController',
  function($scope, $rootScope, Host) {
      /*scope.hosts = [{name: 'My Host', time_left: '1 week', company: 'My company 1', hostId: 0},
                        {name: 'PayPal.com', description: 'PayPal is awesome', 'url': 'http://paypal.com', user: "newt",
                            time_left: '24 hours', company: 'PayPal', hostId: 1}];
      */
      $scope.hosts = Host.query();

      $scope.getHost = function(hostId) {
            if (hostId == null) {
                return;
            }
            for (var i=0; i < $scope.hosts.all.length; i++) {
                if ($scope.hosts[i].id.toString() == hostId.toString()) {
                    return $scope.hosts[i];
                }
            }
      }

      $rootScope.currentUser = null;
      $rootScope.isAuthenticated = function() {
          return $rootScope.currentUser != null;
      }
      $rootScope.authenticate = function(username, password) {
          if (true) {
              $rootScope.currentUser = {username: username}
          }
      }
      $rootScope.logout = function() {
          $rootScope.currentUser = null;
      }
  });