angular.module('pantestingApp').controller('PanTestingController',
  function($scope, $rootScope, $http, Host) {
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
                if ($scope.hosts.all[i].id.toString() == hostId.toString()) {
                    return $scope.hosts.all[i];
                }
            }
      }
      $scope.newHost = function(hostName, hostDescription, bounties) {
           $http.post('/new_host', JSON.stringify({"hostName": hostName, "description": hostDescription, "bounties": bounties,
                                                    "userId": $rootScope.currentUser.id}))
                .success(function(data) {
                   alert('New host created');
               });
      }
      $scope.removeHost = function(hostId) {
          $http.get('/remove_host/' + hostId.toString()).success(function() {
              alert('Deleted');
          })
      }

      $rootScope.currentUser = null;
      $rootScope.isAuthenticated = function() {
          return $rootScope.currentUser != null;
      }
      $rootScope.authenticate = function(username, password) {
          $http.post('/login', {username: username, password: password}).success(function() {
                    $rootScope.getCurrentUser();
          });
      }
      $rootScope.getCurrentUser = function() {
          $http.get('/get_user').success(function(data) {
                if (data) {
                    $rootScope.currentUser = data;
                }
          });
      }
      $rootScope.logout = function() {
          $http.get('/logout').success(function() {
                $rootScope.currentUser = null;
          });
      }
      $rootScope.getCurrentUser();
  });