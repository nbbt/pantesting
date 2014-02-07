angular.module('pantestingApp').controller('PanTestingController',
  function($scope, $rootScope, $http, $location, Host) {
      $scope.hosts = Host.query();

      $scope.refreshHosts = function() {
          $scope.hosts = Host.query();
      }


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
      $scope.newHost = function(hostName, hostDescription, bounties, hostUrl) {
           $http.post('/new_host', JSON.stringify({"hostName": hostName, "description": hostDescription, "bounties": bounties,
                                                    "userId": $rootScope.currentUser.id, url: hostUrl}))
                .success(function(data) {
                   toastr.success('New host created');
                   $scope.refreshHosts();
               });
      }
      $scope.removeHost = function(hostId) {
          $http.delete('/remove_host/' + hostId.toString()).success(function() {
              toastr.success('Host deleted');
              $location.path('/');
          })
      }

      $rootScope.currentUser = null;
      $rootScope.isAuthenticated = function() {
          return $rootScope.currentUser != null;
      }
      $rootScope.authenticate = function(username, password) {
          $http.post('/login', {username: username, password: password}).success(function() {
                    $rootScope.getCurrentUser();
                    toastr.success('Logged in');
          }).error(function() {
                  toastr.error('Access Denied');
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
          }).success(function() {
                  toastr.info('Logged out');
              });
      }
      $rootScope.getCurrentUser();
  });