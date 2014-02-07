angular.module('pantestingApp').controller('Hosts',
  function($scope, $rootScope, $http) {
        $scope.openHost = function(host) {
            $scope.$parent.currentView = 'details';
        }

        $scope.getBountiesTotal = function(hostId) {
          var bountiesData = {count: 0, total: 0}
          $http.get('/get_bounties/' + hostId).success(function(data) {
              bountiesData.count = data.bounties.length;
              bountiesData.total = 0;
              for (var i in data.bounties) {
                  bountiesData.total += data.bounties[i].amount;
              }
          })
          return bountiesData;
        }

  });

angular.module('pantestingApp').controller('HostDetails',
  function($scope, $routeParams, $rootScope, $http) {
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
      $scope.getBounties();

      $scope.submitExploit = function(bountyId) {
          $http.post('/submit_exploit', {bountyId: bountyId,
                                          userId: $rootScope.currentUser.id})
      };

      $scope.addBounty = function(bountyType, bountyAmount) {
          $http.post('/add_bounty', {hostId: $scope.host.id,
                                      type: bountyType,
                                      amount: bountyAmount}).success(function() {
                 alert('Bounty added');
                 $scope.getBounties();
              });
      }
  });

angular.module('pantestingApp').controller('Profile',
  function($scope, $routeParams, $http, $rootScope) {
      $scope.user = $rootScope.currentUser;
      $scope.userHosts = [];
      $scope.approveExploit = function(exploitId) {
          $http.get('/approve_exploit/' + exploitId).success(function() {
              alert('Exploit approved')
          })
      }
      $scope.getHostsByUser = function() {
          $http.get('/get_hosts_by_user/' + $rootScope.currentUser.id).success(function(data) {
                $scope.userHosts = data.hosts;
          })
      }
      $scope.getHostsByUser();
  });