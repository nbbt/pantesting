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
      $scope.submittedBounty = null;

      $scope.isUserHostOwner = function() {
          return $rootScope.currentUser && $scope.host.user.name == $rootScope.currentUser.name;
      }
      $scope.getBounties = function() {
          $http.get('/get_bounties/' + $scope.host.id).success(function(data) {
              $scope.bounties = data.bounties;
          })
      }
      $scope.getBounties();

      toastr.options.positionClass = 'toast-bottom-left';
      $scope.submitExploit = function(bountyId, description) {
          $http.post('/submit_exploit', {bountyId: bountyId,
                                          userId: $rootScope.currentUser.id,
                                          description: description}).success(function() {
                  toastr.success("Submitted");
              })
      };

      $scope.addBounty = function(bountyType, bountyAmount) {
          $http.post('/add_bounty', {hostId: $scope.host.id,
                                      type: bountyType,
                                      amount: bountyAmount}).success(function() {
                 toastr.success('Bounty Added!');
                 $scope.getBounties();
              }).error(function() {
                  toastr.error('Something went wrong..')
              });
      }

      $scope.like = function() {
          toastr.success('Liked!');
      }
  });

angular.module('pantestingApp').controller('Profile',
  function($scope, $routeParams, $http, $location, $rootScope) {
      $scope.user = $rootScope.currentUser;
      $scope.userHosts = [];
      $scope.submittedExploits = [];
      $scope.approveExploit = function(exploitId) {
          $http.put('/approve_exploit/' + exploitId).success(function() {
              toastr.success('Exploit approved');
          })
      }
      $scope.getHostsByUser = function() {
          $http.get('/get_hosts_by_user/' + $rootScope.currentUser.id).success(function(data) {
                $scope.userHosts = data.hosts;
          })
      }
      $scope.getSubmittedExploits = function() {
          $http.get('/get_submitted_exploits/' + $rootScope.currentUser.id).success(function(data) {
              $scope.submittedExploits = data.exploits;
          })
      }
      $scope.getSubmittedExploits();
      $scope.getHostsByUser();

      $scope.goToHost = function(hostId) {
          $location.path('/host/' + hostId);
      };
  });